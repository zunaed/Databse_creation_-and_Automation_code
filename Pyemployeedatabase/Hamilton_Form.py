from tkinter import*
from tkinter import ttk
import random
import tkinter.messagebox
import datetime
import time
import tempfile, os



class Employee:

    def __init__(self, root):
        self.root = root
        self.root.title("Employee Database management system")
        self.root.geometry("1350x800+0+0")
        self.root.configure(bg = 'gainsboro')

        MainFrame = Frame(self.root, bd = 10, width= 1350, height=700, relief = RIDGE)
        MainFrame.grid()
        
        TopFrame1 = Frame(MainFrame, bd = 7, width= 1340, height=50, relief = RIDGE)
        TopFrame1.grid(row =2, column = 0)
        
        TopFrame2 = Frame(MainFrame, bd = 7, width= 1340, height=100, relief = RIDGE)
        TopFrame2.grid(row =1, column = 0)
        
        TopFrame3 = Frame(MainFrame, bd = 7, width= 1340, height=500, relief = RIDGE)
        TopFrame3.grid(row =0, column = 0)

        LeftFrame = Frame(TopFrame3, bd = 5, width= 1340, height=400, padx=2, bg="gainsboro", relief = RIDGE)
        LeftFrame.pack(side = LEFT)
        LeftFrame1 = Frame(LeftFrame, bd = 5, width= 600, height=180, padx=4, pady=4, bg="gainsboro", relief = RIDGE)
        LeftFrame1.pack(side = TOP)
        
        LeftFrame2 = Frame(LeftFrame, bd = 5, width= 600, height=180, padx=2, bg="gainsboro", relief = RIDGE)
        LeftFrame2.pack(side = TOP)
        LeftFrame2Left = Frame(LeftFrame2, bd = 5, width= 300, height=170, padx=2, bg="gainsboro", relief = RIDGE)
        LeftFrame2Left.pack(side = LEFT)
        LeftFrame2Right = Frame(LeftFrame2, bd = 5, width= 300, height=170, padx=2, bg="gainsboro", relief = RIDGE)
        LeftFrame2Right.pack(side = RIGHT)

        RightFrame1 = Frame(TopFrame3, bd = 5, width= 320, height=400, padx=2, bg="gainsboro", relief = RIDGE)
        RightFrame1.pack(side = RIGHT)
        RightFrame1a = Frame(RightFrame1, bd = 5, width= 310, height=300, padx=2, bg="gainsboro", relief = RIDGE)
        RightFrame1a.pack(side = TOP)

        RightFrame2 = Frame(TopFrame3, bd = 5, width= 300, height=400, padx=2, bg="gainsboro", relief = RIDGE)
        RightFrame2.pack(side = RIGHT)
        RightFrame2a = Frame(RightFrame2, bd = 5, width= 280, height=50, padx=2, bg="gainsboro", relief = RIDGE)
        RightFrame2a.pack(side = TOP)
        RightFrame2b = Frame(RightFrame2, bd = 5, width= 280, height=180, padx=2, bg="gainsboro", relief = RIDGE)
        RightFrame2b.pack(side = TOP)
        RightFrame2c = Frame(RightFrame2, bd = 5, width= 280, height=100, padx=2, bg="gainsboro", relief = RIDGE)
        RightFrame2c.pack(side = TOP)
        RightFrame2d = Frame(RightFrame2, bd = 5, width= 280, height=50, padx=2, bg="gainsboro", relief = RIDGE)
        RightFrame2d.pack(side = TOP)

        #==========================Variables===============================================================================================
        global Ed
        Firstname = StringVar()
        Surname = StringVar() 
        EmployeeID = StringVar()  #Address
        Reference = StringVar()
        TaskName = StringVar() #Mobile
        DeviceName = StringVar() #Gender
        Test1 = StringVar() #CityWeighting
        Test2= StringVar() #BasicSalary
        Test3 = StringVar() #OverTime
        Test4 = StringVar() 
        Result = StringVar() #GrossPay
        NetPay = StringVar() 
        Par1 = StringVar()  #Tax
        Par2 = StringVar() #Pension
        Par3 = StringVar() #stdLoan
        Par4 = StringVar() #NIPayment
        Deductions = StringVar()
        
        Day = StringVar()  #Payday
        Period = StringVar() #TaxPeriod
        PNumber = StringVar() #NINumber
        PCode = StringVar() #NICode
        TaxablePay = StringVar()
        PensionablePay = StringVar() 
        
        Unit = StringVar() #TaxCode

        Test1.set("")
        Test2.set("")
        Test4.set("0.00")
        #==============================================Receipt==============================================================
        self.txtReceipt = Text(RightFrame1a, height=23, width =42, bd=10, font=('arial',9,'bold'))
        self.txtReceipt.grid(row =0, column = 0)
        
        #==========================Var===============================================================================================
        self.lblLabel = Label(TopFrame2,  font=('arial',10,'bold'),padx=6,pady=2,
        text="Reference\tFirstname\tsurname\t\tEmployeeID\tDeviceName\tTaskName\tNI Number\tTest1\tTest2\tTest3 \tTest4\tNet Pay\t\tResult")
              
        self.lblLabel.grid(row = 0, column=0, columnspan  =17)

        #==========================ListBox and Scrollbar===============================================================================================
        scrollbar = Scrollbar(TopFrame2)
        scrollbar.grid(row=1, column=1, sticky = 'ns')

        lstEmployee = Listbox(TopFrame2, width =145, height=5, font=('arial', 12,'bold'), yscrollcommand=scrollbar.set)
        lstEmployee.bind('<<ListboxSelect>>')
        lstEmployee.grid(row=1, column=0, padx=1, sticky='nsew')
        scrollbar.config(command = lstEmployee.xview)

        #==========================Widget===============================================================================================
        self.lblReference = Label(LeftFrame1, font=('arial',12,'bold'),text="Reference", bd=7,bg='gainsboro', anchor='w')
        self.lblReference.grid(row=0, column=0, sticky=W, padx=5)
        self.txtReference = Entry(LeftFrame1, font=('arial',12,'bold'),bd =5, width=60, justify='left', textvariable=Reference)
        self.txtReference.grid(row=0, column=1)
        
        self.lblFirstname = Label(LeftFrame1, font=('arial',12,'bold'),text="First Name", bd=7,bg='gainsboro', anchor='w')
        self.lblFirstname.grid(row=1, column=0, sticky=W, padx=5)
        self.txtFirstname = Entry(LeftFrame1, font=('arial',12,'bold'),bd =5, width=60, justify='left', textvariable=Firstname)
        self.txtFirstname.grid(row=1, column=1)

        self.lblSurname = Label(LeftFrame1, font=('arial',12,'bold'),text="Surname", bd=7,bg='gainsboro', justify=LEFT)
        self.lblSurname.grid(row=2, column=0, sticky=W, padx=5)
        self.txtSurname = Entry(LeftFrame1, font=('arial',12,'bold'),bd =5, width=60, justify='left', textvariable=Surname)
        self.txtSurname.grid(row=2, column=1)

        self.lblEmployeeID = Label(LeftFrame1, font=('arial',12,'bold'),text="Employee ID", bd=7,bg='gainsboro')
        self.lblEmployeeID.grid(row=3, column=0, sticky=W, padx=5)
        self.txtEmployeeID = Entry(LeftFrame1, font=('arial',12,'bold'),bd =5, width=60, justify='left', textvariable=EmployeeID)
        self.txtEmployeeID.grid(row=3, column=1)

        self.lblDeviceName = Label(LeftFrame1, font=('arial',12,'bold'),text="Device Name", bd=5,bg='gainsboro')
        self.lblDeviceName.grid(row=4, column=0, sticky=W, padx=5)
        self.txtDeviceName = Entry(LeftFrame1, font=('arial',12,'bold'),bd =5, width=60, justify='left', textvariable=DeviceName)
        self.txtDeviceName.grid(row=4, column=1)

        self.lblTaskName = Label(LeftFrame1, font=('arial',12,'bold'),text="Task Name", bd=5, bg='gainsboro')
        self.lblTaskName.grid(row=5, column=0, sticky=W, padx=5)
        self.txtTaskName = Entry(LeftFrame1, font=('arial',12,'bold'),bd =5, width=60, justify='left', textvariable=TaskName)
        self.txtTaskName.grid(row=5, column=1)
        

#==========================Widget===============================================================================================
        self.lblPar1 = Label(LeftFrame2Right, font=('arial',12,'bold'),text="Parameter 1", bd=7,bg='gainsboro', anchor='e')
        self.lblPar1.grid(row=0, column=0, sticky=W)
        self.txtPar1 = Entry(LeftFrame2Right, font=('arial',12,'bold'),bd =5, width=20, justify='left', textvariable=Par1)
        self.txtPar1.grid(row=0, column=1)

        self.lblPar2 = Label(LeftFrame2Right, font=('arial',12,'bold'),text="Parameter 2", bd=7,bg='gainsboro', anchor='w', justify=LEFT)
        self.lblPar2.grid(row=1, column=0, sticky=W)
        self.txtPar2 = Entry(LeftFrame2Right, font=('arial',12,'bold'),bd =5, width=20, justify='left', textvariable=Par2)
        self.txtPar2.grid(row=1, column=1)

        self.lblPar3 = Label(LeftFrame2Right, font=('arial',12,'bold'),text="Parameter 3", bd=7,bg='gainsboro',anchor='w', justify=LEFT)
        self.lblPar3.grid(row=2, column=0, sticky=W)
        self.txtPar3 = Entry(LeftFrame2Right, font=('arial',12,'bold'),bd =5, width=20, justify='left', textvariable=Par3)
        self.txtPar3.grid(row=2, column=1)

        self.lblPar4 = Label(LeftFrame2Right, font=('arial',12,'bold'),text="Parameter 4", bd=7,bg='gainsboro',anchor='w', justify=LEFT)
        self.lblPar4.grid(row=3, column=0, sticky=W)
        self.txtPar4 = Entry(LeftFrame2Right, font=('arial',12,'bold'),bd =5, width=20, justify='left', textvariable=Par4)
        self.txtPar4.grid(row=3, column=1)

        #==========================Widget===============================================================================================
        self.lblTest1 = Label(LeftFrame2Left, font=('arial',12,'bold'),text="Test 1", bd=7,bg='gainsboro', anchor='e')
        self.lblTest1.grid(row=0, column=0, sticky=W)
        self.txtTest1 = Entry(LeftFrame2Left, font=('arial',12,'bold'),bd =5, width=20, justify='left', textvariable=Test1)
        self.txtTest1.grid(row=0, column=1)

        self.lblTest2 = Label(LeftFrame2Left, font=('arial',12,'bold'),text="Test 2", bd=7,bg='gainsboro', anchor='w', justify=LEFT)
        self.lblTest2.grid(row=1, column=0, sticky=W)
        self.txtTest2 = Entry(LeftFrame2Left, font=('arial',12,'bold'),bd =5, width=20, justify='left', textvariable=Test2)
        self.txtTest2.grid(row=1, column=1)

        self.lblTest3 = Label(LeftFrame2Left, font=('arial',12,'bold'),text="Test 3 ", bd=7,bg='gainsboro',anchor='w', justify=LEFT)
        self.lblTest3.grid(row=2, column=0, sticky=W)
        self.txtTest3 = Entry(LeftFrame2Left, font=('arial',12,'bold'),bd =5, width=20, justify='left', textvariable=Test3)
        self.txtTest3.grid(row=2, column=1)

        self.lblTest4 = Label(LeftFrame2Left, font=('arial',12,'bold'),text="Test 4", bd=7,bg='gainsboro',anchor='w', justify=LEFT)
        self.lblTest4.grid(row=3, column=0, sticky=W)
        self.txtTest4 = Entry(LeftFrame2Left, font=('arial',12,'bold'),bd =5, width=20, justify='left', textvariable=Test4)
        self.txtTest4.grid(row=3, column=1)

        #==========================Widget7-21-2022===============================================================================================
        self.lblDay = Label(RightFrame2a, font=('arial',12,'bold'),text="Day", bd=7,bg='gainsboro', anchor='w', justify=LEFT)
        self.lblDay.grid(row=0, column=0, sticky=W)
        self.txtDay = Entry(RightFrame2a, font=('arial',12,'bold'),bd =5, width=20, justify='left', textvariable=Day)
        self.txtDay.grid(row=0, column=1)

        self.lblPeriod = Label(RightFrame2b, font=('arial',12,'bold'),text="Period", bd=7,bg='gainsboro', anchor='w', justify=LEFT)
        self.lblPeriod.grid(row=0, column=0, sticky=W)
        self.txtPeriod = Entry(RightFrame2b, font=('arial',12,'bold'),bd =5, width=17, justify='left', textvariable=Period)
        self.txtPeriod.grid(row=0, column=1)

        self.lblUnit = Label(RightFrame2b, font=('arial',12,'bold'),text="Unit", bd=7,bg='gainsboro', anchor='w', justify=LEFT)
        self.lblUnit.grid(row=1, column=0, sticky=W)
        self.txtUnit = Entry(RightFrame2b, font=('arial',12,'bold'),bd =5, width=17, justify='left', textvariable=Unit)
        self.txtUnit.grid(row=1, column=1)

        self.lblPNumber = Label(RightFrame2b, font=('arial',12,'bold'),text="P Number", bd=7,bg='gainsboro', anchor='w', justify=LEFT)
        self.lblPNumber.grid(row=2, column=0, sticky=W)
        self.txtPNumber = Entry(RightFrame2b, font=('arial',12,'bold'),bd =5, width=17, justify='left', textvariable=PNumber)
        self.txtPNumber.grid(row=2, column=1)

        self.lblPCode = Label(RightFrame2b, font=('arial',12,'bold'),text="P Code", bd=7,bg='gainsboro', anchor='w', justify=LEFT)
        self.lblPCode.grid(row=3, column=0, sticky=W)
        self.txtPCode = Entry(RightFrame2b, font=('arial',12,'bold'),bd =5, width=17, justify='left', textvariable=PCode)
        self.txtPCode.grid(row=3, column=1)




        
        

if __name__ == '__main__':
    root = Tk()
    applicaion = Employee(root)
    root.mainloop()
    
        
