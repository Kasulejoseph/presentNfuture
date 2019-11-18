# Quiz: Coding Cross-entropy
# Now, time to shine! Let's code the formula for cross-entropy in Python.

import numpy as np

# Write a function that takes as input two lists Y, P,
# and returns the float corresponding to their cross-entropy.
def cross_entropy(Y, P):
    prob_truth = 0
    prob_falsy = 0
    for key, i in enumerate(Y):
        if(i == 1):
            prob_truth += np.log(P[key])
        elif(i == 0):
            prob_falsy += np.log(1-P[key])
    cross_entropy = -(prob_truth + prob_falsy)
    return cross_entropy

cross_entropy([1,0,1,1], [0.4,0.6,0.1,0.5])


# solution.py
"""
def cross_entropy(Y, P):
    Y = np.float_(Y)
    P = np.float_(P)
    return -np.sum(Y * np.log(P) + (1 - Y) * np.log(1 - P))
"""