import numpy as np

trainingData = []
testingData = []

def loadData():
    global trainingData, testingData
    f = open('train.txt', 'r')
    trainingData = [(line.split()) for line in f]
    f = open ('test.txt', 'r')
    testingData = [(line.split()) for line in f]
    #print trainingData

def perceptron(dataset,w, P):
    for string in dataset:
        label = int(string[1])
        if(label*kernel(w, string, P) <= 0):
            w.append(string)
    return w

def kernel(w, TestString, P):
    sum = 0
    for string in w:
        attr = string[0]
        label = int(string[1])
        sum += label*commonString(TestString, string, P)
    return sum

def commonString(stringA, stringB, P):
    sum = 0
    for i in range(len(stringA[0])-P):
        if(stringA[0][i:i+P] in stringB[0]):
            sum+=1
    return sum

def err(w, testingData, P):
    count = 0
    for data in testingData:
        if kernel(w, data, P) > 0:
            label = 1
        else:
            label = -1
        if label != int(data[1]):
            count += 1
    return float(count)/len(testingData)


def main():
    loadData()
    w = []
    w = perceptron(trainingData, w, 3)
    print "Training error with P=3:", err(w, trainingData, 3)
    print "Testing error with P=3:", err(w, testingData, 3)

    w = perceptron(trainingData, w, 4)
    print "Training error with P=4:", err(w, trainingData, 4)
    print "Testing error with P=4:", err(w, testingData, 4)

    w = perceptron(trainingData, w, 5)
    print "Training error with P=5:", err(w, trainingData, 5)
    print "Testing error with P=5:", err(w, testingData, 5)


main()