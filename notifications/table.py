from docxtpl import DocxTemplate
import datetime
import pymysql

mydb = pymysql.connect(
  host="localhost",
  user="root",
  passwd="1111",
  database="UTM5"
)

mycursor = mydb.cursor() 
res = 'SELECT full_name FROM users WHERE basic_account = 470'
mycursor.execute(res)
rows = mycursor.fetchall()

for row in rows:
   data = row

mydb.commit()
mydb.close()

doc = DocxTemplate("word.docx")
context = {'fam':data}
doc.render(context)
doc.save("generated_doc.docx")