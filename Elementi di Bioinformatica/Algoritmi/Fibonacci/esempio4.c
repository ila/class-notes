#include <stdlib.h>
#include <stdio.h>
#include "esempio4.h"

int main(int argc, char const *argv[])
{
    unsigned int limit = atoi(argv[1]);
    for(unsigned int n = 1; n <= limit; n++)
        printf("%d ", fibo(n));
    return 0;
}

unsigned int fibo(unsigned int n) {
    if(n <= 2)
        return 1;
    else
        return fibo(n - 1) + fibo(n - 2);
}