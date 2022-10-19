#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math
import turtle as t
import time
from random import random


# TODO: Définissez vos fonction ici

def ellipsoide(a, b, c, p):
    volume = math.pi * a * b * c * 4.0/3
    mass = volume * p
    return volume, mass


def mostUsed(letterFrequencyDict):
    return list(zip(letterFrequencyDict.keys(),
                    letterFrequencyDict.values()))\
        .sort(key=lambda x: -x[1])[0][0]


class ADN:
    def __init__(self, sequence: str) -> None:
        self.sequence = sequence
        assert ADN.isValid(sequence)

    def howMuchOfSubSequence(self, subSequence):
        if not isinstance(subSequence, ADN):
            subSequence = ADN(subSequence)

        count = self.sequence.count(subSequence.sequence)
        return float(count) * len(subSequence.sequence) / len(self.sequence)


    @staticmethod
    def isValid(sequence: str):
        isValid = True
        for char in sequence:
            isValid &= char in ['a', 't', 'c', 'g']
        # What are those even called?, also pairings...

        return isValid

    @staticmethod
    def getInput():
        while True:
            try:
                adn = ADN(input("Enter ADN sequence: "))
                return adn
            except:
                pass


    @staticmethod
    def test():
        a = ADN.getInput()
        b = ADN.getInput()
        print(a.howMuchOfSubSequence(b))


def tree(norm=100, theta=90, deltaTheta = 25, pensize = 5):
    def nextNorm(): return (0.5 + abs(random() - 0.5)) * norm * 0.95

    if norm < 5:
        return

    t.pensize(pensize)
    t.pendown()
    t.setheading(theta)
    t.forward(norm)
    
    t1 = theta + deltaTheta
    t2 = theta - deltaTheta
    tree(nextNorm(), t1, deltaTheta, pensize*0.85)
    tree(nextNorm(), t2, deltaTheta, pensize*0.85)

    t.setheading(theta)
    t.backward(norm)
    



if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    assert ellipsoide(1, 1, 1, 1) == (4.0/3 * math.pi, 4.0/3 * math.pi)
    # ADN.test()

    t.colormode(255)
    t.color((0, 200, 200))
    t.pensize(3)
    t.speed(0)
    tree()
    time.sleep(2)