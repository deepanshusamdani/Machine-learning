#!/usr/bin/python3

import time
import tkinter
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
#loading iris datsets
iris=load_iris()
#print flower names
fl_name=iris.target_names

#print features of iris
fl_features=iris.feature_names
#loading flower features data
fl_feature_data=iris.data
#print(fl_feature_data)

#loading flower name data
fl_real_data=iris.target


setosa=iris.target[0:50]

train_setosa=setosa[0:49]
test_setosa=setosa[-1]


print (train_setosa)
print (test_setosa)


plt.xlabel('setosa')
plt.ylabel('versicolor')
plt.xlabel('IRIS FLOWER')
x1=fl_feature_data[0:50]
y1=fl_feature_data[0:50]
plt.scatter(x1,y1)
plt.show()
