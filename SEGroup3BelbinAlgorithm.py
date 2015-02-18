#Algorithm to determine Belbin's roles and place them into suitable teams
#TODO// figure out how to cycle through each entry in a db

import MySQLdb, re

#**All of this may not be needed once the database is actually implemented**
db = MySQLdb.connect(host = "localhost", #hostname
                     user = 'sla5srr', #user (Sam for now)
                     password = 'pa55word', #default password
                     db = 'qresults') #questionnaire results

cur = db.cursor() #cursor object

cur.EXECUTE('DROP TABLE IF EXISTS Belbin') #troubleshooting: delete Belbin table if it somehow exists

cur.EXECUTE('CREATETABLE Belbin') #create a new table to contain Belbin's roles
(
    StudentID varchar(10) NOT NULL      #student number
    TestResult int                      #the overall test score
    BelbinRole varchar(20)              #Belbin's team role
    PRIMARY KEY (StudentID)
)
db.commit()

findTotal()
findBelbin(total, StudentID)


def findTotal(): #function to pull each data string from the database and assess
#the idea is that the data is stored in a table with
    
    list(data)=[] #empty list for data
    str(eachRow) = cur.EXECUTE(SELECT * FROM QRESULTS)#pull row from database
    data = eachRow.strip().split('|')#separate the data within the list
    total = 0
    StudentID = re.findall(r'C/d{7}',data) #find standard student ID with regex
    

#simple answer-based algorithm to assign an overall score to the questionnaire results
#can be made more complex to assess the answer to each question individually if necessary
#answers 1-4 will be made more specific (probably as ints) as we know what they will be

    for item in list:
        if item is not int: #skip over the names and student number
            continue
        if item = "answer1":
            total = total +4
        elif item = "answer2":
            total = total +3
        elif item = "answer3":
            total = total +2
        elif item = "answer4":
            total = total +1
        return total, StudentID

#use the total to place the candidate into one of Belbin's roles
#values are placeholder only for now
    
def findBelbin(total,StudentID): 
    if total is >=0 and <=10:
        cur.EXECUTE(INSERT INTO Belbin (StudentId, TestResult, BelbinRole)
        VALUES (StudentID, total, 'Plant'))
        db.commit()
    if total is >=11 and <=20:
        cur.EXECUTE(INSERT INTO Belbin (StudentId, TestResult, BelbinRole)
        VALUES (StudentID, total, 'Monitor Evaluator'))
        db.commit()
    if total is >=21 and <=30:
        cur.EXECUTE(INSERT INTO Belbin (StudentId, TestResult, BelbinRole)
        VALUES (StudentID, total, 'Co-ordinator'))
        db.commit()
    if total is >=31 and <=40:
        cur.EXECUTE(INSERT INTO Belbin (StudentId, TestResult, BelbinRole)
        VALUES (StudentID, total, 'Resource Investigator'))
        db.commit()
    if total is >=41 and <=50:
        cur.EXECUTE(INSERT INTO Belbin (StudentId, TestResult, BelbinRole)
        VALUES (StudentID, total, 'Implementer'))
        db.commit
    if total is >=51 and <=60:
        cur.EXECUTE(INSERT INTO Belbin (StudentId, TestResult, BelbinRole)
        VALUES (StudentID, total, 'Completer Finisher'))
        db.commit
    if total is >=61 and <=70:
        cur.EXECUTE(INSERT INTO Belbin (StudentId, TestResult, BelbinRole)
        VALUES (StudentID, total, 'Teamworker'))
        db.commit
    if total is >=71 and <=80:
        cur.EXECUTE(INSERT INTO Belbin (StudentId, TestResult, BelbinRole)
        VALUES (StudentID, total, 'Shaper'))
        db.commit
    if total is >=81 and <=90:
        cur.EXECUTE(INSERT INTO Belbin (StudentId, TestResult, BelbinRole)
        VALUES (StudentID, total, 'Specialist'))
        db.commit
    return

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

    
#SAMPLE CODE FOR CREATION OF DATABASE TO STORE TEST RESULTS

cur.EXECUTE(CREATETABLE qresults
    (StudentID varchar2(10)
     FirstName varchar2 (255)
     LastName varchar2 (255)
     Email varchar2 (255)
     A1 int
     A2 int
     A3 int
     A4 int
     ...
     A15 int
     PRIMARY KEY(StudentID)
     ))
    
db.commit()
    
