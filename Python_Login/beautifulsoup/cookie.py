import os
if "HTTP_COOKIE" in os.environ:
	print(os.environ['HTTP_COOKIE'])
else:
	print('not set')