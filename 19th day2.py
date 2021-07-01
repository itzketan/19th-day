import xlrd
import mysql.connector
book = xlrd.open_workbook('C:\KETAN GURAV\Python\StudentData.xls')
sheet = book.sheet_by_index(0)
mydb = mysql.connector.connect(host="localhost",user="root",password="@mysqlketangurav22",db="studentdata")
print(mydb)
dbase = mydb.cursor()

dbase.execute("SHOW DATABASES")
for i in dbase:
    print(i)
dbase.execute("CREATE TABLE Student6(Addmission_no VARCHAR(225),First_Name VARCHAR(20), Surname VARCHAR(20), DOB int(10), Gender VARCHAR(6) , Year int(3))")
dbase.execute("SHOW TABLES")
for table in dbase:
    print(table)
for row in range(1,sheet.utter_max_rows):
    sql = "INSERT INTO Student6(Addmission_no, First_Name, Surname, DOB, Gender, Year)VALUES (%s,%s,%s,%s,%s,%s)"
    for _ in range(0):
        Addmission_no = sheet.cell(row,0).value
        First_Name = sheet.cell(row,1).value
        Surname = sheet.cell(row,2).value
        DOB = sheet.cell(row,3).value
        Gender = sheet.cell(row,4).value
        Year = sheet.cell(row,5).value

        values = (Addmission_no, First_Name, Surname, DOB, Gender, Year)
        dbase.execute(sql, values)
mydb.commit()
dbase.execute("SELECT * FROM Student6")
database = dbase.fetchall()
for data in database:
    print(data)
mydb.close()