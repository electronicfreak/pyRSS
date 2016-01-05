#! /usr/bin/python

from lxml import html
import func as f
import config as c
import requests

# durchsucht seite nach gewünschten infos
def scrappy(url,key=False):
	page = requests.get(url)
	tree = html.fromstring(page.content)
	
	r = []
	if key:
		for k in key:
			#print(k)
			r.append(tree.xpath(k))
		
# holt anleitung aus db
def checkPages():
	sql = f.sql_connect(c.DB_FILE)
	
	
	
scrappy("http://rule34.xxx/index.php?page=post&s=list&tags=living_clothes",['//div//span//a/@href','//div//span//a//img/@alt'])