# Quiz: Coding Softmax
# And now, your time to shine! Let's code the formula for the Softmax function in Python.

import numpy as np

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    denominator = 0
    numerator = np.exp(L)
    sum_of_exp = np.sum(numerator)
    result_Ans = []
    for i in range(len(L)):
        denominator +=  np.exp(L[i])
        math = numerator[i]*1.0/sum_of_exp
        result_Ans.append(math)
    return result_Ans

softmax([5,6,7])