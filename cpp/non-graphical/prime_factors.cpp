#include <iostream>
#include <math.h>
#include <vector>
#include <string>
#include <fstream>
#include "prime_factors.h"
using namespace std;

prime_factors::prime_factors(){
  run();
}

void prime_factors::decompose(long n){
  while(n%2 == 0){
      factors.push_back(2);
      n = n/2;
  }

  for(int i=3; i<sqrt(n); i++){
      while(n%i == 0){
          factors.push_back(i);
          n = n/i;
      }
  }

  if(n>2){
      factors.push_back(n);
  }
}

void prime_factors::run(){
  std::ifstream in_file;
  std::string line;
  in_file.open("rand_ints.txt");
  if(!in_file.is_open()){
    cout << "unable to open file" << endl;
    return;
  }
  while(getline(in_file, line)){
    long n = stol(line);
    decompose(n);
  }
  in_file.close();
}
