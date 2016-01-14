#! /usr/bin/python

import func
import config

con = func.sql_connect(config.DB_FILE)
print("Erstelle ergebnis tabelle")
func.sql(con,'''CREATE TABLE ergebnisse (
  url varchar(255) NOT NULL,
  created timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
)''')

func.sql_close(con)
