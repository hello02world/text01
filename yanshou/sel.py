#!/usr/bin/env python

import MySQLdb

db = MySQLdb.connect("172.17.0.2", "root", "123456", "phone", charset='utf8' )

cursor = db.cursor()

sql = """select max(price),min(price),avg(price),count(price) from huawei;"""

cursor.execute(sql)
data = cursor.fetchall()
cursor.close()
db.close()

for row in data:
  print """<min,max,avg,num>"""
  print row
