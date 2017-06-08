#ifndef PRIME_FACTORS_H
#define PRIME_FACTORS_H
#include <vector>

class prime_factors{
    public:
        prime_factors();
        void decompose(long n);
        std::vector<int> factors;
        void run();
};

#endif // PRIME_FACTORS_H
