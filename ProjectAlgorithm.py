#Algorithm to determine Belbin's roles and place them into suitable teams
#TODO// figure out how to cycle through each entry in a db

import sqlite3
import re

#function to pull each data string from the database and assess
#the idea is that the data is stored in a table with
#**All of this may not be needed once the database is actually implemented**
def findTotal(): 
    data=[] 
    cur.execute("SELECT * FROM qresults")
    
    data = eachRow.strip().split('|')
    total = 0
    StudentID = re.findall(r'C/d{7}',data) 
    
#simple answer-based algorithm to assign an overall score to the questionnaire results
#can be made more complex to assess the answer to each question individually if necessary
#answers 1-4 will be made more specific (probably as ints) as we know what they will be

    for item in list:
        if item is not int: #skip over the names and student number
            continue
        if item == "answer1":
            total = total +4
        elif item == "answer2":
            total = total +3
        elif item == "answer3":
            total = total +2
        elif item == "answer4":
            total = total +1
        return total, StudentID
    
#use the total to place the candidate into one of Belbin's roles
#values are placeholder only for now
    
def findBelbin(total,StudentID): 
    if total >= 0 and total <= 10:
        cur.execute("INSERT INTO Belbin (StudentId, TestResult, BelbinRole")
        VALUES (StudentID, total, 'Plant')
        db.commit()
    if total >= 11 and total <= 20:
        cur.execute("INSERT INTO Belbin (StudentId, TestResult, BelbinRole")
        VALUES (StudentID, total, 'Monitor Evaluator')
        db.commit()
    if total >= 21 and total <= 30:
        cur.execute("INSERT INTO Belbin (StudentId, TestResult, BelbinRole")
        VALUES (StudentID, total, 'Co-ordinator')
        db.commit()
    if total >= 31 and total <= 40:
        cur.execute("INSERT INTO Belbin (StudentId, TestResult, BelbinRole")
        VALUES (StudentID, total, 'Resource Investigator')
        db.commit()
    if total >= 41 and total <= 50:
        cur.execute("INSERT INTO Belbin (StudentId, TestResult, BelbinRole")
        VALUES (StudentID, total, 'Implementer')
        db.commit
    if total >= 51 and total <= 60:
        cur.execute("INSERT INTO Belbin (StudentId, TestResult, BelbinRole")
        VALUES (StudentID, total, 'Completer Finisher')
        db.commit
    if total >= 61 and total <= 70:
        cur.execute("INSERT INTO Belbin (StudentId, TestResult, BelbinRole")
        VALUES (StudentID, total, 'Teamworker')
        db.commit
    if total >= 71 and total <= 80:
        cur.execute("INSERT INTO Belbin (StudentId, TestResult, BelbinRole")
        VALUES (StudentID, total, 'Shaper')
        db.commit
    if total >= 81 and total <= 90:
        cur.execute("INSERT INTO Belbin (StudentId, TestResult, BelbinRole")
        VALUES (StudentID, total, 'Specialist')
        db.commit
    return

def main():


#SAMPLE CODE FOR CREATION OF DATABASE TO STORE TEST RESULTS

    cur.execute("DROP TABLE IF EXISTS QRESULTS")
    cur.execute("""CREATE TABLE QRESULTS
    (STUDENTID TEXT PRIMARY KEY NOT NULL, 
     FIRST TEXT,
     LAST TEXT,
     EMAIL CHAR(50),
     A1 INT,A2 INT,A3 INT,A4 INT,A5 INT, A6 INT,A7 INT,A8 INT,A9 INT,A10 INT
     )""")
    print("Created db successfully")

    cur.execute("""INSERT INTO QRESULTS
    (STUDENTID, FIRST, LAST, EMAIL, A1, A2, A3, A4, A5,
    A6, A7, A8, A9, A10)
    VALUES
    ('C0506344', 'Sam', 'Rogers', 'rogerssr@cf.ac.uk', 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1)
    """)
    print("Data entered successfully")
    db.commit()

#create a new table to contain Belbin's roles
    cur.execute("DROP TABLE IF EXISTS BELBIN") 
    cur.execute("""CREATE TABLE BELBIN 
    (STUDENTID TEXT PRIMARY KEY NOT NULL,      
     RESULT INT,                     
     BELBINROLE TEXT
     )""")
    db.commit()

    findTotal()
    findBelbin(total, StudentID)
    db.close()

#start of program
db = sqlite3.connect('example.db') 
cur = db.cursor()
main()

#determine group makeup
#two classes - student with attributes: studentNumber, belbinRole, belbinSubRole 
#and group with attributes: members, belbinRole, maxSize
#BelbinRole is one of the three groups including (PL, ME, CO)(RI, IMP, CF)(TW, SH,SP)
#algorithm would be along the lines of:
#if student has belbinRole "xxxx" and group does not have belbinRole "xxxx"
#and number of members does not equal maxSize
#   add student to group
#move to next team, repeat the above, cycle through each team and reset
#if group has belbinRole "xxxx", check if group has belbinSubRole "yyyy"
#if group does not have belbinSubRole "yyyy" add student to group
