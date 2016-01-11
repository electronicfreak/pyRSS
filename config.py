#! /usr/bin/python
DB_FILE = "pyRSS.db"
UPLOAD_PATH  = "http://rss.electronicfreak.de/update.php"

SEEDS = (
	{'root':"http://rule34.xxx",'url':"http://rule34.xxx//index.php?page=post&s=list&tags=living_clothes",'search':('//div//span//a/@href','//div//span//a//img/@alt'),'cat':"h"},
	{'root':"http://blog.fefe.de",'url':"http://blog.fefe.de/rss.xml",'search':('//item//link/text()','//item//title/text()'),'cat':"fefe"}
)
