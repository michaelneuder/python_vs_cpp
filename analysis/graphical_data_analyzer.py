#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
	print('\nanalyzing runtime of pyqt vs qt in c++\n')
	python_data = pd.io.parsers.read_csv('../python/graphical/results_python.csv', names=['number of input','runtime'], header=1)
	cpp_data = pd.io.parsers.read_csv('../cpp/graphical/results_c++.csv', names=['number of input','runtime'], header=1)

	py_time_plot = np.asarray(python_data['runtime'], dtype=np.float64)
	cpp_time_plot = np.asarray(cpp_data['runtime'], dtype=np.float64)

	num_input_plot = np.asarray(python_data['number of input'], dtype=np.float64)

	plt.plot(num_input_plot, py_time_plot, 'g')
	plt.plot(num_input_plot, cpp_time_plot, 'r')
	plt.show()
	quotient =  np.asarray([py_time_plot[i]/cpp_time_plot[i] for i in range(len(py_time_plot))])
	print("pyqt is on average", quotient.mean(), "times slower than qt for c++.")

if __name__ == '__main__':
	main()
