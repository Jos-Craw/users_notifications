import pymysql
from pymysql.constants import CLIENT

mydb = pymysql.connect(
  host="localhost",
  user="root",
  passwd="1111",
  database='UTM5',
  client_flag=CLIENT.MULTI_STATEMENTS)


mycursor = mydb.cursor() 
x = '\n'.join(open('SS.sql', 'r', encoding='UTF8').readlines())
mycursor.execute(x)
