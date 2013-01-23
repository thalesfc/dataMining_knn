# -*- coding: utf-8 -*-
import load_data as ld
import space
import scipy.spatial.distance as spd
import heapq
import numpy as np
from time import clock


def main():
    parser = ld.parse_arguments()

    print "#### LEAVE ONE OUT "
    print "# KNN Classifier", parser.k

    # stopwords
    stopwords = None
    if parser.stopwords_path:
        stopwords = ld.load_stopwords(parser.stopwords_path)

    # loading the necessary data
    (vocabulary, neigh_classes) = ld.load_train(parser.train_path, stopwords)

    # transforming each item to a v-dimensional space
    train = space.train_transform(vocabulary, parser.train_path)

    print "# Classifying"
    acc = 0

    for x in xrange(len(train)):
        dist_heap = []
        item = train[x]
        for i in xrange(len(train)):
            # skipping the own element
            if x == i:
                continue
            point = train[i]
            distance = spd.euclidean(item, point)

            tup = (distance, i)
            heapq.heappush(dist_heap, tup)

        # return the highest k similar points
        top_k = heapq.nsmallest(parser.k, dist_heap)

        # classifing
        classification = np.zeros(2)
        for (_, idi) in top_k:
            classe = neigh_classes[idi]
            classification[int(classe)] += 1

        out_class = 0
        if(classification[0] >= classification[1]):
            out_class = 0
        else:
            out_class = 1

        print x, " -> ", out_class, neigh_classes[x]

        # increment the acc
        if out_class == neigh_classes[x]:
            acc += 1

    print "# Acurácia para ", parser.k, ": ",
    print acc, float(acc) / float(len(train))


if __name__ == '__main__':
    t1 = clock()
    main()
    t2 = clock()
    print "# Tempo de execução", (t2 - t1), "s"
