#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
	print('\nanalyzing runtime of pyqt vs qt in c++\n')
	python_data = pd.io.parsers.read_csv('../python/graphical/results_python_nf.csv', names=['number of input','runtime'], header=1)
	cpp_data = pd.io.parsers.read_csv('../cpp/graphical/results_c++_nf.csv', names=['number of input','runtime'], header=1)

	py_time_plot = np.asarray(python_data['runtime'], dtype=np.float64)
	cpp_time_plot = np.asarray(cpp_data['runtime'], dtype=np.float64)

	py_x_plot = np.asarray(python_data['number of input'], dtype=np.float64)
	cpp_x_plot = np.asarray(cpp_data['number of input'], dtype=np.float64)

	plt.plot(py_x_plot, py_time_plot, 'g', label='python')
	plt.plot(cpp_x_plot, cpp_time_plot, 'r', label='cpp')
	plt.title("graphical, no-factorization")
	plt.xlabel("number of input")
	plt.ylabel("runtime (ms)")
	plt.legend(loc=2)
	plt.show()
	quotient =  np.asarray([py_time_plot[i]/cpp_time_plot[i] for i in range(len(py_time_plot))])
	print("pyqt is on average {} times slower than qt for c++.".format(quotient.mean()))

if __name__ == '__main__':
	main()
