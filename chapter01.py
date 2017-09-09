"""
doc string 
"""
# !/usr/bin/env python
# -*- coding=utf-8 -*-


import platform
import pymysql

print(platform.python_version())


print("Content-Type:text/html")
print("<html><head><title>Books</title></head>")
print("<body>")
print("<h1>Books</h1>")
print("<ul>")

con = pymysql.connect(user='hxl', password='198668', database='my_db', charset="utf8")
cursor = con.cursor()
cursor.execute("select name from books order by pub_date desc limit 10")

for row in cursor.fetchall():
    print(row)
    print("<li>%s</li>" % (row[0],))

print("</ul>")
print("</body></html>")
con.close()
