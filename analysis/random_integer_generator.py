#!/usr/bin/env python3
import random

num_numbers = input("enter the number of random numbers to generate :")

with open("rand_ints.txt", mode='w') as WRITE_FILE:
    counter = 0
    while(counter < int(num_numbers)):
        WRITE_FILE.write(str(random.randint(2,1000000000)) + '\n')
        counter+=1
WRITE_FILE.close()
