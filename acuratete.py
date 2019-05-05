# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 15:35:44 2019

@author: iuliu
"""

def main():
# prepare data
trainingSet=[]
testSet=[]
split = 0.67
loadDataset('C:/Users/Ada/Documents/GoogleDrive/cursuri/MIRF/labs/lab5/
iris.data.txt', split, trainingSet, testSet)
print('Train set: ' + repr(len(trainingSet)))
print('Test set: ' + repr(len(testSet)))
# generate predictions
predictions=[]
k = 3
for x in range(len(testSet)):
neighbors = getNeighbors(trainingSet, testSet[x], k)
result = getResponse(neighbors)
predictions.append(result)
print('> predicted=' + repr(result) + ', actual=' +
repr(testSet[x][-1]))
accuracy = getAccuracy(testSet, predictions)
print('Accuracy: ' + repr(accuracy) + '%')