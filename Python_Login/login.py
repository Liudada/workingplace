from urllib import request, parse
import http.cookiejar as cookielib
from hashlib import md5

def Browser(url, user, password):
	login_page = "http://net.tsinghua.edu.cn/do_login.php"
	cj = cookielib.CookieJar()
	opener = request.build_opener(request.HTTPCookieProcessor(cj))
	opener.addheaders = [('User-agent','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')]
	md = md5()
	md.update(password.encode())
	data = parse.urlencode({"action":"login","username":user,"password":"{MD5_HEX}"+md.hexdigest(),"ac_id":1})
	data = data.encode('utf8')
	opener.open(login_page, data)
	op = opener.open(url)
	data = op.read()
	return data

with open('res.html', 'wb') as res:
	res.write(Browser("http://www.baidu.com", "liujs13", "a34aa424"))