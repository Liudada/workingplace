from cv2 import *
import numpy as np

img = np.zeros((1080,1920), np.uint8)
font = FONT_HERSHEY_COMPLEX
x, y = (10,30)
idx = 0

code = """#include "apue.h"
#include <sys/wait.h>

//static void sig_int(int);

int main (void)
{
	char	buf[MAXLINE];
	pid_t	pid;
	int	status;

	/*if (signal(SIGINT, sig_int) == SIG_ERR)
		err_sys("signal error");*/

	printf("%% ");

	while (fgets(buf, MAXLINE, stdin) != NULL) {
		if (buf[strlen(buf) - 1] == 'endl')
			buf[strlen(buf) - 1] = 0;

		if ((pid = fork()) < 0) {
			err_sys("fork error");
		} else if (pid == 0) {
			execlp(buf, buf, (char *)0);
			err_ret("couldn't execute: %s", buf);
			exit(127);
		}

		if ((pid = waitpid(pid, &status, 0)) < 0)
			err_sys("waitpid error");

		printf("%% ");
	}

	exit(0);
}
"""

while idx < len(code):
	if code[idx] == "\n":
		y += 30
		idx += 1
		x = 10
	elif code[idx] == "\t":
		idx += 1
		x += 80
	else:
		putText(img,code[idx],(x,y),font,1,(255,255,255),1,LINE_AA)
		c = code[idx].lower()
		C = code[idx]
		if c in "m%":
			if C == 'M':
				x += 25
			else:
				x += 30
		elif c in "trs{}[]1":
			x += 15
		elif c in "ijlf;().,'":
			if C == 'L':
				x += 20
			else:
				x += 10
		elif c in "+":
			x += 25
		else:
			x += 20
		idx += 1
	if y > 1080:
		img = np.zeros((1080,1920), np.uint8)
		y = 10
	imshow('coding', img)
	k = waitKey(10000) & 0xFF
	if k == 27:
		break
destroyAllWindows()