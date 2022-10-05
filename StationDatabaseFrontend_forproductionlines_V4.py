#This code is written by Zunaed Kibria (Email: zkibria@nevada.unr.edu) for Summer internship program at Hamilton Company, Reno
#Date: 25 August , 2022.
#To run this code you need to have python installed on the comuper
#To run this code you need to have station_Database_Backend_for_production.py file in the same folder
#Most of the module come with python as deafulat, only tkcalender needs to be installed seperately.


# This portion is written for importing required modules. 

from tkinter import*
from tkcalendar import*
#import pymysql
from tkinter import ttk
import random
import tkinter.messagebox
import datetime
import time
import tkinter.ttk as tkrtk
import tkinter as tkr
import station_Database_Backend_for_production
import tempfile, os


#From here mail class starts, inside the class all the variables, functionality, frames are defined

class stationRecords:

    def __init__(self,root):
     self.root = root
     self.root.title("Station Management Systems")
     self.root.geometry("1350x800+0+0")


    #+++++++++++++++++++++++++++++++++++Variables+++++++++++++++++++++++++++
     #There are total 25 variables defined for different parameters, users can change it according to their need.
     #Variable names are kept consistent throught the program (both in this file and station_Database_Backend_for_production.py file.
     
     Line = StringVar() 
     Shift = StringVar() 
     WorkstationID = StringVar() 
     WorkstationName = StringVar() 
     TesterID = StringVar() 
     TesterName = StringVar() 

     InspectionItemID = StringVar() 
     InspectionItemType = StringVar() 
     Descripton = StringVar() 
     InspectionGroupID = StringVar() 
     
     Test1 = StringVar() 
     Test2 = StringVar() 
     Test3 = StringVar() 
     Test4 = StringVar() 
     Test5 = StringVar() 

     NumericVal1 = StringVar() 
     NumericVal2 = StringVar() 
     NumericVal3= StringVar() 
     NumericVal4 = StringVar() 
     NumericVal5 = StringVar() 

     Checklist1 = StringVar()
     Checklist2 = StringVar()
     Checklist3 = StringVar()
     Checklist4 = StringVar()
     Checklist5 = StringVar()
     Print = StringVar()

     #========== Functions======
     #In this portion all the functions are defined.
     #iExit function is for exiting the program
     #iPrint function is for Printing the data in Print frame
     #clearData function helps to reset the screen
     #addData helps adding new data in the database
     #displayData shows the database data on the screen
     #search and update functions are not working , if you want you can comment out.
     #StationRec function is used for creating record into the database
     #Printdata is used for adding new information which comes with adddata function to the Print frame screen. That is why in the button section at self.btnAddData, command = Printdata

     
     def iExit():
        iExit = tkinter.messagebox.askyesno("Station Management Systems", "Confirm if you want to exit")
        if iExit > 0:
            root.destroy()
            return

     def iPrint():
        q = self.txtPrint.get("1.0", "end-1c")
        filename = tempfile.mktemp(".doc")
        open (filename,'w'). write(q)
        os.startfile(filename, "print")


     def clearData():
        self.cboLine.delete(0,END)
        self.cboShift.delete(0,END)
        self.txtWorkstationID.delete(0,END)
        self.txtWorkstationName.delete(0,END)
        self.txtTesterID.delete(0,END)
        self.txtTesterName.delete(0,END)
        
        self.txtInspectionItemID.delete(0,END)
        self.txtInspectionItemType.delete(0,END)
        self.txtDescripton.delete(0,END)
        self.txtInspectionGroupID.delete(0,END)

        self.cboTest1.delete(0,END)
        self.cboTest2.delete(0,END)
        self.cboTest3.delete(0,END)
        self.cboTest4.delete(0,END)
        self.cboTest5.delete(0,END)

        self.SpNumericVal1.delete(0,END)
        self.SpNumericVal2.delete(0,END)
        self.SpNumericVal3.delete(0,END)
        self.SpNumericVal4.delete(0,END)
        self.SpNumericVal5.delete(0,END)

        self.SpChecklist1.delete(0,END)
        self.SpChecklist2.delete(0,END)
        self.SpChecklist3.delete(0,END)
        self.cboChecklist4.delete(0,END)
        self.cboChecklist5.delete(0,END)

        self.txtPrint.delete("1.0",END)

        


     def addData():
            if(len(Line.get())!=0):
                station_Database_Backend_for_production.addStnRec(Line.get(), Shift.get(), WorkstationID.get(), WorkstationName.get(), TesterID.get(), TesterName.get(),InspectionItemID.get(),\
                                                                  InspectionItemType.get(), Descripton.get(), InspectionGroupID.get(),Test1.get(), Test2.get(), Test3.get(), Test4.get(), Test5.get(),\
                                                                  NumericVal1.get(), NumericVal2.get(), NumericVal3.get(), NumericVal4.get(), NumericVal5.get(),Checklist1.get(), Checklist2.get(),\
                                                                  Checklist3.get(), Checklist4.get(), Checklist5.get())
                stationlist.delete(0,END)
                stationlist.insert(END,(Line.get(), Shift.get(), WorkstationID.get(), WorkstationName.get(), TesterID.get(), TesterName.get(),InspectionItemID.get(),\
                                                                  InspectionItemType.get(), Descripton.get(), InspectionGroupID.get(),Test1.get(), Test2.get(), Test3.get(), Test4.get(), Test5.get(),\
                                                                  NumericVal1.get(), NumericVal2.get(), NumericVal3.get(), NumericVal4.get(), NumericVal5.get(),Checklist1.get(), Checklist2.get(),\
                                                                  Checklist3.get(), Checklist4.get(), Checklist5.get()))

        
     
     def DisplayData():
            stationlist.delete(0,END)
            for row in station_Database_Backend_for_production.viewData():
             stationlist.insert(END,row,str(""))


     def StationRec(event):
            global sd
            searchStd = stationlist.curselection()[0]
            sd = stationlist.get(searchStd)

            self.cboLine.delete(0,END)
            self.cboLine.insert(END,sd[1])
            self.cboShift.delete(0,END)
            self.cboShift.insert(END,sd[2])
            self.txtWorkstationID.delete(0,END)
            self.txtWorkstationID.insert(END,sd[3])
            self.txtWorkstationName.delete(0,END)
            self.txtWorkstationName.insert(END,sd[4])
            self.txtTesterID.delete(0,END)
            self.txtTesterID.insert(END,sd[5])
            self.txtTesterName.delete(0,END)
            self.txtTesterName.insert(END,sd[6])
            self.txtInspectionItemID.delete(0,END)
            self.txtInspectionItemID.insert(END,sd[7])
            self.txtInspectionItemType.delete(0,END)
            self.txtInspectionItemType.insert(END,sd[8])
            self.txtDescripton.delete(0,END)
            self.txtDescripton.insert(END,sd[9])
            self.txtInspectionGroupID.delete(0,END)
            self.txtInspectionGroupID.insert(END,sd[10])
            
            self.cboTest1.delete(0,END)
            self.cboTest1.insert(END,sd[11])
            self.cboTest2.delete(0,END)
            self.cboTest2.insert(END,sd[12])
            self.cboTest3.delete(0,END)
            self.cboTest3.insert(END,sd[13])
            self.cboTest4.delete(0,END)
            self.cboTest4.insert(END,sd[14])
            self.cboTest5.delete(0,END)
            self.cboTest5.insert(END,sd[15])
            self.SpNumericVal1.delete(0,END)
            self.SpNumericVal1.insert(END,sd[16])
            self.SpNumericVal2.delete(0,END)
            self.SpNumericVal2.insert(END,sd[17])
            self.SpNumericVal3.delete(0,END)
            self.SpNumericVal3.insert(END,sd[18])
            self.SpNumericVal4.delete(0,END)
            self.SpNumericVal4.insert(END,sd[19])
            self.SpNumericVal5.delete(0,END)
            self.SpNumericVal5.insert(END,sd[20])
            self.SpChecklist1.delete(0,END)
            self.SpChecklist1.insert(END,sd[21])
            self.SpChecklist2.delete(0,END)
            self.SpChecklist2.insert(END,sd[22])
            self.SpChecklist3.delete(0,END)
            self.SpChecklist3.insert(END,sd[23])
            self.cboChecklist4.delete(0,END)
            self.cboChecklist4.insert(END,sd[24])
            self.cboChecklist5.delete(0,END)
            self.cboChecklist5.insert(END,sd[25])

 #In the PrintData function you can print whatever the variables you like. For demonstation right now WorkstationID, WorkstationName, Test1-5, Checklist1 is printed

     def PrintData():
            #self.txtPrint.insert(END,'\t\t Print' + "\n\n")
            addData()
            self.txtPrint.insert(END,'WorkstationID \t' + WorkstationID.get() + "\n")
            self.txtPrint.insert(END,'WorkstationName \t' + WorkstationName.get() + "\n")
            self.txtPrint.insert(END,'Test1 \t' + Test1.get() + "\n")
            self.txtPrint.insert(END,'Test2 \t' + Test2.get() + "\n")
            self.txtPrint.insert(END,'Test3 \t' + Test3.get() + "\n")
            self.txtPrint.insert(END,'Test4 \t' + Test4.get() + "\n")
            self.txtPrint.insert(END,'Test5 \t' + Test5.get() + "\n")
            self.txtPrint.insert(END,'Checklist1 \t' + Checklist1.get() + "\n")


     def DeleteData():
            if(len(Line.get())!=0):
              station_Database_Backend_for_production.deleteRec(sd[0])
              clearData()
              DisplayData()

     def searchDatabase():
            stationlist.delete(0,END)
            for row in station_Database_Backend_for_production.searchData(Line.get(), Shift.get(), WorkstationID.get(), WorkstationName.get(), TesterID.get(), TesterName.get(),InspectionItemID.get(),\
                                                                  InspectionItemType.get(), Descripton.get(), InspectionGroupID.get(),Test1.get(), Test2.get(), Test3.get(), Test4.get(), Test5.get(),\
                                                                  NumericVal1.get(), NumericVal2.get(), NumericVal3.get(), NumericVal4.get(), NumericVal5.get(),Checklist1.get(), Checklist2.get(),\
                                                                  Checklist3.get(), Checklist4.get(), Checklist5.get()):
             stationlist.insert(END,row,str(""))


     def update():
            if(len(Line.get())!=0):
             station_Database_Backend_for_production(sd[0])
            if(len(Line.get())!=0):
             station_Database_Backend_for_production(Line.get(), Shift.get(), WorkstationID.get(), WorkstationName.get(), TesterID.get(), TesterName.get(),InspectionItemID.get(),\
                                                                  InspectionItemType.get(), Descripton.get(), InspectionGroupID.get(),Test1.get(), Test2.get(), Test3.get(), Test4.get(), Test5.get(),\
                                                                  NumericVal1.get(), NumericVal2.get(), NumericVal3.get(), NumericVal4.get(), NumericVal5.get(),Checklist1.get(), Checklist2.get(),\
                                                                  Checklist3.get(), Checklist4.get(), Checklist5.get())
             stationlist.delete(0,END)
             stationlist.insert(END,(Line.get(), Shift.get(), WorkstationID.get(), WorkstationName.get(), TesterID.get(), TesterName.get(),InspectionItemID.get(),\
                                                                  InspectionItemType.get(), Descripton.get(), InspectionGroupID.get(),Test1.get(), Test2.get(), Test3.get(), Test4.get(), Test5.get(),\
                                                                  NumericVal1.get(), NumericVal2.get(), NumericVal3.get(), NumericVal4.get(), NumericVal5.get(),Checklist1.get(), Checklist2.get(),\
                                                                  Checklist3.get(), Checklist4.get(), Checklist5.get()))


     #+++++++++++++++++++++++++++++++++++Frames define+++++++++++++++++++++++++++
     #Here the Frames and below subframes(Data and print frame) are defined. 
 
     MainFrame = Frame(self.root, bd=10, width = 1350, height = 1000, relief = RIDGE) #self.TabControl1
     MainFrame.grid(padx=5, pady=10)


     TopFrame3 = Frame(MainFrame, bd=10, width = 1340, height = 500, relief = RIDGE)
     TopFrame3.grid(padx=5, pady=10)

     DataFrame2 = Frame(MainFrame, bd=10, width = 1340, height = 300, relief = RIDGE)
     DataFrame2.grid(padx=5, pady=10)
     
     DataFrame = Frame(DataFrame2, bd=10, width = 1000, height = 300, relief = RIDGE)
     DataFrame.pack(side=LEFT, pady=0)

     
     PrintFrame = Frame(DataFrame2, bd=5, width = 300, height = 200, relief = RIDGE)
     PrintFrame.pack(side=RIGHT)

     
     #+++++++++++++++++++++++++++++++++++Framesdefime+++++++++++++++++++++++++++
     #Here above subframes are defined.Boolean Frame is for Test 1-5, NumericValueFrame is for Numeric value 1-5, ChecklistFrame is for Checklist 1-5
     
     RightFrame = Frame(TopFrame3, bd=5, width = 1340, height = 400,padx=2, bg="cadetblue", relief = RIDGE)
     RightFrame.pack(side=RIGHT, pady=0)
     InspectionItemFrame = Frame(RightFrame, bd=5, width = 600, height = 180,padx=4, relief = RIDGE)
     InspectionItemFrame.pack(side=TOP, pady=2)

     RightFrame2 = Frame(RightFrame, bd=5, width = 600, height = 180,padx=2, bg="cadetblue", relief = RIDGE)
     RightFrame2.pack(side=TOP)
     BooleanFrame = Frame(RightFrame2, bd=5, width = 300, height = 170,padx=2, relief = RIDGE) #StudentStatus
     BooleanFrame.pack(side=LEFT)
     NumericValueFrame = Frame(RightFrame2, bd=5, width = 300, height = 170,padx=2, relief = RIDGE)
     NumericValueFrame.pack(side=RIGHT)
     ChecklistFrame = Frame(RightFrame2, bd=5, width = 300, height = 170,padx=2, relief = RIDGE)
     ChecklistFrame.pack(side=RIGHT)

     ButtonFrame = Frame(RightFrame, bd=5, width = 320, height = 50,padx=3, relief = RIDGE)
     ButtonFrame.pack(side=LEFT, pady=3)

     LeftFrame2 = Frame(TopFrame3, bd=5, width = 300, height = 400,padx=2, bg="cadetblue", relief = RIDGE)
     LeftFrame2.pack(side=LEFT, pady=5)
     LineFrame = Frame(LeftFrame2, bd=5, width = 280, height = 50,padx=2, relief = RIDGE)
     LineFrame.pack(side=TOP, pady=3)
     CalenderFrame = Frame(LeftFrame2, bd=5, width = 200, height = 50,padx=3, relief = RIDGE)
     CalenderFrame.pack(side=LEFT)



 


#+++++++++++++++++++++++++++++++++++LineFrames+++++++++++++++++++++++++++
     #This portion is for definiing the upper left frame labels. This is for taking input for Line, Shift, WorkstationID, Workstationname, Tester ID, TesterName.
     #cbo statnd for defining combobox, you can change the oprtions according to your need.
     #lbl stands for label.
     #txt stand for textbox

     
     self.lblLine = Label(LineFrame, font=('arial',12,'bold'), text='Line', bd=7, anchor='w', justify=LEFT)
     self.lblLine.grid(row=0,column=0, sticky = W, padx=5, pady=5)
     self.cboLine = ttk.Combobox(LineFrame,textvariable = Line, width = 23, font=('arial',12,'bold'), state = 'readonly')
     self.cboLine['value'] = ('','Star','Nimbus','Vantage','Zeus')
     self.cboLine.current(0)
     self.cboLine.grid(row=0,column=1)

     self.lblShift = Label(LineFrame, font=('arial',12,'bold'), text='Shift', bd=7, justify=LEFT)
     self.lblShift.grid(row=1,column=0, sticky = W, padx=5)
     self.cboShift = ttk.Combobox(LineFrame,textvariable = Shift, width = 23, font=('arial',12,'bold'), state = 'readonly')
     self.cboShift['value'] = ('','Day','Swing','Graveyard')
     self.cboShift.current(0)
     self.cboShift.grid(row=1,column=1)

     self.lblWorkstationID = Label(LineFrame, font=('arial',12,'bold'), text='Workstation ID', bd=5)
     self.lblWorkstationID.grid(row=2,column=0, sticky = W, padx=5)
     self.txtWorkstationID = Entry(LineFrame, font=('arial',12,'bold'),bd=5, width = 25, textvariable = WorkstationID)
     self.txtWorkstationID.grid(row=2,column=1)

     self.lblWorkstationName = Label(LineFrame, font=('arial',12,'bold'), text='Workstation Name', bd=5)
     self.lblWorkstationName.grid(row=3,column=0, sticky = W, padx=5)
     self.txtWorkstationName = Entry(LineFrame, font=('arial',12,'bold'),bd=5, width = 25, textvariable = WorkstationName)
     self.txtWorkstationName.grid(row=3,column=1)
     
     self.lblTesterID = Label(LineFrame, font=('arial',12,'bold'), text='Tester ID', bd=5)
     self.lblTesterID.grid(row=4,column=0, sticky = W, padx=5)
     self.txtTesterID = Entry(LineFrame, font=('arial',12,'bold'),bd=5, width = 25, textvariable = TesterID)
     self.txtTesterID.grid(row=4,column=1)

     self.lblTesterName = Label(LineFrame, font=('arial',12,'bold'), text='Tester Name', bd=5)
     self.lblTesterName.grid(row=5,column=0, sticky = W, padx=5)
     self.txtTesterName = Entry(LineFrame, font=('arial',12,'bold'),bd=5, width = 25, textvariable = TesterName)
     self.txtTesterName.grid(row=5,column=1)
     
 


    

#+++++++++++++++++++++++++++++++++++++++++++Inspection ITEM FRAME++++++++++
     #This portion is for definiing the upper right frame labels. This is for taking input for Inspection Item ID, Type, Description, Inspection group ID.
     #lbl stands for label.
     #txt stand for textbox
     
     self.lblInspectionItemID = Label(InspectionItemFrame, font=('arial',12,'bold'), text='Inspec. Item ID', bd=6)
     self.lblInspectionItemID.grid(row=0,column=0, sticky = W, padx=5)
     self.txtInspectionItemID = Entry(InspectionItemFrame, font=('arial',12,'bold'),bd=5, width = 52, textvariable = InspectionItemID)
     self.txtInspectionItemID.grid(row=0,column=1)

     self.lblInspectionItemType = Label(InspectionItemFrame, font=('arial',12,'bold'), text='Inspec. Item Type', bd=6)
     self.lblInspectionItemType.grid(row=1,column=0, sticky = W, padx=5)
     self.txtInspectionItemType = Entry(InspectionItemFrame, font=('arial',12,'bold'),bd=5, width = 52, textvariable = InspectionItemType)
     self.txtInspectionItemType.grid(row=1,column=1)  

     self.lblDescripton= Label(InspectionItemFrame, font=('arial',12,'bold'), text='Descripton', bd=6)
     self.lblDescripton.grid(row=2,column=0, sticky = W, padx=5)
     self.txtDescripton = Entry(InspectionItemFrame, font=('arial',12,'bold'),bd=5, width = 52, textvariable = Descripton)
     self.txtDescripton.grid(row=2,column=1)

     self.lblInspectionGroupID= Label(InspectionItemFrame, font=('arial',12,'bold'), text='Inspec. GroupID', bd=6)
     self.lblInspectionGroupID.grid(row=3,column=0, sticky = W, padx=5)
     self.txtInspectionGroupID = Entry(InspectionItemFrame, font=('arial',12,'bold'),bd=5, width = 52, textvariable = InspectionGroupID)
     self.txtInspectionGroupID.grid(row=3,column=1)

     

#+++++++++++++++++++++++++++++++++++++++++++TestFrame++++++++++
     #This portion is for definiing the test frame labels. This is for taking input for test1-5.
     #lbl stands for label.
     #txt stands for textbox
     #cbo stands for combobox
     
     self.lblTest1 = Label(BooleanFrame, font=('arial',12,'bold'), text='Test 1', bd=6,)
     self.lblTest1.grid(row=0,column=0, sticky = W)
     self.cboTest1 = ttk.Combobox(BooleanFrame,textvariable = Test1, width = 14, font=('arial',12,'bold'), state = 'readonly')
     self.cboTest1['values'] = ('pass ','fail')
     self.cboTest1.current(0)
     self.cboTest1.grid(row=0,column=1, pady=8)

     self.lblTest2 = Label(BooleanFrame, font=('arial',12,'bold'), text='Test 2', bd=6,)
     self.lblTest2.grid(row=1,column=0, sticky = W)
     self.cboTest2 = ttk.Combobox(BooleanFrame,textvariable = Test2, width = 14, font=('arial',12,'bold'), state = 'readonly')
     self.cboTest2['values'] = ('No','Yes')
     self.cboTest2.current(0)
     self.cboTest2.grid(row=1,column=1, pady=8)


     self.lblTest3= Label(BooleanFrame, font=('arial',12,'bold'), text='Test 3', bd=6,)
     self.lblTest3.grid(row=2,column=0, sticky = W)
     self.cboTest3 = ttk.Combobox(BooleanFrame,textvariable = Test3, width = 14, font=('arial',12,'bold'), state = 'readonly')
     self.cboTest3['values'] = ('No','Yes')
     self.cboTest3.current(0)
     self.cboTest3.grid(row=2,column=1, pady=8)

     self.lblTest4 = Label(BooleanFrame, font=('arial',12,'bold'), text='Test 4', bd=6,)
     self.lblTest4.grid(row=3,column=0, sticky = W)
     self.cboTest4 = ttk.Combobox(BooleanFrame,textvariable = Test4, width = 14, font=('arial',12,'bold'), state = 'readonly')
     self.cboTest4['values'] = ('No','Yes')
     self.cboTest4.current(0)
     self.cboTest4.grid(row=3,column=1, pady=8)

     self.lblTest5 = Label(BooleanFrame, font=('arial',12,'bold'), text='Test 5', bd=6,)
     self.lblTest5.grid(row=4,column=0, sticky = W)
     self.cboTest5 = ttk.Combobox(BooleanFrame,textvariable = Test5, width = 14, font=('arial',12,'bold'), state = 'readonly')
     self.cboTest5['values'] = ('No','Yes')
     self.cboTest5.current(0)
     self.cboTest5.grid(row=4,column=1, pady=8)

#+++++++++++++++++++++++++++++++++++++++++++NumericValueFrame++++++++++
     #This portion is for definiing the NumericValueFrame frame labels. This is for taking input for NumericValue1-5.
     #lbl stands for label.
     #Sp stands for spinbox
     #In the spin box value range have been set from 0 to 20. it can be set according to user need
     
     self.lblNumericVal1 = Label(NumericValueFrame, font=('arial',12,'bold'), text='Numeric Value1', bd=10)
     self.lblNumericVal1.grid(row=0,column=0, sticky = W)
     self.SpNumericVal1 = ttk.Spinbox(NumericValueFrame, from_=0, to=20,textvariable = NumericVal1, width = 9, font=('arial',12,'bold'))
     self.SpNumericVal1.grid(row=0,column=1, pady=5)

     self.lblNumericVal2 = Label(NumericValueFrame, font=('arial',12,'bold'), text='Numeric Value2', bd=10)
     self.lblNumericVal2.grid(row=1,column=0, sticky = W)
     self.SpNumericVal2  = ttk.Spinbox(NumericValueFrame, from_=0, to=20,textvariable = NumericVal2, width = 9, font=('arial',12,'bold'))
     self.SpNumericVal2.grid(row=1,column=1, pady=5)

     self.lblNumericVal3 = Label(NumericValueFrame, font=('arial',12,'bold'), text='Numeric Value3', bd=10)
     self.lblNumericVal3.grid(row=2,column=0, sticky = W)
     self.SpNumericVal3  = ttk.Spinbox(NumericValueFrame, from_=0, to=20,textvariable = NumericVal3, width = 9, font=('arial',12,'bold'))
     self.SpNumericVal3.grid(row=2,column=1, pady=5)

     self.lblNumericVal4 = Label(NumericValueFrame, font=('arial',12,'bold'), text='Numeric Value4', bd=10)
     self.lblNumericVal4.grid(row=3,column=0, sticky = W)
     self.SpNumericVal4  = ttk.Spinbox(NumericValueFrame, from_=0, to=20,textvariable = NumericVal4, width = 9, font=('arial',12,'bold'))
     self.SpNumericVal4.grid(row=3,column=1, pady=5)

     self.lblNumericVal5 = Label(NumericValueFrame, font=('arial',12,'bold'), text='Numeric Value5', bd=10)
     self.lblNumericVal5.grid(row=4,column=0, sticky = W)
     self.SpNumericVal5  = ttk.Spinbox(NumericValueFrame, from_=0, to=20,textvariable = NumericVal5, width = 9, font=('arial',12,'bold'))
     self.SpNumericVal5.grid(row=4,column=1, pady=5)


#+++++++++++++++++++++++++++++++++++++++++++ChecklistFrame++++++++++
     #This portion is for definiing the ChecklistFram labels. This is for taking input for ChecklistFrame1-5.
     #lbl stands for label.
     #Sp stands for spinbox. total 3 spinbox defined here
     #cbo stands for combobox. total 2 combobox defined here.
     #In the spin box value range have been set from 0 to 20. it can be set according to user need
     
     self.lblChecklist1 = Label(ChecklistFrame, font=('arial',12,'bold'), text='Checklist1', bd=10)
     self.lblChecklist1.grid(row=0,column=0, sticky = W)
     self.SpChecklist1 = ttk.Spinbox(ChecklistFrame, from_=0, to=20,textvariable = Checklist1, width = 9, font=('arial',12,'bold'))
     self.SpChecklist1.grid(row=0,column=1, pady=5)

     self.lblChecklist2 = Label(ChecklistFrame, font=('arial',12,'bold'), text='Checklist 2', bd=10)
     self.lblChecklist2.grid(row=1,column=0, sticky = W)
     self.SpChecklist2  = ttk.Spinbox(ChecklistFrame, from_=0, to=20,textvariable = Checklist2, width = 9, font=('arial',12,'bold'))
     self.SpChecklist2.grid(row=1,column=1, pady=5)

     self.lblChecklist3 = Label(ChecklistFrame, font=('arial',12,'bold'), text='Checklist 3', bd=10)
     self.lblChecklist3.grid(row=2,column=0, sticky = W)
     self.SpChecklist3  = ttk.Spinbox(ChecklistFrame, from_=0, to=20,textvariable = Checklist3, width = 9, font=('arial',12,'bold'))
     self.SpChecklist3.grid(row=2,column=1, pady=5)

     self.lblChecklist4 = Label(ChecklistFrame, font=('arial',12,'bold'), text='Checklist 4', bd=6,)
     self.lblChecklist4.grid(row=3,column=0, sticky = W)
     self.cboChecklist4 = ttk.Combobox(ChecklistFrame,textvariable = Checklist4, width = 14, font=('arial',12,'bold'), state = 'readonly')
     self.cboChecklist4['values'] = ('Fail','Pass')
     self.cboChecklist4.current(0)
     self.cboChecklist4.grid(row=3,column=1, pady=8)

     self.lblChecklist5 = Label(ChecklistFrame, font=('arial',12,'bold'), text='Checklist 5', bd=6,)
     self.lblChecklist5.grid(row=4,column=0, sticky = W)
     self.cboChecklist5 = ttk.Combobox(ChecklistFrame,textvariable = Checklist5, width = 14, font=('arial',12,'bold'), state = 'readonly')
     self.cboChecklist5['values'] = ('Fail','Pass')
     self.cboChecklist5.current(0)
     self.cboChecklist5.grid(row=4,column=1, pady=8)

#+++++++++++++++++++++++++++++calender frame+++++++++++++++++++++++
     #this is for calender. 
     def getSelectedDate():
         nowDate =cal.get_date()
         self.ResultDate.set(nowDate)
         
     cal = Calendar(CalenderFrame, selectmode = "day", date_pattern ='dd-mm-yyyy', font=('arial',9,'bold'), padx=100)
     cal.grid(row=0,column=0)
    


     

     #==========ListBox & Scrollbar Widget ======
     #this scorrlbar is for botom left display data frame. 

     scrollbar = Scrollbar(DataFrame)
     scrollbar.grid(row=0, column=1, sticky='ns')

     stationlist = Listbox(DataFrame, width=80, height=10, font=('arial',12,'bold'), yscrollcommand=scrollbar.set)
     stationlist.bind('<<ListboxSelect>>',StationRec)
     stationlist.grid(row=0, column=0, padx=8)
     scrollbar.config(command = stationlist.yview)

     #==========PrintFrame ======
     #this scorrlbar is for botom right print frame. 
     self.txtPrint = Text(PrintFrame, width=50, height=10, font=('arial',12,'bold'))
     self.txtPrint.grid(row=0, column=0)
     #self.txtPrint.config(command = PrintData)

     #+++++++++++++++++++++++++++++++++ButtonFrame++++++
     #this portion is for defining the button. Total 8 button here. search and update button hs been disabled. Rest are working properly. 

     self.btnAddData = Button(ButtonFrame, text="Add New", font=('arial', 15, 'bold'), height=1,width=7, bd=4, command=PrintData)
     self.btnAddData.grid(row=0, column=0)
        
     self.btnDisplayData = Button(ButtonFrame, text="Display", font=('arial', 15, 'bold'), height=1,width=6, bd=4, command=DisplayData)
     self.btnDisplayData.grid(row=0, column=1)
        
     self.btnClearData = Button(ButtonFrame, text="Clear", font=('arial', 15, 'bold'), height=1,width=6, bd=4, command=clearData)
     self.btnClearData.grid(row=0, column=2)
        
     self.btnDeleteData = Button(ButtonFrame, text="Delete", font=('arial', 15, 'bold'), height=1,width=6, bd=4, command=DeleteData)
     self.btnDeleteData.grid(row=0, column=3)
        
     self.btnSearchData = Button(ButtonFrame, text="Search", font=('arial', 15, 'bold'), height=1,width=6, bd=4) # command=searchDatabase have been commented out as the functionality wasn't working
     self.btnSearchData.grid(row=0, column=4)
        
     self.btnUpdateData = Button(ButtonFrame, text="Update", font=('arial', 15, 'bold'), height=1,width=6, bd=4) #, command = update  have been commented out as the functionality wasn't working
     self.btnUpdateData.grid(row=0, column=5)
        
     self.btnExit = Button(ButtonFrame, text="Exit", font=('arial', 15, 'bold'), height=1,width=6, bd=4, command=iExit)
     self.btnExit.grid(row=0, column=6)

     self.btnPrint = Button(ButtonFrame, text="Print", font=('arial', 15, 'bold'), height=1,width=6, bd=4, command=iPrint)
     self.btnPrint.grid(row=0, column=7)

        



     

     

if __name__ == '__main__':
    root = Tk()
    application = stationRecords(root)
    root.mainloop()





















