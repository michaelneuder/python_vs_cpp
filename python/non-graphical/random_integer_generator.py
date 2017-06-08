#!/usr/bin/env python3
import random

class generator(object):
	def __init__(self, number):
		self.num_numbers = number
		self.generate()

	def generate(self):
		with open("rand_ints.txt", mode='w') as WRITE_FILE:
		    counter = 0
		    while(counter < self.num_numbers):
		        WRITE_FILE.write(str(random.randint(2,1000000000)) + '\n')
		        counter+=1
		WRITE_FILE.close()
