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