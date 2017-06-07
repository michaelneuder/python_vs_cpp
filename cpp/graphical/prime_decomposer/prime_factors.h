#ifndef PRIME_FACTORS_H
#define PRIME_FACTORS_H
#include <vector>

class prime_factors{
    public:
        prime_factors();
        void decompose(long n);
        std::vector<int> get_factors();
    private:
        std::vector<int> factors;
};

#endif // PRIME_FACTORS_H
