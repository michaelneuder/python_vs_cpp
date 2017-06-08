#include <iostream>
#include <vector>
#include <cmath>
#include <fstream>
#include <random>
#include <ctime>
#include <string>
#include "random_integer_generator.h"
using namespace std;

int main(){
  int input_array[1000];
  for(int i=1; i<1001;i++){
    input_array[i-1] = ((i-1)*500)+1;
    cout << input_array[i-1] << endl;
  }
  float rng_data[1000];

  for(int i=0; i<1000; i++){
    cout << "---------------------------" << endl;
    cout << input_array[i] << " inputs" << endl;
    clock_t start_time1 = clock();
    random_integer_generator generator1(input_array[i]);
    clock_t end_time1 = clock();
    double time_run1 = double (end_time1-start_time1) / CLOCKS_PER_SEC * 1000;
    cout << "generator finished in " << time_run1 << " ms" << endl;
    rng_data[i] = time_run1;
    cout << "---------------------------" << endl;

    ofstream out_file;
    out_file.open("data/rng_data.csv");
    if(!out_file.is_open()){
      cout << "file error" << endl;
      return 1;
    }
    out_file << "number of inputs, runtime(in ms)\n\n";
    for(int i=0; i<1000; i++){
      out_file << (500*i)+1  << ", " << rng_data[i] << "\n";
    }
    out_file.close();
  }
  return 0;
}
