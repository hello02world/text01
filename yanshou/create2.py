#!/usr/bin/env python

import MySQLdb

db = MySQLdb.connect("172.17.0.2", "root", "123456", "phone", charset='utf8' )

cursor = db.cursor()

sql = """CREATE TABLE mi(
         url char(200),
         namevc char(200),
         price float(7,2))"""

cursor.execute(sql)

db.close()
