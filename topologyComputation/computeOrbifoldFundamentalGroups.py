from itertools import combinations, combinations_with_replacement
import math
from numpy import isclose


class SingularSet:
    '''
    For example: vector_representation = [NaN, NaN, NaN, NaN, 0, 0, 0, 0]
    '''
    def __init__(self, vector_representation):
        self.vector_representation = vector_representation

    def generate_example(self):
        ex = self.vector_representation[:]
        for k in range(len(ex)):
            if math.isnan(ex[k]):
                ex[k] = 0.01
        return ex

    def is_in_set(self, x):
        for k in range(len(x)):
            if not math.isnan(self.vector_representation[k]):
                if not isclose(x[k], self.vector_representation[k], atol=0.01, equal_nan=True):
                    # print('%s : %s' % (x[k], self.vector_representation[k]))
                    return False
        return True


class TorusTransformations:
    @staticmethod
    def alpha(x):
        return [
            -x[0], -x[1], -x[2], -x[3], x[4], x[5], x[6], x[7]
        ]

    @staticmethod
    def beta(x):
        return [
            x[0], x[1], x[2], x[3], -x[4], -x[5], -x[6], -x[7]
        ]

    @staticmethod
    def gamma(x):
        return [
            1./2-x[0], 1./2-x[1], x[2], x[3], 1./2-x[4], 1./2-x[5], x[6], x[7]
        ]

    @staticmethod
    def delta(x):
        return [
            -x[0], x[1], 1./2-x[2], x[3], -x[4], x[5], 1./2-x[6], x[7]
        ]

    @staticmethod
    def tau(i, x):
        y = x[:]
        y[i] = y[i]+1
        return y


if __name__ == '__main__':
    nan = float('nan')

    # Define the ninth singular set in T^8 according to the list in p.369, Lemma 14.2.2 in Joyce's book
    S9 = SingularSet([1./4, 1./4, nan, nan, 1./4, 1./4, nan, nan])


    maps = [
        'alpha(x)', 'beta(x)', 'gamma(x)', 'delta(x)', 'tau(0,x)', 'tau(1,x)', 'tau(2,x)',
        'tau(3,x)', 'tau(4,x)', 'tau(5,x)', 'tau(6,x)', 'tau(7,x)'
    ]
    print('Find all elements in Deck(T9) which can be written as the product of 3 or less of the maps %s.' % (maps))
    for k in range(4):
        print(k)
        for comb in combinations(maps, k):
            x = S9.generate_example()
            for func in comb:
                x = eval('TorusTransformations.' + func)
            if S9.is_in_set(x):
                print('%s: %s' % (comb, S9.is_in_set(x)))
