#! /usr/bin/python

from lxml import html
import requests

def scrappy(url,key=False):
	page = requests.get(url)
	tree = html.fromstring(page.content)
	
	# '//div[@title="buyer-name"]/text()'
	# '//span[@class="item-price"]/text()'
	# '//div//span//a//img/@alt'
	# '//div//span//a/@href'
	
	r = []
	
	for k in key:
		#print(k)
		r.append(tree.xpath(k))
	
scrappy("http://rule34.xxx/index.php?page=post&s=list&tags=living_clothes",['//div//span//a/@href','//div//span//a//img/@alt'])