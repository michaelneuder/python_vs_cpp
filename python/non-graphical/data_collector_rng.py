#!/usr/bin/env python3
from random_integer_generator import generator
import numpy as np
import time

def main():
	input_number = np.arange(1,500001,500)
	rng_data = []
	for i in input_number:
		print("---------------------------")
		print(i, "inputs")
		start_time = time.clock()
		generator1 = generator(i)
		end_time = time.clock()
		print("generator finished in {} ms".format((end_time-start_time)*1000))
		rng_data.append((end_time-start_time)*1000)
		print("---------------------------\n")

	with open("data/rng_data_mod.csv", 'w') as WRITE_FILE:
		WRITE_FILE.write('number of inputs, runtime (in ms)\n\n')
		for i in input_number:
			WRITE_FILE.write(str(i) + ", " + str(rng_data[int((i-1)/500)]) + "\n")
	WRITE_FILE.close()


if __name__ == '__main__':
	main()
