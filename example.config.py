#! /usr/bin/python
DB_FILE = "pyRSS.db" #lokale sqlite file
UPLOAD_PATH  = "" #url an die die daten gesendet werden sollen
DEBUG = True #daten werden nicht gespeichert sondern nur ausgegeben
SEEDS = (
	{
		'root':"http://blog.fefe.de",
		'url':"http://blog.fefe.de/rss.xml",
		'pStart':"<language>de</language>",
		'pStop':"</channel>",
		'lStart:"<item>",
		'lStop':"</item>",
		'uStart:"<link>",
		'uStop':"</link>",
		'dStart':"",
		'dStop':"",
		'tStart':"<title>",
		'tStop':"</title>",
		'cat':"fefe"
	}
	"""
	,{
		'root':"",
		'url':"",
		'pStart':"",
		'pStop':"",
		'lStart:"",
		'lStop':"",
		'uStart:"",
		'uStop':"",
		'dStart':"",
		'dStop':"",
		'tStart':"",
		'tStop':"",
		'cat':""
	}
	"""
)
