#include "apue.h"
#include <errno.h>

int main (int argc, char *argv[])
{
	fprintf(stderr, "ENOENT: %s\n", strerror(ENOENT));
	errno = EACCES;
	perror(argv[0]);
	exit(0);
}
