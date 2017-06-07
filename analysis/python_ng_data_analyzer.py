#!/usr/bin/env python3
import csv
import numpy as np
import matplotlib.pyplot as plt

def main():
    rng_data = []
    decomp_data = []
    with open('../python/non-graphical/data/rng_data.csv', mode='r') as READ_FILE:
        reader = csv.reader(READ_FILE)
        for line in reader:
            rng_data.append(float(line[1]))
    READ_FILE.close()
    with open('../python/non-graphical/data/decomp_data.csv', mode='r') as READ_FILE:
       reader = csv.reader(READ_FILE)
       for line in reader:
           decomp_data.append(float(line[1]))
    READ_FILE.close()

    x_plot = np.arange(1,1001)
    plt.plot(x_plot, rng_data, 'g')
    plt.show()
    plt.clf()
    plt.plot(x_plot, decomp_data, 'g')
    plt.show()


if __name__ == '__main__':
    main()
