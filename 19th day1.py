"""1.Create an Excel with data of Student database and add all the values which is required for student
 management database,Read the excel file and add the datas into a DB (using script)"""
import xlrd
import pandas as pd
df = pd.read_excel(r'C:\KETAN GURAV\Python\StudentData.xls')
print(df)
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="@mysqlketangurav22"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE Studentdata")
