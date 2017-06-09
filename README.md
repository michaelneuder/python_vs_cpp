# python_vs_cpp
a couple benchmarks to compare python and c++ runtimes. a detailed analysis and presentation of the results can be found in the ![jupyter notebook](https://github.com/michaelneuder/python_vs_cpp/blob/master/results.ipynb) in the main directory. i will include some graphs produced below for a quick glance a the results. the tl;dr version of the results is that python is about 50x slower when doing compututions. the pyqt graphics library, however, is only about 5x slower than the standard c++ version of qt.

---
### result overview

###### random number generation
![rng](https://github.com/michaelneuder/python_vs_cpp/blob/master/images/rng.png)

###### prime factorization
![rng](https://github.com/michaelneuder/python_vs_cpp/blob/master/images/factorization.png)

###### graphics - no computation
![rng](https://github.com/michaelneuder/python_vs_cpp/blob/master/images/g_nf.png)

###### graphics - computation
![rng](https://github.com/michaelneuder/python_vs_cpp/blob/master/images/g_fact.png)


###### graphical app (looks identical in python and c++)
![rng](https://github.com/michaelneuder/python_vs_cpp/blob/master/images/open.png)
![rng](https://github.com/michaelneuder/python_vs_cpp/blob/master/images/using_manual.png)
![rng](https://github.com/michaelneuder/python_vs_cpp/blob/master/images/opening_file.png)
![rng](https://github.com/michaelneuder/python_vs_cpp/blob/master/images/after_upload.png)

check out the notebook if you are interested. it explains everything.

-mike
