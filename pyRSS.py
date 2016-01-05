#! /usr/bin/python

from lxml import html
import requests

def scrappy(url,key=""):
	page = requests.get(url)
	print(page.content)
	tree = html.fromstring(page.content)
	print("--------------------------------------------")
	print(tree)
	
scrappy("http://192.168.1.1")