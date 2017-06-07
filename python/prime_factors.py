#!/usr/bin/env python3
from math import sqrt

class prime_factors(object):
    def __init__(self):
        self.factors = []
        self.run()

    def decompose(self, n):
        while(n%2 == 0):
            self.factors.append(2)
            n /= 2

        for i in range(3,int(sqrt(n))+1):
            while(n%i == 0):
                self.factors.append(i)
                n /= i

        if(n > 2):
            self.factors.append(int(n))

    def run(self):
        with open("rand_ints.txt", mode='r') as READ_FILE:
            for line in READ_FILE:
                self.decompose(int(line.strip()))
        READ_FILE.close()


def main():
	pass

if __name__=='__main__':
    main()
