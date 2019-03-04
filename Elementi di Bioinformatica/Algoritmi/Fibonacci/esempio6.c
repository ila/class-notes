#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>
#include <inttypes.h>

void fibo(uint32_t n) {
    if(n <= 1)
        printf("1\n");
    else if (n <= 2)
        printf("1 1\n");
    else {
        uint32_t prev = 1;
        uint32_t prev2 = 1;
        printf("1 1 ");
        for(uint32_t x = 3; x <= n; )
    }
}