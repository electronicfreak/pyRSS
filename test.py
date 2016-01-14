#! /usr/bin/python

import func as f

con = f.sql_connect('/root/lib/pyRSS/pyRSS.db')
print(f.sql(con,"SELECT * FROM ergebnisse"))
f.sql_close(con)
