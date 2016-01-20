#! /usr/bin/python

import config as c
import requests
import func as f

lite = f.sql_connect(c.DB_FILE)

# holt seite (str)
#untestet
def getPage(url):
	page = requests.get(url,verify=False)
	return page.content

# seite beschneiden (str)
#untestet
def findStart(page,start,stop):
	start = page.find(start) + len(start)
	stop = page.find(stop)
	return page[start:stop]

# zerteilt page in lines (list)
#untestet
def findLines(page,start,stop):
	loop = True
	lines = []
	while loop:
		t1 = page.find(start) + len(start)
		if t1 >= 0:
			stop = str(stop)
			t2 = page.find(stop,t1)
			if t2 >= 0:
				line = page[t1:t2]
				lines.append(line)
				page = page[t2:]
			else:
				loop = False
		else:
			loop = False
	return lines

# extrahiert daten (str)
def findData(line,start,stop):
	if not(start == "" or stop == ""):
		start = line.find(start) + len(start)
		stop = line.find(stop)
		return line[start:stop]
	else:
		return ""

def sendData(url, data, title, cat):
	global lite
	
	url = f.no_inject(url)
	data = f.no_inject(data)
	title = f.no_inject(title)
	cat = f.no_inject(cat)

	url = url.replace("&amp;","&")

	if c.DEBUG:
		print(len(f.sql(lite,"SELECT * FROM ergebnisse WHERE `url` = '"+url+"'")))
		print("INSERT INTO ergebnisse (url) VALUES ('"+url+"')")
		return True
	else:
		if len(f.sql(lite,"SELECT * FROM ergebnisse WHERE `url` = '"+url+"'")) <= 0:
			f.sql(lite,"INSERT INTO ergebnisse (`url`) VALUES ('"+url+"')")
			return True
		return False
		
def updateData(url,data,title,cat):
	if c.DEBUG:
	    return True
	else:
		r = requests.post(c.UPLOAD_PATH, data={'url': url, 'data': data,'title':title,'cat': cat})
		if r.text == "OK":
			return True
		return False
	
def doStuff(i):
	page = getPage(i['url'])
	page = findStart(page,i['pStart'],i['pStop'])
	if c.DEBUG:
		print(page)
		print("----------------------------------------------------------------------")
	lines = findLines(page,i['lStart'],i['lStop'])
	if c.DEBUG:
		print(lines)
		print("-----------------------------------------------------------------------")

	for j in lines:
		url = findData(j,i['uStart'],i['uStop'])
		data = findData(j,i['dStart'],i['dStop'])
		title = findData(j,i['tStart'],i['tStop'])

		if not url.startswith("http"):
		    url = i['root'] +"/"+ url

		if sendData(url,data,title,i['cat']):
			updateData(url,data,title,i['cat'])

if type(c.SEEDS) == dict:
	doStuff(c.SEEDS)
else:
	for i in c.SEEDS:
		doStuff(i)
	
