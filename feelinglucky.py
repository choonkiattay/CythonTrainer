import argparse
from realnumber_operation import real_operation
from matrix_operation import matrix_operation


def init_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--numbers', type=int, help='Numbers of random to generate')
    parser.add_argument('--mode', type=str, help='realnumber or matrix')
    parser.add_argument('--type', type=str, help='int or float')

    return parser.parse_args()


def calculator(numbers, mode, type):

    if mode == 'realnumber':
        realnum_gen = real_operation.RandomNumber(numbers)
        if type == 'int':
            result = realnum_gen.int_creator()
        elif type == 'float':
            result = realnum_gen.float_creator()
    elif mode == 'matrix':
        matrix_gen = matrix_operation.RandomMatrix(numbers)
        if type == 'int':
            result = matrix_gen.int_creator()
        elif type == 'float':
            result = matrix_gen.float_creator()

    return result


if __name__ == '__main__':
    args = init_args()
    grand_result = calculator(numbers=args.numbers, mode=args.mode, type=args.type)
    print(grand_result)
