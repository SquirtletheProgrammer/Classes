'''
/* THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING CODE
WRITTEN BY OTHER STUDENTS.
Dillon Wu */
'''

import argparse
import numpy as np
import pandas as pd
import sklearn as sk

import knn


def standard_scale(xTrain, xTest):
    """
    Preprocess the training data to have zero mean and unit variance.
    The same transformation should be used on the test data. For example,
    if the mean and std deviation of feature 1 is 2 and 1.5, then each
    value of feature 1 in the test set is standardized using (x-2)/1.5.

    Parameters
    ----------
    xTrain : nd-array with shape n x d
        Training data 
    xTest : nd-array with shape m x d
        Test data 

    Returns
    -------
    xTrain : nd-array with shape n x d
        Transformed training data with mean 0 and unit variance 
    xTest : nd-array with shape m x d
        Transformed test data using same process as training.
    """
    # TODO FILL IN

    #calculating the mean and standard deviation
    #standard deviation for each column
    std = []
    #mean for each column
    mean = []
    for i in xTrain.columns:
        std.append( xTrain[i].std())
        mean.append (xTrain[i].mean())

    #normalize xTrain
    counter = 0
    for i in xTrain.columns:
        for j in range(0, len(xTrain[i])):
            xTrain[i][j] = (xTrain[i][j] - mean[counter]) / std[counter]
        counter+=1

    #normalize xTest
    stdTest=[]
    meanTest=[]
    counter = 0
    for i in xTest.columns:
        stdTest.append( xTest[i].std())
        meanTest.append (xTest[i].mean())

    for i in xTest.columns:
        for j in range(0, len(xTest[i])):
            xTest[i][j] = (xTest[i][j] - meanTest[counter]) / stdTest[counter]
        counter+=1

    return xTrain, xTest


def minmax_range(xTrain, xTest):
    """
    Preprocess the data to have minimum value of 0 and maximum
    value of 1.T he same transformation should be used on the test data.
    For example, if the minimum and maximum of feature 1 is 0.5 and 2, then
    then feature 1 of test data is calculated as:
    (1 / (2 - 0.5)) * x - 0.5 * (1 / (2 - 0.5))

    Parameters
    ----------
    xTrain : nd-array with shape n x d
        Training data 
    xTest : nd-array with shape m x d
        Test data 

    Returns
    -------
    xTrain : nd-array with shape n x d
        Transformed training data with min 0 and max 1.
    xTest : nd-array with shape m x d
        Transformed test data using same process as training.
    """
    # TODO FILL IN

    #Finding the min and max of xTrain
    minimum = []
    maximum = []
    for i in xTrain.columns:
        minimum.append( xTrain[i].min())
        maximum.append( xTrain[i].max())

    #normalizing for xTrain
    counter = 0
    for i in xTrain.columns:
        for j in range(0, len(xTrain [i])):
            xTrain[i][j] = (xTrain[i][j] - minimum[counter]) / (maximum[counter] - minimum[counter])
        counter+=1

    #Finding the min and max of xTest
    minimum = []
    maximum = []
    for i in xTest.columns:
        minimum.append( xTest[i].min())
        maximum.append( xTest[i].max())

    #normalizing for xTest
    counter = 0
    for i in xTest.columns:
        for j in range(0, len(xTest [i])):
            xTest[i][j] = (xTest[i][j] - minimum[counter]) / (maximum[counter] - minimum[counter])
        counter+=1

    return xTrain, xTest


def add_irr_feature(xTrain, xTest):
    """
    Add 2 features using Gaussian distribution with 0 mean,
    standard deviation of 1.

    Parameters
    ----------
    xTrain : nd-array with shape n x d
        Training data 
    xTest : nd-array with shape m x d
        Test data 

    Returns
    -------
    xTrain : nd-array with shape n x (d+2)
        Training data with 2 new noisy Gaussian features
    xTest : nd-array with shape m x (d+2)
        Test data with 2 new noisy Gaussian features
    """
    # TODO FILL IN
    csize = xTrain.columns[0]
    irrelevant1=[]
    irrelevant2=[]
    for i in range (0, len(xTrain[csize])):
        irrelevant1.append(np.random.normal(0,1))
        irrelevant2.append(np.random.normal(0,1))
    xTrain["irrelevant1"] = irrelevant1
    xTrain["irrelevant2"] = irrelevant2
    
    ctsize = xTest.columns[0]
    irrelevant1=[]
    irrelevant2=[]
    for i in range (0, len(xTest[ctsize])):
        irrelevant1.append(np.random.normal(0,1))
        irrelevant2.append(np.random.normal(0,1))
    
    xTest["irrelevant1"] = irrelevant1
    xTest["irrelevant2"] = irrelevant2

    return xTrain, xTest


def knn_train_test(k, xTrain, yTrain, xTest, yTest):
    """
    Given a specified k, train the knn model and predict
    the labels of the test data. Returns the accuracy of
    the resulting model.

    Parameters
    ----------
    k : int
        The number of neighbors
    xTrain : nd-array with shape n x d
        Training data 
    yTrain : 1d array with shape n
        Array of labels associated with training data.
    xTest : nd-array with shape m x d
        Test data 
    yTest : 1d array with shape m
        Array of labels associated with test data.

    Returns
    -------
    acc : float
        The accuracy of the trained knn model on the test data
    """
    
    model = knn.Knn(k)
    model.train(xTrain, yTrain['label'])
    # predict the test dataset
    yHatTest = model.predict(xTest)
    return knn.accuracy(yHatTest, yTest['label'])

    

def main():
    # set up the program to take in arguments from the command line
    parser = argparse.ArgumentParser()
    parser.add_argument("k",
                        type=int,
                        help="the number of neighbors")
    parser.add_argument("--xTrain",
                        default="q4xTrain.csv",
                        help="filename for features of the training data")
    parser.add_argument("--yTrain",
                        default="q4yTrain.csv",
                        help="filename for labels associated with training data")
    parser.add_argument("--xTest",
                        default="q4xTest.csv",
                        help="filename for features of the test data")
    parser.add_argument("--yTest",
                        default="q4yTest.csv",
                        help="filename for labels associated with the test data")

    args = parser.parse_args()
    # load the train and test data
    xTrain = pd.read_csv(args.xTrain)
    yTrain = pd.read_csv(args.yTrain)
    xTest = pd.read_csv(args.xTest)
    yTest = pd.read_csv(args.yTest)

    # no preprocessing
    acc1 = knn_train_test(args.k, xTrain, yTrain, xTest, yTest)
    print("Test Acc (no-preprocessing):", acc1)
    # preprocess the data using standardization scaling
    xTrainStd, xTestStd = standard_scale(xTrain, xTest)
    acc2 = knn_train_test(args.k, xTrainStd, yTrain, xTestStd, yTest)
    print("Test Acc (standard scale):", acc2)
    # preprocess the data using min max scaling
    xTrainMM, xTestMM = minmax_range(xTrain, xTest)
    acc3 = knn_train_test(args.k, xTrainMM, yTrain, xTestMM, yTest)
    print("Test Acc (min max scale):", acc3)
    # add irrelevant features
    xTrainIrr, yTrainIrr = add_irr_feature(xTrain, xTest)
    acc4 = knn_train_test(args.k, xTrainIrr, yTrain, yTrainIrr, yTest)
    print("Test Acc (with irrelevant feature):", acc4)

if __name__ == "__main__":
    main()
