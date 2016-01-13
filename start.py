#! /usr/bin/python

import config as c
import secret as s
import requsts


# holt seite (str)
#untestet
def getPage(url):
	page = requests.get(url)
	return page.content

# seite beschneiden (str)
#untestet
def findStart(page,start,stop):
	start = page.find(start) + start.len()
	stop = page.find(stop)
	return page[start:stop]

# zerteilt page in lines (list)
#untestet
def findLines(page,start,stop):
	loop = True
	lines = []
	while loop:
		t1 = page.find(start) + start.len()
		if t1 >= 0:
			t2 = page.find(stop)
			if t2 >= 0:
				lines.append(page[t1:t2])
				page = page[t2:]
			else:
				loop = False
		else:
			loop = False
			
		return lines

# extrahiert daten (str)
def findData(line,start,stop):
	start = line.find(start) + start.len()
	stop = line.find(stop)
	return line[start:stop]

for i in c.SEEDS:
	page = getPage(i['url'])
	page = findStart(page,i['start'],i['stop'])
	lines = findLines(page,i['lStart'],['lStop'])
	for j in lines:
		url = findData(j,i['uStart'],i['uStop'])
		data = findData(j,i['dStart'],i['dStop'])
		title = findData(j,i['tStart'],i['tStop'])
		#if sendData(url,title,data):
		#	updateData(url,title,data)