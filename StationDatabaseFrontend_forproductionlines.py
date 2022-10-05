from tkinter import*

from tkcalendar import*
import pymysql
from tkinter import ttk
import random
import tkinter.messagebox
import datetime
import time
import tkinter.ttk as tkrtk
import tkinter as tkr

class studentRecords:

    def __init__(self,root):
     self.root = root
     self.root.title("Student Record System")
     self.root.geometry("1350x800+0+0")

     notebook = ttk.Notebook(self.root)
     self.TabControl1 = ttk.Frame(notebook)
     self.TabControl2 = ttk.Frame(notebook)
     #self.TabControl3 = ttk.Frame(notebook)
     notebook.add(self.TabControl1, text='School System')
     notebook.add(self.TabControl2, text='Student Details')

     notebook.grid()
    #+++++++++++++++++++++++++++++++++++Variables+++++++++++++++++++++++++++
     self.Line = StringVar() #StudentID
     self.Shift = StringVar() #Firstname
     self.WorkstationID = StringVar() #Surname
     self.WorkstationName = StringVar() #Address
     self.TesterID = StringVar() #PostCode
     self.TesterName = StringVar() #TesterName

     self.InspectionItemID = StringVar() #Course
     self.InspectionItemType = StringVar() # CourseCode
     self.Descripton = StringVar() #Faculty 
     self.InspectionGroupID = StringVar() #Dean
     
     self.Test1 = StringVar() #HomeStudent
     self.Test2 = StringVar() #Oversea
     self.Test3 = StringVar() #Accomodation
     self.Test4 = StringVar() #ExchangeProg
     self.Test5 = StringVar() #Scholarship

     self.NumericVal1 = StringVar() #BA
     self.NumericVal2 = StringVar() #BSc
     self.NumericVal3= StringVar() #MA
     self.NumericVal4 = StringVar() #MSc
     self.NumericVal5 = StringVar() #Phd

     self.Checklist1 = StringVar()
     self.Checklist2 = StringVar()
     self.Checklist3 = StringVar()
     self.Checklist4 = StringVar()
     self.Checklist5 = StringVar()


     self.English = StringVar()
     self.Games = StringVar()
     self.Animation = StringVar()
     self.Database = StringVar()
     self.Maths = StringVar()
     self.AddMaths = StringVar()
     self.Physics = StringVar()
     self.Media = StringVar()
     self.GraphicD = StringVar()

     self.ScoreMaths = StringVar()
     self.ScoreEnglish = StringVar()
     self.ScoreBiology = StringVar()
     self.ScoreComputing = StringVar()
     self.ExamNo = StringVar()
     self.ScoreChemistry = StringVar()
     self.ScorePhysics = StringVar()
     self.ScoreAddMaths = StringVar()
     self.ScoreBusiness = StringVar()
     self.TotalScore = StringVar()
     self.Average = StringVar()
     self.Ranking = StringVar()
     self.Taxperiod = StringVar()
     self.iDate = StringVar()

     self.Module1 = StringVar()
     self.Module2 = StringVar()
     self.Module3 = StringVar()
     self.Module4 = StringVar()
     self.Module5 = StringVar()
     self.Module6 = StringVar()
     self.Module7 = StringVar()
     self.Module8 = StringVar()
     self.Ranking = StringVar()
     self.TotalScore = StringVar()
     self.ResultDate = StringVar()

     self.Subject1 = StringVar()
     self.Subject2 = StringVar()
     self.Subject3 = StringVar()
     self.Subject4 = StringVar()
     self.Subject5 = StringVar()
     self.Subject6 = StringVar()
     self.Subject7 = StringVar()
     self.Subject8 = StringVar()

     #+++++++++++++++++++++++++++++++++++Frames+++++++++++++++++++++++++++

     MainFrame = Frame(self.TabControl1, bd=10, width = 1350, height = 700, relief = RIDGE)
     MainFrame.grid(padx=5, pady=10)

     Tab2Frame = Frame(self.TabControl2, bd=10, width = 1350, height = 700, relief = RIDGE)
     Tab2Frame.grid(padx=5, pady=10)

     TopFrame3 = Frame(MainFrame, bd=10, width = 1340, height = 500, relief = RIDGE)
     TopFrame3.grid(padx=5, pady=10)

     
#+++++++++++++++++++++++++++++++++++Frames+++++++++++++++++++++++++++
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
     CalenderFrame = Frame(LeftFrame2, bd=5, width = 280, height = 50,padx=3, relief = RIDGE)
     CalenderFrame.pack(side=TOP)


 


#+++++++++++++++++++++++++++++++++++Frames+++++++++++++++++++++++++++
     self.lblLine = Label(LineFrame, font=('arial',12,'bold'), text='Line', bd=7, anchor='w', justify=LEFT)
     self.lblLine.grid(row=0,column=0, sticky = W, padx=5, pady=5)
     self.cboLine = ttk.Combobox(LineFrame,textvariable = self.Line, width = 23, font=('arial',12,'bold'), state = 'readonly')
     self.cboLine['value'] = ('','Star','Nimbus','Vantage','Zeus')
     self.cboLine.current(0)
     self.cboLine.grid(row=0,column=1)

     self.lblShift = Label(LineFrame, font=('arial',12,'bold'), text='Shift', bd=7, justify=LEFT)
     self.lblShift.grid(row=1,column=0, sticky = W, padx=5)
     self.cboShift = ttk.Combobox(LineFrame,textvariable = self.Shift, width = 23, font=('arial',12,'bold'), state = 'readonly')
     self.cboShift['value'] = ('','Day','Swing','Graveyard')
     self.cboShift.current(0)
     self.cboShift.grid(row=1,column=1)

     self.lblWorkstationID = Label(LineFrame, font=('arial',12,'bold'), text='Workstation ID', bd=5)
     self.lblWorkstationID.grid(row=2,column=0, sticky = W, padx=5)
     self.txtWorkstationID = Entry(LineFrame, font=('arial',12,'bold'),bd=5, width = 25, textvariable = self.WorkstationID)
     self.txtWorkstationID.grid(row=2,column=1)

     self.lblWorkstationName = Label(LineFrame, font=('arial',12,'bold'), text='Workstation Name', bd=5)
     self.lblWorkstationName.grid(row=3,column=0, sticky = W, padx=5)
     self.txtWorkstationName = Entry(LineFrame, font=('arial',12,'bold'),bd=5, width = 25, textvariable = self.WorkstationName)
     self.txtWorkstationName.grid(row=3,column=1)
     
     self.lblTesterID = Label(LineFrame, font=('arial',12,'bold'), text='Tester ID', bd=5)
     self.lblTesterID.grid(row=4,column=0, sticky = W, padx=5)
     self.txtTesterID = Entry(LineFrame, font=('arial',12,'bold'),bd=5, width = 25, textvariable = self.TesterID)
     self.txtTesterID.grid(row=4,column=1)

     self.lblTesterName = Label(LineFrame, font=('arial',12,'bold'), text='Tester Name', bd=5)
     self.lblTesterName.grid(row=5,column=0, sticky = W, padx=5)
     self.txtTesterName = Entry(LineFrame, font=('arial',12,'bold'),bd=5, width = 25, textvariable = self.TesterName)
     self.txtTesterName.grid(row=5,column=1)
     
 
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    

#+++++++++++++++++++++++++++++++++++++++++++self.course++++++++++
     self.lblInspectionItemID = Label(InspectionItemFrame, font=('arial',12,'bold'), text='Inspec. Item ID', bd=6)
     self.lblInspectionItemID.grid(row=0,column=0, sticky = W, padx=5)
     self.txtInspectionItemID = Entry(InspectionItemFrame, font=('arial',12,'bold'),bd=5, width = 52, textvariable = self.InspectionItemID)
     self.txtInspectionItemID.grid(row=0,column=1)

     self.lblInspectionItemType = Label(InspectionItemFrame, font=('arial',12,'bold'), text='Inspec. Item Type', bd=6)
     self.lblInspectionItemType.grid(row=1,column=0, sticky = W, padx=5)
     self.txtInspectionItemType = Entry(InspectionItemFrame, font=('arial',12,'bold'),bd=5, width = 52, textvariable = self.InspectionItemType)
     self.txtInspectionItemType.grid(row=1,column=1)  

     self.lblDescripton= Label(InspectionItemFrame, font=('arial',12,'bold'), text='Descripton', bd=6)
     self.lblDescripton.grid(row=2,column=0, sticky = W, padx=5)
     self.txtDescripton = Entry(InspectionItemFrame, font=('arial',12,'bold'),bd=5, width = 52, textvariable = self.Descripton)
     self.txtDescripton.grid(row=2,column=1)

     self.lblInspectionGroupID= Label(InspectionItemFrame, font=('arial',12,'bold'), text='Inspec. GroupID', bd=6)
     self.lblInspectionGroupID.grid(row=3,column=0, sticky = W, padx=5)
     self.txtInspectionGroupID = Entry(InspectionItemFrame, font=('arial',12,'bold'),bd=5, width = 52, textvariable = self.InspectionGroupID)
     self.txtInspectionGroupID.grid(row=3,column=1)

     

#+++++++++++++++++++++++++++++++++++++++++++StudentStatusFrame++++++++++
     
     self.lblTest1 = Label(BooleanFrame, font=('arial',12,'bold'), text='Test 1', bd=6,)
     self.lblTest1.grid(row=0,column=0, sticky = W)
     self.cboTest1 = ttk.Combobox(BooleanFrame,textvariable = self.Test1, width = 14, font=('arial',12,'bold'), state = 'readonly')
     self.cboTest1['values'] = ('No','Yes')
     self.cboTest1.current(0)
     self.cboTest1.grid(row=0,column=1, pady=8)

     self.lblTest2 = Label(BooleanFrame, font=('arial',12,'bold'), text='Test 2', bd=6,)
     self.lblTest2.grid(row=1,column=0, sticky = W)
     self.cboTest2 = ttk.Combobox(BooleanFrame,textvariable = self.Test2, width = 14, font=('arial',12,'bold'), state = 'readonly')
     self.cboTest2['values'] = ('No','Yes')
     self.cboTest2.current(0)
     self.cboTest2.grid(row=1,column=1, pady=8)


     self.lblTest3= Label(BooleanFrame, font=('arial',12,'bold'), text='Test 3', bd=6,)
     self.lblTest3.grid(row=2,column=0, sticky = W)
     self.cboTest3 = ttk.Combobox(BooleanFrame,textvariable = self.Test3, width = 14, font=('arial',12,'bold'), state = 'readonly')
     self.cboTest3['values'] = ('No','Yes')
     self.cboTest3.current(0)
     self.cboTest3.grid(row=2,column=1, pady=8)

     self.lblTest4 = Label(BooleanFrame, font=('arial',12,'bold'), text='Test 4', bd=6,)
     self.lblTest4.grid(row=3,column=0, sticky = W)
     self.cboTest4 = ttk.Combobox(BooleanFrame,textvariable = self.Test4, width = 14, font=('arial',12,'bold'), state = 'readonly')
     self.cboTest4['values'] = ('No','Yes')
     self.cboTest4.current(0)
     self.cboTest4.grid(row=3,column=1, pady=8)

     self.lblTest5 = Label(BooleanFrame, font=('arial',12,'bold'), text='Test 5', bd=6,)
     self.lblTest5.grid(row=4,column=0, sticky = W)
     self.cboTest5 = ttk.Combobox(BooleanFrame,textvariable = self.Test5, width = 14, font=('arial',12,'bold'), state = 'readonly')
     self.cboTest5['values'] = ('No','Yes')
     self.cboTest5.current(0)
     self.cboTest5.grid(row=4,column=1, pady=8)

#+++++++++++++++++++++++++++++++++++++++++++NumericValueFrame++++++++++   
     self.lblNumericVal1 = Label(NumericValueFrame, font=('arial',12,'bold'), text='Numeric Value1', bd=10)
     self.lblNumericVal1.grid(row=0,column=0, sticky = W)
     self.SpNumericVal1 = ttk.Spinbox(NumericValueFrame, from_=0, to=20,textvariable = self.NumericVal1, width = 9, font=('arial',12,'bold'))
     self.SpNumericVal1.grid(row=0,column=1, pady=5)

     self.lblNumericVal2 = Label(NumericValueFrame, font=('arial',12,'bold'), text='Numeric Value2', bd=10)
     self.lblNumericVal2.grid(row=1,column=0, sticky = W)
     self.SpNumericVal2  = ttk.Spinbox(NumericValueFrame, from_=0, to=20,textvariable = self.NumericVal2, width = 9, font=('arial',12,'bold'))
     self.SpNumericVal2.grid(row=1,column=1, pady=5)

     self.lblNumericVal3 = Label(NumericValueFrame, font=('arial',12,'bold'), text='Numeric Value3', bd=10)
     self.lblNumericVal3.grid(row=2,column=0, sticky = W)
     self.SpNumericVal3  = ttk.Spinbox(NumericValueFrame, from_=0, to=20,textvariable = self.NumericVal3, width = 9, font=('arial',12,'bold'))
     self.SpNumericVal3.grid(row=2,column=1, pady=5)

     self.lblNumericVal4 = Label(NumericValueFrame, font=('arial',12,'bold'), text='Numeric Value4', bd=10)
     self.lblNumericVal4.grid(row=3,column=0, sticky = W)
     self.SpNumericVal4  = ttk.Spinbox(NumericValueFrame, from_=0, to=20,textvariable = self.NumericVal4, width = 9, font=('arial',12,'bold'))
     self.SpNumericVal4.grid(row=3,column=1, pady=5)

     self.lblNumericVal5 = Label(NumericValueFrame, font=('arial',12,'bold'), text='Numeric Value5', bd=10)
     self.lblNumericVal5.grid(row=4,column=0, sticky = W)
     self.SpNumericVal5  = ttk.Spinbox(NumericValueFrame, from_=0, to=20,textvariable = self.NumericVal5, width = 9, font=('arial',12,'bold'))
     self.SpNumericVal5.grid(row=4,column=1, pady=5)


#+++++++++++++++++++++++++++++++++++++++++++ChecklistFrame++++++++++   
     self.lblChecklist1 = Label(ChecklistFrame, font=('arial',12,'bold'), text='Checklist1', bd=10)
     self.lblChecklist1.grid(row=0,column=0, sticky = W)
     self.SpChecklist1 = ttk.Spinbox(ChecklistFrame, from_=0, to=20,textvariable = self.Checklist1, width = 9, font=('arial',12,'bold'))
     self.SpChecklist1.grid(row=0,column=1, pady=5)

     self.lblChecklist2 = Label(ChecklistFrame, font=('arial',12,'bold'), text='Checklist 2', bd=10)
     self.lblChecklist2.grid(row=1,column=0, sticky = W)
     self.SpChecklist2  = ttk.Spinbox(ChecklistFrame, from_=0, to=20,textvariable = self.Checklist2, width = 9, font=('arial',12,'bold'))
     self.SpChecklist2.grid(row=1,column=1, pady=5)

     self.lblChecklist3 = Label(ChecklistFrame, font=('arial',12,'bold'), text='Checklist 3', bd=10)
     self.lblChecklist3.grid(row=2,column=0, sticky = W)
     self.SpChecklist3  = ttk.Spinbox(ChecklistFrame, from_=0, to=20,textvariable = self.Checklist3, width = 9, font=('arial',12,'bold'))
     self.SpChecklist3.grid(row=2,column=1, pady=5)

     self.lblChecklist4 = Label(ChecklistFrame, font=('arial',12,'bold'), text='Checklist 4', bd=6,)
     self.lblChecklist4.grid(row=3,column=0, sticky = W)
     self.cboChecklist4 = ttk.Combobox(ChecklistFrame,textvariable = self.Checklist4, width = 14, font=('arial',12,'bold'), state = 'readonly')
     self.cboChecklist4['values'] = ('Fail','Pass')
     self.cboChecklist4.current(0)
     self.cboChecklist4.grid(row=3,column=1, pady=8)

     self.lblChecklist5 = Label(ChecklistFrame, font=('arial',12,'bold'), text='Checklist 5', bd=6,)
     self.lblChecklist5.grid(row=4,column=0, sticky = W)
     self.cboChecklist5 = ttk.Combobox(ChecklistFrame,textvariable = self.Checklist5, width = 14, font=('arial',12,'bold'), state = 'readonly')
     self.cboChecklist5['values'] = ('Fail','Pass')
     self.cboChecklist5.current(0)
     self.cboChecklist5.grid(row=4,column=1, pady=8)

#+++++++++++++++++++++++++++++calender frame+++++++++++++++++++++++
     def getSelectedDate():
         nowDate =cal.get_date()
         self.ResultDate.set(nowDate)
         
     cal = Calendar(CalenderFrame, selectmode = "day", date_pattern ='dd-mm-yyyy', font=('arial',9,'bold'), padx=100)
     cal.grid(row=0,column=0)
    
     
#+++++++++++++++++++++++++++Unit No++++++++++++++++++++++

     



#++++++++++++++++++++++++++++++++++++++++++++++


#+++++++++++++++++++++++++++++++++Subject++++++

     

     #+++++++++++++++++++++++++++++++++ButtonFrame++++++

     

     #+++++++++++++++++++++++++++++++++ButtonFrame++++++

     self.btnAddNewStudent = Button(ButtonFrame, pady=1,padx=11, text="Add New", font=('arial', 16, 'bold'),bg='cadetblue', height=1,width=5, bd=4).grid(row=0, column=1, padx=1)
        
     self.btnUpdate = Button(ButtonFrame, pady=1,padx=11, text="Update", font=('arial', 16, 'bold'),bg='cadetblue', height=1,width=5, bd=4).grid(row=0, column=2, padx=1)

     self.btnDelete = Button(ButtonFrame, pady=1,padx=11, text="Delete", font=('arial', 16, 'bold'),bg='cadetblue', height=1,width=5, bd=4).grid(row=0, column=3, padx=1)

     self.btnReset = Button(ButtonFrame, pady=1,padx=11, text="Reset", font=('arial', 16, 'bold'),bg='cadetblue', height=1,width=5, bd=4).grid(row=0, column=4, padx=1)
        
     self.btnResult = Button(ButtonFrame, pady=1,padx=11, text="Result", font=('arial', 16, 'bold'),bg='cadetblue', height=1,width=5, bd=4).grid(row=0, column=5, padx=1)

     self.btnExit = Button(ButtonFrame, pady=1,padx=11, text="Exit", font=('arial', 16, 'bold'),bg='cadetblue', height=1,width=5, bd=4).grid(row=0, column=6, padx=1)  

        



     

     

if __name__ == '__main__':
    root = Tk()
    application = studentRecords(root)
    root.mainloop()





















