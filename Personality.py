from tkinter import *
import tkinter.messagebox
import operator
from students import *
import auto_test
import pickle

class Personality (Frame):

    def __init__ (self, master, number):
        master.title("Personality Questions")
        super(Personality, self).__init__(master)
        self.master = master
        self.grid()
        self.number = number
        self.subper_button ()
        self.get_personality()
        
    def spacer (self):
        self.grid(pady = 20, padx = 20)
        self.space1 = Label(self, text = '    ', font=('MS', 8, 'bold'))
    def get_personality(self):
        self.str_msg= ""
        # Provide Instructions
        #self.pack(pady= 30, padx = 30)
        self.inst = Label(self, text = 'Instructions:\n\n', font=('MS', 8, 'bold'))
        self.inst.grid(row= 2, column = 0, sticky = W)
        self.inst_info = Label (self, text = "Please read the following words and rank them from 4 to 1 with 4 being the word that best describes you \n"
                                + "and 1 being the least like you. Please use each value only once per line and select your answer instinctively, \n"
                                + "not what you perceive to be the 'best' answer. ", font=('MS', 8))
        self.inst_info.grid(row = 2, column = 1, columnspan = 6, rowspan = 3, sticky = W)
        self.space = Label(self, text = '     ', font=('MS', 8, 'bold'))
        self.space.grid(row= 6, rowspan =2, column = 0, sticky = W)

        self.space1 = Label(self, text = '    ', font=('MS', 8, 'bold'))
        self.space1.grid(row= 7, column = 0, sticky = W)

        # Ask questions
        #Line 1
        
        self.r1q1 = Label (self, text = 'Forceful', font=('MS', 8, 'bold'))
        self.r1q1.grid (row = 8, column = 0)
        self.r1q1_opt = Spinbox(self, from_=1, to= 4, width = 3)
        self.r1q1_opt.grid (row= 8, column = 1)
        
        self.r1q2 = Label (self, text = 'Lively', font=('MS', 8, 'bold'))
        self.r1q2.grid (row = 8, column = 2)
        self.r1q2_opt = Spinbox(self, from_=1, to= 4, width = 3)
        self.r1q2_opt.grid (row= 8, column = 3, columnspan = 1, sticky = W)

        self.r1q3 = Label (self, text = 'Modest', font=('MS', 8, 'bold'))
        self.r1q3.grid (row = 8, column = 4)
        self.r1q3_opt = Spinbox(self, from_=1, to= 4, width = 3)
        self.r1q3_opt.grid (row= 8, column = 5, columnspan = 1)

        self.r1q4 = Label (self, text = 'Tactful', font=('MS', 8, 'bold'))
        self.r1q4.grid (row = 8, column = 6)
        self.r1q4_opt = Spinbox(self, from_=1, to= 4, width = 4)
        self.r1q4_opt.grid (row= 8, column = 7, columnspan = 1)

        self.spacer()
        self.space1.grid(row= 9, column = 0, sticky = W)

         

            
        #Line3
        self.r3q1 = Label (self, text = 'Direct', font=('MS', 8, 'bold'))
        self.r3q1.grid (row = 12, column = 0)
        self.r3q1_opt = Spinbox(self, from_=1, to= 4, width = 3)
        self.r3q1_opt.grid (row= 12, column = 1)
        
        self.r3q2 = Label (self, text = 'Animated', font=('MS', 8, 'bold'))
        self.r3q2.grid (row = 12, column = 2)
        self.r3q2_opt = Spinbox(self, from_=1, to= 4, width = 3)
        self.r3q2_opt.grid (row= 12, column = 3, columnspan = 1, sticky = W)

        self.r3q3 = Label (self, text = 'Agreeable', font=('MS', 8, 'bold'))
        self.r3q3.grid (row = 12, column = 4)
        self.r3q3_opt = Spinbox(self, from_=1, to= 4, width = 3)
        self.r3q3_opt.grid (row= 12, column = 5, columnspan = 1)

        self.r3q4 = Label (self, text = 'Accurate', font=('MS', 8, 'bold'))
        self.r3q4.grid (row = 12 , column = 6)
        self.r3q4_opt = Spinbox(self, from_=1, to= 4, width = 4)
        self.r3q4_opt.grid (row= 12, column = 7, columnspan = 1)

        self.spacer()
        self.space1.grid(row= 13, column = 0, sticky = W)
        
        
        #Line4
        self.r4q1 = Label (self, text = 'Tough', font=('MS', 8, 'bold'))
        self.r4q1.grid (row = 14, column = 0)
        self.r4q1_opt = Spinbox(self, from_=1, to= 4, width = 3)
        self.r4q1_opt.grid (row= 14, column = 1)
        
        self.r4q2 = Label (self, text = 'People-orientated', font=('MS', 8, 'bold'))
        self.r4q2.grid (row = 14, column = 2)
        self.r4q2_opt = Spinbox(self, from_=1, to= 4, width = 3)
        self.r4q2_opt.grid (row= 14, column = 3, columnspan = 1, sticky = W)

        self.r4q3 = Label (self, text = 'Gentle', font=('MS', 8, 'bold'))
        self.r4q3.grid (row = 14, column = 4)
        self.r4q3_opt = Spinbox(self, from_=1, to= 4, width = 3)
        self.r4q3_opt.grid (row= 14, column = 5, columnspan = 1)

        self.r4q4 = Label (self, text = 'Perfectionist', font=('MS', 8, 'bold'))
        self.r4q4.grid (row = 14 , column = 6)
        self.r4q4_opt = Spinbox(self, from_=1, to= 4, width = 4)
        self.r4q4_opt.grid (row= 14, column = 7, columnspan = 1)

        self.spacer()
        self.space1.grid(row= 15, column = 0, sticky = W)
        
        

        #Line5
        self.r5q1 = Label (self, text = 'Daring', font=('MS', 8, 'bold'))
        self.r5q1.grid (row = 16, column = 0)
        self.r5q1_opt = Spinbox(self, from_=1, to= 4, width = 3)
        self.r5q1_opt.grid (row= 16, column = 1)
        
        self.r5q2 = Label (self, text = 'Impulsive', font=('MS', 8, 'bold'))
        self.r5q2.grid (row = 16, column = 2)
        self.r5q2_opt = Spinbox(self, from_=1, to= 4, width = 3)
        self.r5q2_opt.grid (row= 16, column = 3, columnspan = 1, sticky = W)

        self.r5q3 = Label (self, text = 'Kind', font=('MS', 8, 'bold'))
        self.r5q3.grid (row = 16, column = 4)
        self.r5q3_opt = Spinbox(self, from_=1, to= 4, width = 3)
        self.r5q3_opt.grid (row= 16, column = 5, columnspan = 1)

        self.r5q4 = Label (self, text = 'Cautious', font=('MS', 8, 'bold'))
        self.r5q4.grid (row = 16 , column = 6)
        self.r5q4_opt = Spinbox(self, from_=1, to= 4, width = 4)
        self.r5q4_opt.grid (row= 16, column = 7, columnspan = 1)

        self.spacer()
        self.space1.grid(row= 17, column = 0, sticky = W)
        
       

        #Line6
        self.r6q1 = Label (self, text = 'Competitive', font=('MS', 8, 'bold'))
        self.r6q1.grid (row = 18, column = 0)
        self.r6q1_opt = Spinbox(self, from_=1, to= 4, width = 3)
        self.r6q1_opt.grid (row= 18, column = 1)
        
        self.r6q2 = Label (self, text = 'Expressive', font=('MS', 8, 'bold'))
        self.r6q2.grid (row = 18, column = 2)
        self.r6q2_opt = Spinbox(self, from_=1, to= 4, width = 3)
        self.r6q2_opt.grid (row= 18, column = 3, columnspan = 1, sticky = W)

        self.r6q3 = Label (self, text = 'Supportive', font=('MS', 8, 'bold'))
        self.r6q3.grid (row = 18, column = 4)
        self.r6q3_opt = Spinbox(self, from_=1, to= 4, width = 3)
        self.r6q3_opt.grid (row= 18, column = 5, columnspan = 1)

        self.r6q4 = Label (self, text = 'Precise', font=('MS', 8, 'bold'))
        self.r6q4.grid (row = 18 , column = 6)
        self.r6q4_opt = Spinbox(self, from_=1, to= 4, width = 4)
        self.r6q4_opt.grid (row= 18, column = 7, columnspan = 1)

        self.spacer()
        self.space1.grid(row= 19, column = 0, sticky = W)
        
        #Line7
        self.r7q1 = Label (self, text = 'Argumentative', font=('MS', 8, 'bold'))
        self.r7q1.grid (row = 20, column = 0)
        self.r7q1_opt = Spinbox(self, from_=1, to= 4, width = 3)
        self.r7q1_opt.grid (row= 20, column = 1)
        
        self.r7q2 = Label (self, text = 'Fun-Loving', font=('MS', 8, 'bold'))
        self.r7q2.grid (row = 20, column = 2)
        self.r7q2_opt = Spinbox(self, from_=1, to= 4, width = 3)
        self.r7q2_opt.grid (row= 20, column = 3, columnspan = 1, sticky = W)

        self.r7q3 = Label (self, text = 'Patient', font=('MS', 8, 'bold'))
        self.r7q3.grid (row = 20, column = 4)
        self.r7q3_opt = Spinbox(self, from_=1, to= 4, width = 3)
        self.r7q3_opt.grid (row= 20, column = 5, columnspan = 1)

        self.r7q4 = Label (self, text = 'Logical', font=('MS', 8, 'bold'))
        self.r7q4.grid (row = 20 , column = 6)
        self.r7q4_opt = Spinbox(self, from_=1, to= 4, width = 4)
        self.r7q4_opt.grid (row= 20, column = 7, columnspan = 1)

        self.spacer()
        self.space1.grid(row= 21, column = 0, sticky = W)
        
        #Line8
        self.r8q1 = Label (self, text = 'Bold', font=('MS', 8, 'bold'))
        self.r8q1.grid (row = 22, column = 0)
        self.r8q1_opt = Spinbox(self, from_=1, to= 4, width = 3)
        self.r8q1_opt.grid (row= 22, column = 1)
        
        self.r8q2 = Label (self, text = 'Spontaneous', font=('MS', 8, 'bold'))
        self.r8q2.grid (row = 22, column = 2)
        self.r8q2_opt = Spinbox(self, from_=1, to= 4, width = 3)
        self.r8q2_opt.grid (row= 22, column = 3, columnspan = 1, sticky = W)

        self.r8q3 = Label (self, text = 'Stable', font=('MS', 8, 'bold'))
        self.r8q3.grid (row = 22, column = 4)
        self.r8q3_opt = Spinbox(self, from_=1, to= 4, width = 3)
        self.r8q3_opt.grid (row= 22, column = 5, columnspan = 1)

        self.r8q4 = Label (self, text = 'Organized', font=('MS', 8, 'bold'))
        self.r8q4.grid (row = 22 , column = 6)
        self.r8q4_opt = Spinbox(self, from_=1, to= 4, width = 4)
        self.r8q4_opt.grid (row= 22, column = 7, columnspan = 1)

        self.spacer()
        self.space1.grid(row= 23, column = 0, sticky = W)
        
                 #Line10
        self.r10q1 = Label (self, text = 'Candid', font=('MS', 8, 'bold'))
        self.r10q1.grid (row = 26, column = 0)
        self.r10q1_opt = Spinbox(self, from_=1, to= 4, width = 3)
        self.r10q1_opt.grid (row= 26, column = 1)
        
        self.r10q2 = Label (self, text = 'Cheerful', font=('MS', 8, 'bold'))
        self.r10q2.grid (row = 26, column = 2)
        self.r10q2_opt = Spinbox(self, from_=1, to= 4, width = 3)
        self.r10q2_opt.grid (row= 26, column = 3, columnspan = 1, sticky = W)

        self.r10q3 = Label (self, text = 'Loyal', font=('MS', 8, 'bold'))
        self.r10q3.grid (row = 26, column = 4)
        self.r10q3_opt = Spinbox(self, from_=1, to= 4, width = 3)
        self.r10q3_opt.grid (row= 26, column = 5, columnspan = 1)

        self.r10q4 = Label (self, text = 'Serious', font=('MS', 8, 'bold'))
        self.r10q4.grid (row = 26 , column = 6)
        self.r10q4_opt = Spinbox(self, from_=1, to= 4, width = 4)
        self.r10q4_opt.grid (row= 26, column = 7, columnspan = 1)

        self.spacer()
        self.space1.grid(row= 27, column = 0, sticky = W)
        
         #Line11
        self.r11q1 = Label (self, text = 'Independent', font=('MS', 8, 'bold'))
        self.r11q1.grid (row = 28, column = 0)
        self.r11q1_opt = Spinbox(self, from_=1, to= 4, width = 3)
        self.r11q1_opt.grid (row= 28, column = 1)
        
        self.r11q2 = Label (self, text = 'Enthusiastic', font=('MS', 8, 'bold'))
        self.r11q2.grid (row = 28, column = 2)
        self.r11q2_opt = Spinbox(self, from_=1, to= 4, width = 3)
        self.r11q2_opt.grid (row= 28, column = 3, columnspan = 1, sticky = W)

        self.r11q3 = Label (self, text = 'Good Listener', font=('MS', 8, 'bold'))
        self.r11q3.grid (row = 28, column = 4)
        self.r11q3_opt = Spinbox(self, from_=1, to= 4, width = 3)
        self.r11q3_opt.grid (row= 28, column = 5, columnspan = 1)

        self.r11q4 = Label (self, text = 'High Standards', font=('MS', 8, 'bold'))
        self.r11q4.grid (row = 28 , column = 6)
        self.r11q4_opt = Spinbox(self, from_=1, to= 4, width = 4)
        self.r11q4_opt.grid (row= 28, column = 7, columnspan = 1)

        self.spacer()
        self.space1.grid(row= 29, column = 0, sticky = W)
        
         #Line12
        self.r12q1 = Label (self, text = 'Risk Taker', font=('MS', 8, 'bold'))
        self.r12q1.grid (row = 30, column = 0)
        self.r12q1_opt = Spinbox(self, from_=1, to= 4, width = 3)
        self.r12q1_opt.grid (row= 30, column = 1)
        
        self.r12q2 = Label (self, text = 'Talkative', font=('MS', 8, 'bold'))
        self.r12q2.grid (row = 30, column = 2)
        self.r12q2_opt = Spinbox(self, from_=1, to= 4, width = 3)
        self.r12q2_opt.grid (row= 30, column = 3, columnspan = 1, sticky = W)

        self.r12q3 = Label (self, text = 'Conflict Averse', font=('MS', 8, 'bold'))
        self.r12q3.grid (row = 30, column = 4)
        self.r12q3_opt = Spinbox(self, from_=1, to= 4, width = 3)
        self.r12q3_opt.grid (row= 30, column = 5, columnspan = 1)

        self.r12q4 = Label (self, text = 'Factual', font=('MS', 8, 'bold'))
        self.r12q4.grid (row = 30 , column = 6)
        self.r12q4_opt = Spinbox(self, from_=1, to= 4, width = 4)
        self.r12q4_opt.grid (row= 30, column = 7, columnspan = 1)

        self.spacer()
        self.space1.grid(row= 31, column = 0, sticky = W)
       
#Line2
        self.r2q1 = Label (self, text = 'Aggressive', font=('MS', 8, 'bold'))
        self.r2q1.grid (row = 32, column = 0)
        self.r2q1_opt = Spinbox (self, from_ =1, to = 4, width = 3)
        self.r2q1_opt.grid (row= 32, column = 1)
        
        self.r2q2 = Label (self, text = 'Emotional', font=('MS', 8, 'bold'))
        self.r2q2.grid (row = 32, column = 2)
        self.r2q2_opt = Spinbox (self, from_ =1, to = 4, width = 3)
        self.r2q2_opt.grid (row= 32, column = 3, columnspan = 1, sticky = W)
        

        self.r2q3 = Label (self, text = 'Accomodating', font=('MS', 8, 'bold'))
        self.r2q3.grid (row = 32, column = 4)
        self.r2q3_opt = Spinbox(self, from_=1, to= 4, width = 3)
        self.r2q3_opt.grid (row= 32, column = 5, columnspan = 1)

        self.r2q4 = Label (self, text = 'Consistent', font=('MS', 8, 'bold'))
        self.r2q4.grid (row = 32 , column = 6)
        self.r2q4_opt = Spinbox(self, from_=1, to= 4, width = 4)
        self.r2q4_opt.grid (row= 32, column = 7, columnspan = 1)
        self.spacer()
        self.space1.grid(row= 33, column = 0, sticky = W)

 #Line9
        self.r9q1 = Label (self, text = 'Take Charge', font=('MS', 8, 'bold'))
        self.r9q1.grid (row = 34, column = 0)
        self.r9q1_opt = Spinbox(self, from_=1, to= 4, width = 3)
        self.r9q1_opt.grid (row= 34, column = 1)
        
        self.r9q2 = Label (self, text = 'Optimistic', font=('MS', 8, 'bold'))
        self.r9q2.grid (row = 34, column = 2)
        self.r9q2_opt = Spinbox(self, from_=1, to= 4, width = 3)
        self.r9q2_opt.grid (row= 34, column = 3, columnspan = 1, sticky = W)

        self.r9q3 = Label (self, text = 'Peaceful', font=('MS', 8, 'bold'))
        self.r9q3.grid (row = 34, column = 4)
        self.r9q3_opt = Spinbox(self, from_=1, to= 4, width = 3)
        self.r9q3_opt.grid (row= 34, column = 5, columnspan = 1)

        self.r9q4 = Label (self, text = 'Conscientious', font=('MS', 8, 'bold'))
        self.r9q4.grid (row = 34 , column = 6)
        self.r9q4_opt = Spinbox(self, from_=1, to= 4, width = 4)
        self.r9q4_opt.grid (row= 34, column = 7, columnspan = 1)

        self.spacer()
        self.space1.grid(row= 35, column = 0, sticky = W)
  

    def subper_button (self,):
        self.submit_bttn = Button(self, text= 'Submit', command = self.store_resp, font=('MS', 8, 'bold')).grid(row = 37, column = 3, sticky = S)

    def store_resp (self):
        self.str_msg = ""
        self.r1_total = int(self.r1q1_opt.get())+ int(self.r1q2_opt.get())+ int(self.r1q3_opt.get()) + int(self.r1q4_opt.get())
        if self.r1_total != 10:
            self.str_msg = "Please make sure each number is only selected once in Row 1 \n"
        self.r3_total = int(self.r3q1_opt.get())+ int(self.r3q2_opt.get())+ int(self.r3q3_opt.get())+ int(self.r3q4_opt.get())
        if self.r3_total != 10:
            self.str_msg = self.str_msg + "Please make sure each number is only selected once in Row 2 \n"
        self.r4_total = int(self.r4q1_opt.get())+ int(self.r4q2_opt.get())+ int(self.r4q3_opt.get())+ int(self.r4q4_opt.get())
        if self.r4_total != 10:
            self.str_msg = self.str_msg + "Please make sure each number is only selected once in Row 3 \n"
        self.r5_total = int(self.r5q1_opt.get())+ int(self.r5q2_opt.get())+ int(self.r5q3_opt.get())+ int(self.r5q4_opt.get())    
        if self.r5_total != 10:
            self.str_msg = self.str_msg + "Please make sure each number is only selected once in Row 4 \n"
        self.r6_total = int(self.r6q1_opt.get())+ int(self.r6q2_opt.get())+ int(self.r6q3_opt.get())+ int(self.r6q4_opt.get())
        if self.r6_total != 10:
            self.str_msg = self.str_msg + "Please make sure each number is only selected once in Row 5 \n"
        self.r7_total = int(self.r7q1_opt.get())+ int(self.r7q2_opt.get())+ int(self.r7q3_opt.get())+ int(self.r7q4_opt.get())
        if self.r7_total != 10:
            self.str_msg = self.str_msg + "Please make sure each number is only selected once in Row 6 \n"
        self.r8_total = int(self.r8q1_opt.get())+ int(self.r8q2_opt.get())+ int(self.r8q3_opt.get())+ int(self.r8q4_opt.get())
        if self.r8_total != 10:
            self.str_msg = self.str_msg + "Please make sure each number is only selected once in Row 7 \n"
        self.r10_total = int(self.r10q1_opt.get())+ int(self.r10q2_opt.get())+ int(self.r10q3_opt.get())+ int(self.r10q4_opt.get())
        if self.r10_total != 10:
            self.str_msg = self.str_msg + "Please make sure each number is only selected once in Row 8 \n"
        self.r11_total = int(self.r11q1_opt.get())+ int(self.r11q2_opt.get())+ int(self.r11q3_opt.get())+ int(self.r11q4_opt.get())
        if self.r11_total != 10:
            self.str_msg = self.str_msg + "Please make sure each number is only selected once in Row 9 \n"
        self.r12_total = int(self.r12q1_opt.get())+ int(self.r12q2_opt.get())+ int(self.r12q3_opt.get())+ int(self.r12q4_opt.get())
        if self.r12_total != 10:
            self.str_msg = self.str_msg +"Please make sure each number is only selected once in Row 10 \n"
        self.r2_total = int(self.r2q1_opt.get())+ int(self.r2q2_opt.get())+ int(self.r2q3_opt.get())+ int(self.r2q4_opt.get())
        if self.r2_total != 10:
            self.str_msg = self.str_msg + "Please make sure each number is only selected once in Row 11 \n"
        self.r9_total = int(self.r9q1_opt.get())+ int(self.r9q2_opt.get())+ int(self.r9q3_opt.get())+ int(self.r9q4_opt.get())
        if self.r9_total != 10:
            self.str_msg = self.str_msg + "Please make sure each number is only selected once in Row 12 \n"
        if self.str_msg == "":
           
           person = {"leader_score": 0, "teamws_score":0,"coordin_score":0,"finisher_score":0}
           person ["leader"] = int(self.r1q1_opt.get()) + int(self.r2q1_opt.get())+ int(self.r3q1_opt.get())+ int(self.r4q1_opt.get()) + int(self.r5q1_opt.get()) + int(self.r6q1_opt.get()) + int(self.r7q1_opt.get()) + int(self.r8q1_opt.get()) + int(self.r9q1_opt.get()) + int(self.r10q1_opt.get()) + int(self.r11q1_opt.get()) + int(self.r12q1_opt.get())
           #print ( person ["leader"])
           person ["teamworker"] =  int(self.r1q2_opt.get()) + int(self.r2q2_opt.get())+ int(self.r3q2_opt.get())+ int(self.r4q2_opt.get()) + int(self.r5q2_opt.get()) + int(self.r6q2_opt.get()) + int(self.r7q2_opt.get()) + int(self.r8q2_opt.get()) + int(self.r9q2_opt.get()) + int(self.r10q2_opt.get()) + int(self.r11q2_opt.get()) + int(self.r12q2_opt.get())
           #print ( person ["teamworker"])
           person ["coordinator"]= int(self.r1q3_opt.get()) + int(self.r2q3_opt.get())+ int(self.r3q3_opt.get())+ int(self.r4q3_opt.get()) + int(self.r5q3_opt.get()) + int(self.r6q3_opt.get()) + int(self.r7q3_opt.get()) + int(self.r8q3_opt.get()) + int(self.r9q3_opt.get()) + int(self.r10q3_opt.get()) + int(self.r11q3_opt.get()) + int(self.r12q3_opt.get())
           #print ( person ["coordinator"])
           person ["finisher"] = int(self.r1q4_opt.get()) + int(self.r2q4_opt.get())+ int(self.r3q4_opt.get())+ int(self.r4q4_opt.get()) + int(self.r5q4_opt.get()) + int(self.r6q4_opt.get()) + int(self.r7q4_opt.get()) + int(self.r8q4_opt.get()) + int(self.r9q4_opt.get()) + int(self.r10q4_opt.get()) + int(self.r11q4_opt.get()) + int(self.r12q4_opt.get())
           #print ( person ["finisher"])

           personality_type = highest_val(person)
           with open("stu_dict.pkl", "rb") as f:
               
               try:
                   stu_dict = pickle.load(f) #load

               except EOFError:
                   stu_dict = {}

           stu_dict[self.number].addRole(personality_type)

           with open("stu_dict.pkl", "wb") as f:
               pickle.dump(stu_dict, f)
                    
           tkinter.messagebox.showinfo("Personality Questionnaire", "Your personality best fits the " + personality_type + " type. Thank you for submitting your questionnaire!")
           self.master.destroy()    
           
        else:
          tkinter.messagebox.showinfo("Please fix the following errors:", self.str_msg)
          self.str_msg == ""

def highest_val(personality):
     """ a) create a list of the dict's keys and values; 
         b) return the key with the max value"""  
     values=list(personality.values())
     keys=list(personality.keys())
     return keys[values.index(max(values))]



if __name__ == '__main__':

    #test_list = auto_test.list_of_students(15)
    #test_dict = {}
    #with open("stu_dict.pkl", "wb") as f:
    #    for item in test_list:
    #        test_dict[item.number] = item
     #       test_no = item.number
    #    pickle.dump(test_dict, f)

    root = Tk()
    
    app = Personality(root, number)
    root.mainloop()
