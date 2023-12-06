# Author: Clinton Daniel, University of South Florida
# Date: 4/4/2023
# Description: This python script assumes that you already have
# a database.db file at the root of your workspace.
# This python script will CREATE a table called students 
# in the database.db using SQLite3 which will be used
# to store the data collected by the forms in this app
# Execute this python script before testing or editing this app code. 
# Open a python terminal and execute this script:
# python create_table.py

import sqlite3
import os

conn = sqlite3.connect('database.db')
print("Connected to database successfully")
cursor = conn.cursor()

# conn.execute('CREATE TABLE students (S_ID INT, S_Name VARCHAR(255), Section VARCHAR(255), Email VARCHAR(255), Password VARCHAR(255))')
# conn.execute('CREATE TABLE teacher (T_ID INT, T_Name VARCHAR(255), C_ID INT, Email VARCHAR(255), Password VARCHAR(255))')
# conn.execute('CREATE TABLE course (C_ID INT, C_Name VARCHAR(255))')
# conn.execute('CREATE TABLE project (Proposal BLOB, report BLOB, Code BLOB,  INT)')
# conn.execute('CREATE TABLE submission (Submission_ID INT, C_ID INT, Project_NameSubmission_ID TEXT, Submission_Date TEXT, T_ID INT, S_ID INT )')
# print("Created table successfully!")

#__________________________________________INSERT_FUNCTIONS_________________________________

def insert_student(S_ID,S_Name,section,email,password):
    conn.execute("INSERT INTO students (S_ID,S_Name,Section,Email,Password) VALUES (?,?,?,?,?)", (S_ID,S_Name,section,email,password))

def insert_teacher(T_ID,T_Name,C_ID,email,password):
    conn.execute("INSERT INTO teacher (T_ID,T_Name,C_ID,Email,Password) VALUES (?,?,?,?,?)", (T_ID,T_Name,C_ID,email,password))

def insert_course(C_ID,C_Name):
    conn.execute("INSERT INTO course (C_ID,C_Name) VALUES (?,?)", (C_ID,C_Name))

insert_course(123,456)

#__________________________________________RETRIEVE_FUNCTION__________________________________

statement = '''SELECT * FROM students''' 
cursor.execute(statement) 
print("All the data") 
output = cursor.fetchall() 
for row in output: 
  print(row) 

#_____________________________________INSERT_FILE_IN_DB___________________________________________

def convert(file):
    filename = file
    with open(filename, "rb") as file:
        ablob = file.read()
    return ablob

def input_file(proposal,report,code,sub_ID,S_ID,C_ID,T_ID,sub_Date):
    p_file = convert(proposal)
    r_file = convert(report)
    c_file = convert(code)
    cursor.execute("INSERT INTO project (Proposal,report,Code,Submission_ID,S_ID,C_ID,T_ID,Submission_Date) VALUES(?,?,?,?,?,?,?,?)", (p_file,r_file,c_file,sub_ID,S_ID,C_ID,T_ID,sub_Date))

proposal = "C:/Users/usman/OneDrive/Desktop/demo2/file1.txt"
report = "C:/Users/usman/OneDrive/Desktop/demo2/file1.txt"
code = "C:/Users/usman/Downloads/Question 1 .pdf"
submission_id = 6 ; S_ID = 23 ; c_ID = 2 ; T_ID = 2 ; 
submission_date = "6-12-23" 

input_file(proposal,report,code,submission_id,S_ID,c_ID,T_ID,submission_date)

# #_____________________________________UPDATE_PASSWORD_STUDENT_______________________________

def update_password_student(email,password,new_password):
    cursor.execute("Update students SET  password = ? WHERE email = ? AND password = ? ", (new_password,email,password))
email = "k214890@nu.edu.pk"
password = "abc123"
new_password = "abc12345"    
update_password_student(email,password,new_password)

# #_____________________________________UPDATE_PASSWORD_TEACHER_______________________________

def update_password_teacher(email,password,new_password):
    cursor.execute("Update teacher SET  password = ? WHERE email = ? AND password = ? ", (new_password,email,password))
t_email = "k214890@nu.edu.pk"
t_password = "abc123"
t_newpassword = "abc12345"    
update_password_teacher(email,password,new_password)

#____________________________Retrieve_FILES_FROM_CODE_COLUMN_______________________________ 

def Get_Files():
    counter=1
    data = cursor.execute("""SELECT * FROM project""")
    for x in data.fetchall(): 
       with open("{}.pdf".format(counter),"wb") as f :
            title = x[8]
            course_code = x[5]
            student_id = x[4]
            os.chdir("C:/Users/usman/OneDrive/Desktop/report")
            f.write(x[1])
            os.chdir("C:/Users/usman/OneDrive/Desktop/code")
            f.write(x[2])
            counter = counter + 1

Get_Files()

#____________________________UPDATE_COURSE_CODE___________________________________________

def update_coursecode(new,old):
    cursor.execute("update course set C_ID = ? where C_ID = ?", (new,old))
new_cid = 3005
old_cid = 123

update_coursecode(new_cid,old_cid)


conn.commit()
cursor.close()
conn.commit()

conn.close()

