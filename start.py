#! /usr/bin/python

import config as c
import secret as s

# holt seite (str)
def getPage(url):
	

# seite beschneiden (str)
def findStart(page,start,stop):
	#TODO

# zerteilt page in lines (list)
def findLines(page,start,stop):
	#TODO

# extrahiert daten (str)
def findData(line,path,filter):
	#TODO

for i in c.SEEDS:
	page = getPage(i['url'])
	page = findStart(page,i['start'],i['stop'])
	lines = findLines(page,i['lStart'],['lStop'])
	for j in lines:
		url = findData(j,i['uPath'],i['uFilter'])
		data = findData(j,i['dPath'],i['dFilter'])
		title = findData(j,i['tPath'],i['tFilter'])
		if sendData(url,title,data):
			updateData(url,title,data)