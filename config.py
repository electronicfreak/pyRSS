#! /usr/bin/python
DB_FILE = "pyRSS.db"
UPLOAD_PATH  = "http://rss.electronicfreak.de/input.php"

SEEDS = (
	{'root':"http://rule34.xxx/",'url':"http://rss.electronicfreak.de/test.html",'search':('//div//span//a/@href','//div//span//a//img/@alt','cat':"test")},
	{'root':"http://rule34.xxx/",'url':"http://rss.electronicfreak.de/test.html",'search':('//div//span//a/@href','//div//span//a//img/@alt','cat':"h")}
)
