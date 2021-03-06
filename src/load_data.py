# -*- coding: utf-8 -*-
from optparse import OptionParser
import re

#regex
split_regex = "[\\\^´`>0123456789_\[\]@/\+\-=()*%&$#|\s\"':;,.!?!\n]+"


def parse_arguments():
    '''parse the arguments provided in the command line'''

    usage_text = 'Usage: %progi -i <arquivo treino> -t <arquivo teste>'
    usage_text += ' -k <número de vizinhos> [-s stopwords -d distance -m porcentagem]'

    parser = OptionParser(usage=usage_text)

    parser.add_option('-k', '--k_num', type='int',
                      help='número de neighboors', dest='k')

    parser.add_option('-m', '--max', type='float',
                      help='porcentagem da base a ser utilizada', dest='percentage')

    parser.add_option('-i', '--treino', type='string',
                      help='arquivo treino', dest='train_path')

    parser.add_option('-t', '--teste', type='string',
                      help='arquivo teste', dest='test_path')

    parser.add_option('-s', '--stopwords', type='string',
                      help='arquivo stopwords', dest='stopwords_path')

    parser.add_option('-d', '--distance', type='string',
                      help='distance = cosine', dest='distance')

    (options, args) = parser.parse_args()

    if not options.k:
        parser.error('Número de vizinhos não fornecido.')

    if not options.test_path:
        parser.error('Arquivo de teste não fornecido.')

    if not options.train_path:
        parser.error('Arquivo de treino não fornecido.')

    if not options.distance:
        options.distance = 'euclidean'

    if not options.percentage:
        options.percentage = 1

    return options


def load_stopwords(path):
    ''' Load the stowords file '''
    print "Loading Stop words"
    stopwords_set = set()
    f = open(path)
    for line in f:
        tokens = line.split("\n")
        stopwords_set.add(tokens[0])

    return stopwords_set


def load_train(path, stopwords):
    ''' Load the train information '''
    print "\n# Loading train"

    voc = {}
    f = open(path)

    count = 0

    for line in f:
        tokens = re.split(split_regex, line)

        # empty first token
        # creating the vocabulary
        for i in range(1, len(tokens)):
            word = tokens[i]

            # skipping empty words
            if not word:
                continue

            # skipping if words in stopwords
            if stopwords and (word in stopwords):
                continue

            if not word in voc:
                voc[word] = count
                count += 1

    nei_class = []
    # loading the answers
    f = open(path)
    count = 0
    for line in f:
        tokens = line.split(' ')
        classe = int(tokens[0])
        nei_class.append(classe)

    return (voc, nei_class)
