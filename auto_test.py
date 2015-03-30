'''
Module with functions for automated testing.
'''
from students import *
import groups
import random

raw_names = '''Jada Naquin
Jamey Kofoed
Edda Beauchemin
Nancee Vandeusen
Denita Moorhouse
Nakisha Whiteside
Lia Tavarez
Joelle Marlett
Lashanda Hyler
Fae Oliphant
Johna Brey
Evie Sansbury
Tandra Pintor
Chassidy Cutler
Keturah Ryant
Richie Olaughlin
Darla Liller
Alison Sanzone
Jaimee Esper
Ayanna Candela
Cherish Hentz
Nilsa Cartledge
Josie Romines
Estrella Shock
Mildred Faith
Rosemary Shivers
Dollie Enterline
Breann Greathouse
Yvonne Formby
Myrta Winsett
Jimmy Crase
Cherelle Liss
Sasha Gaulding
Gail Rodrick
Mckinley Wakeman
Claude Silvernail
Letha Chance
Dia Vice
Vergie Wickert
Felton Fluellen
Yael Maharaj
Chi Friddle
Toi Scharff
Lianne Dandy
Santina Officer
Tran Lindsay
Earnest Mussman
Andreas Aust
Frida Belles
Jon Isaman'''

list_of_names = raw_names.split("\n")

roles = ["Plant", "Monitor Evaluator", "Co-ordinator", "Resource Investigator", "Implementer", "Complete Finisher", "Teamworker", "Shapers", "Specialist"]

def list_of_students(student_no):

    '''Creates a list of randomised Student objects. Must specify number of students (size of list).''' 

    output_list = []
    i = 0
    
    while i < student_no:
        name = random.choice(list_of_names)
        first_name, last_name = name.split(" ")
        student = Student(first_name, last_name, random.randint(1,999999), "{}@cardiff.ac.uk".format(first_name), grades = random.randint(40,90), role = random.choice(roles))
        output_list.append(student)

        i += 1

    return output_list

def list_of_groups(group_no, size = random.randint(8,15)):

    '''Creates a list of randomised Group objects. Must specify number of Groups (size of list).
    May also specify size of group; otherwise group size is randomly assigned between 8 and 15.'''

    output_list = []
    i = 1

    while i <= group_no:
        student_list = list_of_students(size)
        a_group = groups.Group(i)

        for item in student_list:
            a_group.add_student(item)

        output_list.append(a_group)
        i += 1

    return output_list
        

if __name__ == "__main__":
    test = list_of_groups(8)
    for item in test:
        for entry in item.contents:
            print(entry)
        print("Next group:")

    
