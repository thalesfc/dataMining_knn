# -*- coding: utf-8 -*-
import load_data as ld
import re
import numpy as np


def extract_terms(voc, line):
    ''' Given a line, computes the elements space '''
    space = np.zeros(len(voc), np.int)
    tokens = re.split(ld.split_regex, line)
    for i in range(1, len(tokens)):
        word = tokens[i]

        if word in voc:
            word_id = voc[word]
            space[word_id] += 1

    return space


def train_transform(voc, train_p):
    ''' Transform the train to a v-dimensional space '''
    # transforming the train
    train = []
    f = open(train_p)

    for line in f:
        element = extract_terms(voc, line)
        train.append(element)

    return train


def transform(voc, train_p, test_p):
    ''' Transform the itens to a v-dimensional space '''

    # transforming the train
    train = train_transform(voc, train_p)

    # test
    test = []
    f = open(test_p)

    for line in f:
        element = extract_terms(voc, line)
        test.append(element)

    return (train, test)
