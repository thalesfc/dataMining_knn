# -*- coding: utf-8 -*-
import re
import scipy.spatial.distance as spd
import numpy as np
import heapq
from sys import stderr
from time import clock
import result
import load_data as ld


def load_answers(train_path):
    f = open(train_path)
    answers = []
    for line in f:
        tokens = line.split()
        answers.append(int(tokens[0]))
    return answers


def tokenize_line(line):
    #replace bad caracteres
    line = re.sub(ld.split_regex, ' ', line)

    #tokenize
    tokens = line.split()
    return tokens


def load_vocabulary(train_path, stopwords):
    f = open(train_path)
    voc = {}
    count = 0
    for line in f:
        # tokenize
        tokens = tokenize_line(line)
        for word in tokens:
            # skip small words
            if len(word) < 2:
                continue
            # skip stop words
            elif stopwords and (word in stopwords):
                continue
            else:
                #check if this word is in the dictionary
                if (not (word in voc)):
                    voc[word] = count
                    count += 1
    return voc


def transform(voc, path):
    struct = []
    f = open(path)
    for line in f:
        space = np.zeros(len(voc), np.bool)
        tokens = tokenize_line(line)
        for word in tokens:
            if word in voc:
                word_id = voc[word]
                space[word_id] = True
        struct.append(space)
    return struct


def main():
    print "# KNN Classifier"
    parser = ld.parse_arguments()

    # priting args
    print '\t-k = ' + str(parser.k)
    print '\t-d = ' + parser.distance

    stopwords = None
    if parser.stopwords_path:
        stopwords = ld.load_stopwords(parser.stopwords_path)

    voc = load_vocabulary(parser.train_path, stopwords)
    answers = load_answers(parser.train_path)

    train = transform(voc, parser.train_path)
    test = transform(voc, parser.test_path)

    # output file
    out_path = '../results/' + parser.distance + '_' + str(parser.k)
    out_path += '.txt'
    out_file = open(out_path, 'w')

    for point in test:
        neighbors = []
        for i in xrange(len(train)):
            neigh = train[i]
            distance = 0.0

            if parser.distance == 'cosine':
                distance = spd.cosine(neigh, point)
            elif parser.distance == 'jaccard':
                distance = spd.jaccard(neigh, point)
            elif parser.distance == 'euclidean':
                distance = spd.euclidean(neigh, point)
            elif parser.distance == 'dice':
                distance = spd.dice(neigh, point)
            elif parser.distance == 'correlation':
                distance = spd.correlation(neigh, point)
            elif parser.distance == 'manhattan':
                distance = spd.cityblock(neigh, point)
            else:
                print >> stderr, "ERRO! -  Distância informada inválida."
                exit()

            tup = (distance, i)
            heapq.heappush(neighbors, tup)

        # return the highest k similar points
        top_k = heapq.nsmallest(parser.k, neighbors)

        # classifing
        classification = np.zeros(2)
        for (_, idi) in top_k:
            classe = answers[idi]
            classification[int(classe)] += 1

        # outputing classification
        if(classification[0] >= classification[1]):
            print >> out_file, '0'
            print '0'
        else:
            print >> out_file, '1'
            print '1'

    # outputing the results'
    print
    print "# Resultados salvos no arquivo: " + out_path
    out_file.close()
    result.result("../data/imdb_test", out_path)


if __name__ == '__main__':
    t1 = clock()
    main()
    t2 = clock()
    print "# Tempo de execução", (t2 - t1), "s"
