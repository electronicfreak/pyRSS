#! /usr/bin/python

from lxml import html
import func as f
import config as c
import requests

lite = f.sql_connect(c.DB_FILE)
# durchsucht seite nach gewuenschten infos
#tested
def scrappy(url,key=False):
	page = requests.get(url)
	tree = html.fromstring(page.content)
	#print(page.content)
	#print(tree)
	r = []
	if key:
		for k in key:
			print(k)
			r.append(tree.xpath(k))
			
	return r
		
def updateSrv(url,data,cat):
	r = requests.post(c.UPLOAD_PATH, data={'url': url, 'data': data,'cat': cat})
	print(r.text)
	if r.text == "OK":
		return True
	return False

def writeData(root,url, data, cat):
		global lite
		
		url = f.no_inject(url)
		data = f.no_inject(data)
		cat = f.no_inject(cat)
		
		if not url.startswith("http"):
			url = root+"/"+url
		
		if not f.sql(lite,"SELECT * FROM ergebnisse WHERE `url` = '"+url+"'"):
			f.sql(lite,"INSERT INTO ergebnisse (`url`,`data`) VALUES ('"+url+"','"+data+"')")
			updateSrv(url,data,cat)
			return True
		return False
	
# holt anleitung aus db
def checkPages():
	#alle pages die in der vergangenheit liegen anzeigen
	for i in c.SEEDS:
		#print(i)
		a = scrappy(i["url"],i["search"])
		#print(a)
		for b in range(len(a[0])):	
			writeData(i["root"],a[0][b],a[1][b],i["cat"])
	
#scrappy("http://rule34.xxx/index.php?page=post&s=list&tags=living_clothes",['//div//span//a/@href','//div//span//a//img/@alt'])
checkPages()

#if updateSrv('1','2','2'):
#	print("OK")
#else:
#	print("ERR")