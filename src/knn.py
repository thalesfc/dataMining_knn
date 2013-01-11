# -*- coding: utf-8 -*-
import load_data as ld
import space


def main():
    parser = ld.parse_arguments()

    stopwords = None
    if parser.stopwords_path:
        stopwords = ld.load_stopwords(parser.stopwords_path)

    # loading the necessary data
    (vocabulary, neigh_classes) = ld.load_train(parser.train_path, stopwords)

    # transforming each item to a v-dimensional space
    (train, test) = space.transform(vocabulary, parser.train_path,
                                    parser.test_path)

    # knn classification
    # TODO

if __name__ == '__main__':
    main()
