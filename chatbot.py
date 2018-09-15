# -*- coding: utf-8 -*-

#Data processing

import numpy as np
import tensorflow as tf
import re
import time
 

lines = open('./dataset/movie_lines.txt',encoding='utf-8',errors='ignore').read().split('\n')
 
conversations = open('./dataset/movie_conversations.txt',
                     encoding='utf-8',errors='ignore').read().split('\n')

id2line = {}
for line in lines:
    _line = line.split(' +++$+++ ')
    if(len(_line) == 5):
        id2line[_line[0]] = _line[4]

conversation_ids = []
for conversation in conversations:
    _conversation = conversation.split(' +++$+++ ')[-1][1:-1].replace("'","").replace(" ","")
    conversation_ids.append(_conversation.split(','))

questions = []
answers = []

for conversation in conversation_ids:
    for index in range(len(conversation)-1):
        questions.append(id2line[conversation[index]])
        answers.append(id2line[conversation[index+1]])

def clean_text(text):
    text = text.lower()
    text = re.sub(r"i'm","i am",text)
    text = re.sub(r"he's","he is",text)
    text = re.sub(r"she's","she is",text)
    text = re.sub(r"i'm","i am",text)
    text = re.sub(r"that's","that is",text)
    text = re.sub(r"what's","what is",text)
    text = re.sub(r"where's","where is",text)
    text = re.sub(r"\'ll","will",text)
    text = re.sub(r"\'ve","have",text)
    text = re.sub(r"\'d","would",text)
    text = re.sub(r"won't","will not",text)
    text = re.sub(r"can't","cannot",text)
    text = re.sub(r"[-()\"#/@;:<>{}+=-|.?,]","",text)
    return text
 
clean_questions = []
clean_answers = []
for question in questions:
    clean_questions.append(clean_text(question))
    
for answer in answers:
    clean_answers.append(clean_text(answer))

word2count = {}

for question in clean_questions:
    for word in question.split():
        if word not in word2count:
            word2count[word] = 1
        else:
            word2count[word] += 1
for answer in clean_answers:
    for word in answer.split():
        if word not in word2count:
            word2count[word] = 1
        else:
            word2count[word] += 1

threshold = 20

questionswords2int = {}
answerswords2int = {}

word_number = 0
for word,count in word2count.items():
    if count>=threshold:
        questionswords2int[word] = word_number
        word_number += 1

word_number = 0
for word,count in word2count.items():
    if count>=threshold:
        answerswords2int[word] = word_number
        word_number += 1

tokens = ['<PAD>','<EOS>','<OUT>','<SOS>']
for token in tokens:
    questionswords2int[token] = len(questionswords2int)+1

for token in tokens:
    answerswords2int[token] = len(answerswords2int)+1      

answersint2word = {integer_val:word_key for word_key,integer_val in answerswords2int.items()}


for i in range(len(clean_answers)):
    clean_answers[i]+='<EOS>'
    
# Converted questions and answers to int
questions_to_int = []
answers_to_int = []
for question in clean_questions:
    ints = []
    for word in question.split():
        if word not in questionswords2int:
            ints.append(questionswords2int['<OUT>'])
        else:
            ints.append(questionswords2int[word])
    questions_to_int.append(ints)
for answer in clean_answers:
    ints = []
    for word in answer.split():
        if word not in answerswords2int:
            ints.append(answerswords2int['<OUT>'])
        else:
            ints.append(answerswords2int[word])
    answers_to_int.append(ints)