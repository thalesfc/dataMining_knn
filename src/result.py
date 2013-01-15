from sys import argv

if len(argv) != 3:
    print "Usage: <test-file> <answer-file>"
    exit()

# loading the answers
answer = []
count = 0
f = open(argv[1])
for line in f:
    tokens = line.split(' ')
    classe = tokens[0]
    answer.append(classe)
    count += 1

# loading the classification
classification = []
f = open(argv[2])
for line in f:
    tokens = line.split(' ')
    classe = tokens[0]
    classification.append(classe)


# calculatin the accuracy
acc = 0
for i in xrange(len(answer)):
    if(int(answer[i]) == int(classification[i])):
        acc += 1
print "# Acc", float(acc) / float(count)
