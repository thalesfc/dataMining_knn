from sys import argv


def result(path_answer, path_classification):
    # loading the answer
    answer = []
    count = 0
    f = open(path_answer)
    for line in f:
        tokens = line.split(' ')
        classe = tokens[0]
        answer.append(classe)
        count += 1

    # loading the classification
    classification = []
    f = open(path_classification)
    for line in f:
        tokens = line.split(' ')
        classe = tokens[0]
        classification.append(classe)

    # calculatin the accuracy
    print "# len", len(answer), len(classification)
    acc = 0
    for i in xrange(len(answer)):
        if(int(answer[i]) == int(classification[i])):
            acc += 1
    print "# Acc", float(acc) / float(count)


if __name__ == '__main__':
    if len(argv) != 3:
        print "Usage: <test-file> <answer-file>"
        exit()

    result(argv[1], argv[2])
