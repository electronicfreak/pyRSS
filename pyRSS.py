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
		
def writeData(root,url, data):
		global lite
		
		url = f.no_inject(url)
		data = f.no_inject(data)
		
		if not url.startswith("http"):
			
		
		if not f.sql(lite,"SELECT * FROM ergebnisse WHERE `url` = '"+url+"'):
			f.sql(lite,"INSERT INTO ergebnisse (`url`,`data`) VALUES ('"+url+"','"+data+"')")
			return True
		return False
	
# holt anleitung aus db
def checkPages():
	#alle pages die in der vergangenheit liegen anzeigen
	for i in c.SEEDS:
		#print(i)
		a = scrappy(i["url"],i["search"])
		for b in range(a[0].len):
			writeData(i["root"],a[0][b],a[1][b])
	
#scrappy("http://rule34.xxx/index.php?page=post&s=list&tags=living_clothes",['//div//span//a/@href','//div//span//a//img/@alt'])
checkPages()

f.sql_close(sql)