import numpy as np
import random


class RandomMatrix(object):

    def __init__(self, numbers):
        self.numbers = numbers
        print('Matrix Operation')

    def int_creator(self, ):
        result = []
        for i in range(self.numbers):
            element = np.random.randint(random.randint(0, 9999), size=(random.randint(1, 9), random.randint(1, 9)))
            result.append(element)
        return result

    def float_creator(self, ):
        result = []
        for i in range(self.numbers):
            element = np.random.rand(random.randint(0, 9), random.randint(0, 9))
            result.append(element)
        return result
