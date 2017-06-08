#!/usr/bin/env python3
from prime_factors import prime_factors
from random_integer_generator import generator
import numpy as np
import time

def main():
	input_number = np.arange(1,1001,1)
	decomp_data = []
	for i in input_number:
		print("---------------------------")
		print(i, "inputs")
		generator1 = generator(i)
		start_time = time.clock()
		prime1 = prime_factors()
		end_time = time.clock()
		print("decomposer finised in {} ms".format((end_time-start_time)*1000))
		decomp_data.append((end_time-start_time)*1000)
		print("---------------------------\n")

	with open("data/decomp_data.csv", 'w') as WRITE_FILE:
		WRITE_FILE.write('number of inputs, runtime (in ms)\n\n')
		for i in input_number:
			WRITE_FILE.write(str(i) + ", " + str(decomp_data[i-1]) + "\n")
	WRITE_FILE.close()

if __name__ == '__main__':
	main()
