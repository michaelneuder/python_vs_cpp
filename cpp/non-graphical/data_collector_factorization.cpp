#include <iostream>
#include <vector>
#include <cmath>
#include <fstream>
#include <random>
#include <ctime>
#include <string>
#include "prime_factors.h"
#include "random_integer_generator.h"
using namespace std;

int main(){
  int input_array[1000];
  for(int i=1; i<1001;i++){
    input_array[i-1] = i;
  }
  float decomp_data[1000];

  for(int i=1; i<1001; i++){
    cout << "---------------------------" << endl;
    cout << i << " inputs " << endl;
    random_integer_generator generator(i);
    clock_t start_time = clock();
    prime_factors prime_handler;
    clock_t end_time = clock();
    double time_run = double (end_time-start_time) / CLOCKS_PER_SEC * 1000;
    cout << "decomposer finished in " << time_run << " ms" << endl;
    decomp_data[i-1] = time_run;
    cout << "---------------------------" << endl;

    ofstream out_file;
    out_file.open("data/decomp_data.csv");
    if(!out_file.is_open()){
      cout << "file error" << endl;
      return 1;
    }
    out_file << "number of inputs, runtime of decomposer(in ms)\n\n";
    for(int i=0; i<1000; i++){
      out_file << i+1 << ", " << decomp_data[i] << "\n";
    }
    out_file.close();
  }
  return 0;
}
