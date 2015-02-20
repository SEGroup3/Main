#Algorithm to determine Belbin's roles and place them into suitable teams
#TODO// figure out how to cycle through each entry in a db

import sqlite3
import re

#function to pull each data string from the database and assess
#the idea is that the data is stored in a table with
#**All of this may not be needed once the database is actually implemented**
def find_total(): 
    
    data=[]
    total = 0
    for row in cur.execute("SELECT * FROM qresults"):
        data.append(row)

#simple answer-based algorithm to assign an overall score to the questionnaire results
#can be made more complex to assess the answer to each question individually if necessary
#answers 1-4 will be made more specific (probably as ints) as we know what they will be

    for line in data:
        for item in line:
            if type(item) is str and re.match(r'C\d{7}',item):
                StudentID = item

            elif type(item) is int and item < 5:
                total += item

    find_belbin(total, StudentID)
    
#use the total to place the candidate into one of Belbin's roles
#values are placeholder only for now
    
def write_belbin(total,StudentID,belbin):
    cur.execute("""INSERT INTO BELBIN (STUDENTID, RESULT, BELBINROLE)
    VALUES (?,?,?)""",(StudentID, total, belbin))
    db.commit()
    for row in cur.execute("SELECT * FROM BELBIN"):
        print(row)

def find_belbin(total,StudentID): 
    if total >= 0 and total <= 10:
        belbin = 'Plant'

    elif total >= 11 and total <= 20:
        belbin = 'Monitor Evaluator'

    elif total >= 21 and total <= 30:
        belbin = 'Co-ordinator'

    elif total >= 31 and total <= 40:
        belbin = 'Resource Investigator'

    elif total >= 41 and total <= 50:
        belbin = 'Implementer'

    elif total >= 51 and total <= 60:
        belbin = 'Completer Finisher'

    elif total >= 61 and total <= 70:
        belbin = 'Teamworker'

    elif total >= 71 and total <= 80:
        belbin = 'Shaper'

    elif total >= 81 and total <= 90:
        belbin = 'Specialist'

    else:
        belbin = 'Unknown'

    write_belbin(total,StudentID,belbin)
    
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
    ('C0506344', 'Sam', 'Rogers', 'rogerssr@cf.ac.uk', 2, 4, 4, 1, 1,
    1, 1, 4, 2, 1)
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

    find_total()
    db.close()

if __name__ == "__main__":
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
