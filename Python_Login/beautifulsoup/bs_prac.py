html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

head = {
	'Remote Address':'166.111.4.98:80',
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'Accept-Encoding':'gzip, deflate, sdch',
	'Accept-Language':'en-US,en;q=0.8',
	'Cache-Control':'max-age=0',
	'Connection':'keep-alive',
	'Host':'info.tsinghua.edu.cn',
	'Upgrade-Insecure-Request':'1',
	'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
}

from bs4 import BeautifulSoup
from urllib import request, parse
import http.cookiejar as cookielib

index_page = 'http://info.tsinghua.edu.cn/'

def get_form(index):
	page = BeautifulSoup(request.urlopen(index).read())
	inputs = [i for i in page.form.find_all('input') if i['type'] not in ['hidden','image']]
	info = {'dst':page.form['action']}
	for ipt in inputs:
		if 'value' in ipt:
			info[ipt['name']] = ipt['value']
		else:
			info[ipt['name']] = 0
	return info

def browser(user, password):
	info = get_form(index_page)
	cj = cookielib.CookieJar(cookielib.DefaultCookiePolicy())
	opener = request.build_opener(request.HTTPCookieProcessor(cj))
	opener.handle_open['http'][0].set_http_debuglevel(1)
	#opener.addheaders = [('User-agent','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')]
	dst = info.pop('dst')
	for tag in info:
		if 'u' in tag and not info[tag]:
			info[tag] = user
		if 'p' in tag and not info[tag]:
			info[tag] = password
	data = parse.urlencode(info).encode()
	dst = request.Request(dst, headers=head)
	resp = opener.open(dst, data)
	choice = request.Request('http://info.tsinghua.edu.cn/login_choice.jsp', headers=head)
	resp = opener.open(choice)
	page = BeautifulSoup(resp)
	info_url = page.find(text='进入门户').parent.parent['href']
	info_url = request.Request(index_page[:-1]+info_url, headers=head)
	resp = opener.open(info_url)
	page = BeautifulSoup(resp)
	logs = page.find(class_="log").find_all("span")
	logs = [i.text for i in logs]
	print(logs)
	iframes = page.find_all('iframe')
	for iframe in iframes:
		src = iframe['src']
		if src.startswith('http'):
			opener.open(src)
		else:
			opener.open(index_page[:-1]+src)
	score_url = page.find(text='全部成绩').parent['href']
	score_page = BeautifulSoup(opener.open(score_url, data))
	lines = score_page.find_all('tr')
	score = [0, 0]
	multi = [0, 0]
	for line in lines:
		cols = line.find_all('td')
		try:
			if '任选' in cols[7].text:
				s = cols[5].text.strip()
				if s in ['通过','优秀']:
					pass
				s = int(s)
				w = int(cols[3].text.strip())
				multi[1] += s * w
				score[1] += w
			else:
				s = cols[5].text.strip()
				if s in ['通过','优秀']:
					pass
				s = int(s)
				w = int(cols[3].text.strip())
				multi[0] += s * w
				score[0] += w
				multi[1] += s * w
				score[1] += w
		except:
			pass
	print(score)
	print(multi[0]/score[0])
	print(multi[1]/score[1])

browser('sunyt13', 'Plus1717')
browser('liujs13', 'a34aa424')
browser('xa13', 'xuan1215')