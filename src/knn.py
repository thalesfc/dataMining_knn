# -*- coding: utf-8 -*-
import load_data as ld
import space
import scipy.spatial.distance as spd
import heapq
import numpy as np
from sys import stderr


def main():
    print "# KNN Classifier"
    parser = ld.parse_arguments()

    stopwords = None
    if parser.stopwords_path:
        stopwords = ld.load_stopwords(parser.stopwords_path)

    # priting args
    print "Args: \n"
    print '-k = ' + str(parser.k)
    print '-d = ' + parser.distance

    # loading the necessary data
    (vocabulary, neigh_classes) = ld.load_train(parser.train_path, stopwords)

    # transforming each item to a v-dimensional space
    (train, test) = space.transform(vocabulary, parser.train_path,
                                    parser.test_path)

    # output file
    out_path = '../results/' + parser.distance + '_' + str(parser.k)
    out_path += '.txt'
    out_file = open(out_path, 'w')

    # knn classification
    print "# Classifying"
    for item in test:
        print "*",
        dist_heap = []

        # calculates the distance to every point in the training set
        for i in xrange(len(train)):
            point = train[i]
            distance = 0.0

            if parser.distance == 'cosine':
                distance = spd.cosine(item, point)
            elif parser.distance == 'jaccard':
                distance = spd.jaccard(item, point)
            elif parser.distance == 'euclidean':
                distance = spd.euclidean(item, point)
            elif parser.distance == 'dice':
                distance = spd.dice(item, point)
            elif parser.distance == 'correlation':
                distance = spd.correlation(item, point)
            elif parser.distance == 'manhattan':
                distance = spd.cityblock(item, point)
            else:
                print >> stderr, "ERRO! -  Distância informada inválida."
                exit()

            tup = (distance, i)
            heapq.heappush(dist_heap, tup)

        # return the highest k similar points
        top_k = heapq.nlargest(parser.k, dist_heap)

        # classifing
        classification = np.zeros(2)
        for (_, idi) in top_k:
            classe = neigh_classes[idi]
            classification[int(classe)] += 1

        # outputing classification
        if(classification[0] >= classification[1]):
            print >> out_file, '0'
        else:
            print >> out_file, '1'
    print "# Resultados salvos no arquivo: " + out_path

if __name__ == '__main__':
    main()
