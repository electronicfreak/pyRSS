#! /usr/bin/python
DB_FILE = "pyRSS.db" #lokale sqlite file
UPLOAD_PATH  = "http://rss.electronicfreak.de/update.php" #url an die die daten gesendet werden sollen
DEBUG = False #daten werden nicht gespeichert sondern nur ausgegeben
SEEDS = (
	{
		'root':"http://blog.fefe.de",
		'url':"http://blog.fefe.de/rss.xml",
		'pStart':"<language>de</language>",
		'pStop':"</channel>",
		'lStart':"<item>",
		'lStop':"</item>",
		'uStart':"<link>",
		'uStop':"</link>",
		'dStart':"",
		'dStop':"",
		'tStart':"<title>",
		'tStop':"</title>",
		'cat':"fefe"
	}	,{
		'root':"http://wiki.hackerspace-bi",
		'url':"http://wiki.hackerspace.bi/api.php?hidebots=1&days=7&limit=50&action=feedrecentchanges&feedformat=atom",
		'pStart':"</generator>",
		'pStop':"</feed>",
		'lStart':"<entry>",
		'lStop':"</entry>",
		'uStart':"<id>",
		'uStop':"</id>",
		'dStart':"",
		'dStop':"",
		'tStart':"<title>",
		'tStop':"</title>",
		'cat':"hsb"
	}	,{
		'root': "http://rule34.xxx",
		'url': "http://rule34.xxx/index.php?page=post&s=list&tags=living_clothes",
		'pStart':'<div><span',
		'pStop':'<div id="paginator">',
		'lStart':"<a",
		'lStop':"</a></span>",
		'uStart':'href="',
		'uStop':'" >',
		'dStart':'',
		'dStop':'',
		'tStart':'',
		'tStop':'',
		'cat':"h"
	}
)
"""
	,{
		'root':"",
		'url':"",
		'pStart':"",
		'pStop':"",
		'lStart':"",
		'lStop':"",
		'uStart':"",
		'uStop':"",
		'dStart':"",
		'dStop':"",
		'tStart':"",
		'tStop':"",
		'cat':""
	}
"""
