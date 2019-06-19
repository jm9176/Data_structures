'''
Creating the classifier to predict the digits as per the given input image.
The data used for the classifier is used from the following source and has
also been attached as a .rar format in this directory

https://www.kaggle.com/c/digit-recognizer/data

'''

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from time import time
from sklearn.tree import DecisionTreeClassifier

# Importing the digit dataset
data = pd.read_csv('train.csv').as_matrix()
clf = DecisionTreeClassifier()

# Total no. of samples in the inputs = 42000
print("Total no. of samples: ", len(data))

# training dataset = 35000 samples
featureTrain= data[0:35000,1:]
labelTrain = data[0:35000,0]

# Measuring the training time for the input training samples
# and fitting the model according to the input data
t_train = time()
clf.fit(featureTrain, labelTrain)
print("Training time: ", round(time()-t_train,3),"secs")

# testing dataset = 7000
featureTest = data[35000:,1:]
labelTest = data[35000:,0]

# Measuring the training time for the test samples
# and calculating the classifier score value
t_test = time()
score = clf.score(featureTest, labelTest)
print("Test time: ", round(time()-t_test,3),"secs")
print("Classifier accuracy: ", score)

# Viewing a sample
plt.figure()
test_sample = np.reshape(featureTest[10],(28,28))
print("Actual sample label: ", labelTest[10],"\nPredicted label: ", clf.predict([featureTest[10]]))
plt.imshow(255 - test_sample, cmap = 'gray')
plt.show()
