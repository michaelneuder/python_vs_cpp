#include <random>
#include <fstream>
#include "random_integer_generator.h"
using namespace std;

random_integer_generator::random_integer_generator(long n){
  num_to_generate = n;
  generate();
}

void random_integer_generator::generate(){
  ofstream out_file;
  out_file.open("rand_ints.txt");

  random_device rd;
  mt19937 gen(rd());
  uniform_int_distribution<> dis(1, 1000000000);

  for (int n=0; n<num_to_generate; ++n){
      out_file << dis(gen) << "\n";
  }
  out_file.close();
}
