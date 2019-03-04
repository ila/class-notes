// implementazione della sequenza di Fibonacci in C

/**
	@file fibc.c
	@brief Compute the first \c n Fibonacci numbers
	*/

#include <stdlib.h>
#include <stdio.h>
#include "fibc.h"
#include <inttypes.h>

uint32_t fib(uint32_t x) {
	if (x <= 2)
		return 1;
	else
		return fib(x - 1) + fib(x - 2);
}

int main(int argc, char **argv) {
	uint32_t limit = atoi(argv[1]);
	for (uint32_t n = 1; n <= limit; n++)
		printf("%" PRIu32 " ", fib(n));

	printf("\n");

}


