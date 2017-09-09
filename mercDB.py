import mysql.connector
from mysql.connector import errorcode

def MercSQL():
 cnx = mysql.connector.connect (user='', password='',
 host='', database='')
 cursor = cnx.cursor()


 sql = """LOAD DATA LOCAL INFILE 'titles.txt' INTO TABLE `Products` (title)"""

 cursor.execute(sql)
 print(cursor)

 cnx.commit()
		

 cnx.close()


 print(sql)
