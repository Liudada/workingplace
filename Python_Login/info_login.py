from urllib import request, parse
import http.cookiejar as cookielib
from hashlib import md5

def Browser(url, user, password):
	login_page = "https://learn.tsinghua.edu.cn/MultiLanguage/lesson/teacher/loginteacher.jsp"
	cj = cookielib.CookieJar()
	opener = request.build_opener(request.HTTPCookieProcessor(cj))
	opener.addheaders = [('User-agent','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')]
	data = parse.urlencode({"userid":user,"userpass":password})
	data = data.encode('utf8')
	opener.open(login_page, data)
	op = opener.open(url)
	data = op.read()
	return data

with open('res.html', 'wb') as res:
	res.write(Browser("http://learn.tsinghua.edu.cn/MultiLanguage/lesson/student/MyCourse.jsp?language=cn", "liujs13", "a34aa424"))