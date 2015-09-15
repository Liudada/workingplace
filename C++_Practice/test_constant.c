#include "apue.h"
#include <limits.h>

int main (void) {
	printf("INT_MAX: %d\n", INT_MAX);
	printf("LONG_MAX: %ld\n", LONG_MAX);
	printf("LLONG_MAX: %lld\n", LLONG_MAX);
	printf("MB_LEN_MAX: %d\n", MB_LEN_MAX);
	printf("FOPEN_MAX: %d\n", FOPEN_MAX);
	printf("TMP_MAX: %d\n", TMP_MAX);

	exit(0);
}
