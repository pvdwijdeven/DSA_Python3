"""

https://www.codewars.com/kata/5a21bd361f7f7098e800000c/train/python

Hi there! Welcome to "Building an Adaboost model with Sklearn
(Introductory Machine Learning)".

If you get stuck at any point I strongly recommend you read the relevant
documentation: http://scikit-learn.org/stable/index.html

This kata can be broken up into the following steps:

Import the relevant sklearn libraries (i.e. AdaBoostClassifier, 
train_test_split)
Create the "train_ada_boost" function (more details below)
Split the data (X) into a test set and a training set (you MUST USE sklearns 
train_test_split for this)
TRAIN an adaBoostClassfier (Once again, you MUST USE sklearn for this).
Your "train_ada_boost" function must return a three element tuple (more 
details below).
The "train_ada_boost" function accepts the following arguments:

X -- This would normally be a dataset (but in this kata it is a 1D numpy array)
Target -- This is a 1D numpy array consisting of 1's and 0's. This argument 
is the set of values we are trying to predict with our model
estimators -- KEYWORD ARGUMENT if no argument is passed in the default value 
should be set to 3.
random_seed -- KEYWORD ARGUMENT if no argument is passed in the default value 
should be set to 0.
Your function should return a 3 element tuple consisting of the following 
values in this exact order:

A TRAINED AdaBoostClassifer (return the actual model)
A test set (1D numpy array, which was built by sklearns test_train_split 
function)
A target array (1D numpy array, which was built by sklearns test_train_split 
function))
Details:

Your model should be trained using the specified number of estimators, with a 
random state equal to seed.
When splitting the data, be sure to set the random state equal to seed.
ALL other parameters not mentioned here for both 'test_train_split' and 
'AdaBoost' should be set to default values.
Even though you are handling Numpy arrays there is no need to actually
manipulate the arrays yourself (let sklearn to it for you!).
"""

from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split


def train_ada_boost(X, target):
    (
        X_train,
        X_test,
        target_train,
        target_test,
    ) = train_test_split(X, target, random_state=0)

    model = AdaBoostClassifier(n_estimators=3, random_state=0)
    model.fit(X_train, target_train)

    return model, X_test, target_test


import codewars_test as test
import numpy as np


###################################################################################################################################################################
### Example Test Case
###################################################################################################################################################################
@test.describe("Example Test Case")
def example_test_case():
    X = np.zeros(10)
    target = np.ones(10)
    model, test_data, test_labels = train_ada_boost(X.reshape(-1, 1), target)
    test.it("model is correct type")(
        lambda: test.assert_equals(
            str(type(model)),
            "<class 'sklearn.ensemble._weight_boosting.AdaBoostClassifier'>",
        )
    )
    test.it("test data has correct length")(
        lambda: test.assert_equals(len(test_data), len(test_labels))
    )
    test.it("test data has correct type")(
        lambda: test.assert_equals(type(test_labels), type(test_data))
    )
    test.it("model works correctly")(
        lambda: test.assert_equals(
            model.predict([[X[0]]]), 1, "Hint: Have you fitted the model?"
        )
    )
