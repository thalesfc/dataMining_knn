# -*- coding: utf-8 -*-
import load_data as ld
import re
import numpy as np


def transform(voc, train_p, test_p):
    ''' Transform the itens to a v-dimensional space '''

    # transforming the train
    train = []
    f = open(train_p)

    for line in f:
        space = np.zeros(len(voc))
        tokens = re.split(ld.split_regex, line)
        for i in range(1, len(tokens)):
            word = tokens[i]

            if word in voc:
                word_id = voc[word]
                space[word_id] += 1

        train.append(space)

    # test
    test = []
    f = open(test_p)

    for line in f:
        space = np.zeros(len(voc))
        tokens = re.split(ld.split_regex, line)
        for i in range(1, len(tokens)):
            word = tokens[i]

            if word in voc:
                word_id = voc[word]
                space[word_id] += 1

        test.append(space)

    return (train, test)
