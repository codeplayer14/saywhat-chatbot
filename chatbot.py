# -*- coding: utf-8 -*-

#Data processing

import numpy as np
import tensorflow as tf
import re
import time
 

lines = open('./dataset/movie_lines.txt',encoding='utf-8',errors='ignore').read().split('\n')

conversations = open('./dataset/movie_lines.txt',
                     encoding='utf-8',errors='ignore').read().split('\n')