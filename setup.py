#! /usr/bin/python

import func

con = func.sql_connect('pyRSS.db')
print("Erstelle log tabelle")
func.sql(con,'''CREATE TABLE pages (
  pServer varchar(100) NOT NULL,
  pCategory varchar(100) NULL,
  path0 varchar(255) NOT NULL ,
  path1 varchar(255) NOT NULL ,
  path2 varchar(255) NOT NULL ,
  path3 varchar(255) NOT NULL ,
  pathNames varchar(100) NOT NULL DEFAULT 'URL',
  pNext timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  waitfor int(11) NULL DEFAULT 86400
)''')

func.sql_close(con)