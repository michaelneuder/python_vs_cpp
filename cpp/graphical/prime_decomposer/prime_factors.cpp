#include "prime_factors.h"
#include <stdio.h>
#include <math.h>
#include <vector>
using namespace std;

prime_factors::prime_factors(){

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

vector<int> prime_factors::get_factors(){
    return factors;
}
