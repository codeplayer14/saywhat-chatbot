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

    
    