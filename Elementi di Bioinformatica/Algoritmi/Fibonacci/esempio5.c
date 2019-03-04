#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>
#include <inttypes.h>

uint32_t fibo(uint32_t n) {
    if(n <= 2)
        return 1;
    else
        return fibo(n - 1) + fibo(n - 2);
}

int main(int argc, char const *argv[])
{
    uint32_t limit = atoi(argv[1]);;
    for(uint32_t n = 1; n <= limit; n++)
        print("%" PRIu32 " ", fibo(n));
    return 0;
}
