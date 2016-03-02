import numpy as np

trainingData = []

def loadData():
    global testingDataA
    f = open('hw5train.txt', 'r')
    trainingData = [(line.split()) for line in f]
    print trainingData

def perceptron(dataset,w, P):
    for string in dataset:
        label = string[1]
        print label
        if(label*kernel(w, string, P) <= 0):
            w.append(string)
            print string
    return w

def kernel(w, TestString, P):
    sum = 0
    for string in w:
        attr = string[0]
        label = string[1]
        sum += label*commonString(TestString, string, P)
    return sum

def commonString(stringA, stringB, P):
    sum = 0
    for i in range(len(stringA)-P):
        if(stringB.find(stringA[i:i+P]) >0):
            sum+=1
    return sum

def main():
    loadData()
    w = []
    w = perceptron(trainingData, w, 3)
    print w

main()