import numpy

from keras.datasets import mnist
from matplotlib import pyplot

#loading
(train_X, train_y), (test_X, test_y) = mnist.load_data()

# _X contains the image itself, _y contains the digit represented by the digit
# we have 60,000 train data and 10,000 test data


""" #shape of dataset
print(train_X[0].size)
print('X_train: ' + str(train_X.shape))
print('Y_train: ' + str(train_y.shape))
print('X_test:  '  + str(test_X.shape))
print('Y_test:  '  + str(test_y.shape)) """


""" #plotting
from matplotlib import pyplot
for i in range(2):	
    pyplot.subplot(330 + 1 + i)
    pyplot.imshow(train_X[i], cmap=pyplot.get_cmap('gray'))
    print(train_y[i])
    pyplot.show() """
 