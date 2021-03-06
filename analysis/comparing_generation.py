#!/usr/bin/env python3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    print('\ncomparing runtime of python and c++ with random number generation\n')
    python_data = pd.io.parsers.read_csv('../python/non-graphical/data/rng_data.csv', names=['number of input', 'runtime'], header=1)
    cpp_data = pd.io.parsers.read_csv('../cpp/non-graphical/data/rng_data.csv', names=['number of input', 'runtime'], header=1)

    python_plot = np.asarray(python_data['runtime'], dtype=np.float64)
    cpp_plot = np.asarray(cpp_data['runtime'], dtype=np.float64)

    x_plot_python = np.asarray(python_data['number of input'], dtype=np.float64)
    x_plot_cpp = np.asarray(cpp_data['number of input'], dtype=np.float64)
    plt.title("random number generation")
    plt.xlabel("number of input")
    plt.ylabel("runtime (ms)")
    plt.plot(x_plot_python, python_plot, 'g', label='python')
    plt.plot(x_plot_cpp, cpp_plot, 'r', label='cpp')
    plt.legend()
    plt.show()

    quotient = np.asarray([python_plot[i]/cpp_plot[i] for i in range(len(python_plot))])
    print("python is on average {} times slower than cpp".format(quotient.mean()))

if __name__ == '__main__':
    main()
