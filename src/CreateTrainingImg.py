#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import Image
import tokenize
import numpy as np
from matplotlib import pyplot as plt
import os

file = open('train.csv','rt')
# load the csv data

data_reader = csv.reader(file)
img_examples = list()

for row in data_reader:
  img_examples.append(row)

for i in range(1,len(img_examples)):
  if(i == 1000):
    break
  elm_tokens = map(int, img_examples[i][1].split(' '))  
  print len(elm_tokens), img_examples[i][0] 
  elm_tokens = np.array(elm_tokens,dtype=np.uint8)
  elm_tokens = elm_tokens.reshape(48,48)
  img = Image.fromarray(elm_tokens)
  #img.save(str(i)+"face" + ".thumbnail", "JPEG")
  print elm_tokens.shape

