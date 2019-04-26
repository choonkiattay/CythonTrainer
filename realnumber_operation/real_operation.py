import random


class RandomNumber(object):

    def __init__(self, numbers):
        self.numbers = numbers
        print('Real Number Operation')

    def int_creator(self, ):
        result = []
        for i in range(self.numbers):
            element = random.randint(0, 9999)
            result.append(element)
        return result

    def float_creator(self, ):
        result = []
        for i in range(self.numbers):
            element = random.random()
            result.append(element)
        return result
