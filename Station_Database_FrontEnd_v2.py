#Frontend

from tkinter import*
import tkinter.messagebox
import stn_Database_Backend


class Employee:
    def __init__(self,root):
        self.root =root
        self.root.title("Station Management Systems")#change
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="cadet blue")

        EmpID = StringVar()
        Testname = StringVar()
        Eqpname = StringVar()
        Shift = StringVar()
        StationID = StringVar()
        Testtype = StringVar()
        Result = StringVar()
        Date = StringVar()
        #========== Function======
        def iExit():
            iExit = tkinter.messagebox.askyesno("Station Management Systems", "Confirm if you want to exit")#change
            if iExit > 0:
             root.destroy()
             return

        def clearData():
            self.txtEmpID.delete(0,END)
            self.txtfna.delete(0,END)
            self.txtSna.delete(0,END)
            self.txtShift.delete(0,END)
            self.txtStationID.delete(0,END)
            self.txtTesttype.delete(0,END)
            self.txtResult.delete(0,END)
            self.txtDate.delete(0,END)

        def addData():
            if(len(EmpID.get())!=0):
                stn_Database_Backend.addEmpRec(EmpID.get(),Testname.get(),Eqpname.get(),Shift.get(),StationID.get(),Testtype.get(),Result.get(),Date.get())
                employeelist.delete(0,END)
                employeelist.insert(END,(EmpID.get(),Testname.get(),Eqpname.get(),Shift.get(),StationID.get(),Testtype.get(),Result.get(),Date.get()))

        
        def DisplayData():
            employeelist.delete(0,END)
            for row in stn_Database_Backend.viewData():
             employeelist.insert(END,row,str(""))

        def EmployeeRec(event):
            global sd
            searchStd = employeelist.curselection()[0]
            sd= employeelist.get(searchStd)

            self.txtEmpID.delete(0,END)
            self.txtEmpID.insert(END,sd[1])
            self.txtfna.delete(0,END)
            self.txtfna.insert(END,sd[2])
            self.txtSna.delete(0,END)
            self.txtSna.insert(END,sd[3])
            self.txtShift.delete(0,END)
            self.txtShift.insert(END,sd[4])
            self.txtStationID.delete(0,END)
            self.txtStationID.insert(END,sd[5])
            self.txtTesttype.delete(0,END)
            self.txtTesttype.insert(END,sd[6])
            self.txtResult.delete(0,END)
            self.txtResult.insert(END,sd[7])
            self.txtDate.delete(0,END)
            self.txtDate.insert(END,sd[8])

        def DeleteData():
            if(len(EmpID.get())!=0):
              stn_Database_Backend.deleteRec(sd[0])
              clearData()
              DisplayData()

        def searchDatabase():
            employeelist.delete(0,END)
            for row in stn_Database_Backend.searchData(EmpID.get(),Testname.get(),Eqpname.get(),Shift.get(),StationID.get(),Testtype.get(),Result.get(),Date.get()):
             employeelist.insert(END,row,str(""))

        def update():
            if(len(EmpID.get())!=0):
             stn_Database_Backend.deleteRec(sd[0])
            if(len(EmpID.get())!=0):
             stn_Database_Backend.addEmpRec(EmpID.get(),Testname.get(),Eqpname.get(),Shift.get(),StationID.get(),Testtype.get(),Result.get(),Date.get())
             employeelist.delete(0,END)
             employeelist.insert(END,(EmpID.get(),Testname.get(),Eqpname.get(),Shift.get(),StationID.get(),Testtype.get(),Result.get(),Date.get()))


            
        #========== Frames======

        MainFrame = Frame(self.root, bg="cadet blue")
        MainFrame.grid()

        TitFrame = Frame(MainFrame, bd =2, padx = 54, pady=8, bg= "Ghost White", relief=RIDGE)
        TitFrame.pack(side=TOP)

        self.lblTit = Label(TitFrame,font=('arial', 47,'bold'),text= " Station Management Systems", bg="Ghost White") #change
        self.lblTit.grid()

        ButtonFrame = Frame(MainFrame, bd=2, width=1350, height=70, padx=18, pady=10, bg="Ghost White", relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=20, bg="cadet blue", relief=RIDGE)
        DataFrame.pack(side=BOTTOM)
                
        DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=1000, height=600, padx=20,  bg="Ghost White", relief=RIDGE,font=('arial', 20,'bold'),text="Station Info\n")#change
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=450, height=300, padx=31, pady=3, bg="Ghost White", relief=RIDGE,font=('arial', 20,'bold'),text="Station Details\n")#change
        DataFrameRIGHT.pack(side=RIGHT)


        #==========label and Entry Widgtet ======
        self.lblEmpID = Label(DataFrameLEFT,font=('arial', 20,'bold'),text= "Employee ID:",padx=2, pady=2, bg="Ghost White") #change
        self.lblEmpID.grid(row=0, column=0, sticky=W)
        self.txtEmpID = Entry(DataFrameLEFT,font=('arial', 20,'bold'),textvariable=EmpID,width=39)
        self.txtEmpID.grid(row=0, column=1)

        self.lblfna = Label(DataFrameLEFT,font=('arial', 20,'bold'),text= "Test Name:",padx=2, pady=2, bg="Ghost White")#change
        self.lblfna.grid(row=1, column=0, sticky=W)
        self.txtfna = Entry(DataFrameLEFT,font=('arial', 20,'bold'),textvariable=Testname,width=39)
        self.txtfna.grid(row=1, column=1)

        self.lblSna = Label(DataFrameLEFT,font=('arial', 20,'bold'),text= "Equipmen Name:",padx=2, pady=2, bg="Ghost White")#change
        self.lblSna.grid(row=2, column=0, sticky=W)
        self.txtSna = Entry(DataFrameLEFT,font=('arial', 20,'bold'),textvariable=Eqpname,width=39)
        self.txtSna.grid(row=2, column=1)

        self.lblShift = Label(DataFrameLEFT,font=('arial', 20,'bold'),text= "Shift:",padx=2, pady=2, bg="Ghost White")#change
        self.lblShift.grid(row=3, column=0, sticky=W)
        self.txtShift = Entry(DataFrameLEFT,font=('arial', 20,'bold'),textvariable=Shift,width=39)
        self.txtShift.grid(row=3, column=1)

        self.lblStationID = Label(DataFrameLEFT,font=('arial', 20,'bold'),text= "Station ID",padx=2, pady=2, bg="Ghost White")#change
        self.lblStationID.grid(row=4, column=0, sticky=W)
        self.txtStationID = Entry(DataFrameLEFT,font=('arial', 20,'bold'),textvariable=StationID,width=39)
        self.txtStationID.grid(row=4, column=1)

        self.lblTesttype = Label(DataFrameLEFT,font=('arial', 20,'bold'),text= "Test type",padx=2, pady=2, bg="Ghost White")#change
        self.lblTesttype.grid(row=5, column=0, sticky=W)
        self.txtTesttype = Entry(DataFrameLEFT,font=('arial', 20,'bold'),textvariable=Testtype,width=39)
        self.txtTesttype.grid(row=5, column=1)

        self.lblResult = Label(DataFrameLEFT,font=('arial', 20,'bold'),text= "Test Result",padx=2, pady=2, bg="Ghost White")#change
        self.lblResult.grid(row=6, column=0, sticky=W)
        self.txtResult = Entry(DataFrameLEFT,font=('arial', 20,'bold'),textvariable=Result,width=39)
        self.txtResult.grid(row=6, column=1)

        self.lblDate = Label(DataFrameLEFT,font=('arial', 20,'bold'),text= "Date",padx=2, pady=2, bg="Ghost White")#change
        self.lblDate.grid(row=7, column=0, sticky=W)
        self.txtDate = Entry(DataFrameLEFT,font=('arial', 20,'bold'),textvariable=Date,width=39)
        self.txtDate.grid(row=7, column=1)


        #==========ListBox & Scrollbar Widget ======

        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0, column=1, sticky='ns')

        employeelist = Listbox(DataFrameRIGHT, width=41, height=16, font=('arial',12,'bold'), yscrollcommand=scrollbar.set)
        employeelist.bind('<<ListboxSelect>>',EmployeeRec)
        employeelist.grid(row=0, column=0, padx=8)
        scrollbar.config(command = employeelist.yview)

        #==========Buttons Widgtet ======

        self.btnAddData = Button(ButtonFrame, text="Add New", font=('arial', 20, 'bold'), height=1,width=10, bd=4, command=addData)
        self.btnAddData.grid(row=0, column=0)
        
        self.btnDisplayData = Button(ButtonFrame, text="Display", font=('arial', 20, 'bold'), height=1,width=10, bd=4,command=DisplayData)
        self.btnDisplayData.grid(row=0, column=1)
        
        self.btnClearData = Button(ButtonFrame, text="Clear", font=('arial', 20, 'bold'), height=1,width=10, bd=4, command=clearData)
        self.btnClearData.grid(row=0, column=2)
        
        self.btnDeleteData = Button(ButtonFrame, text="Delete", font=('arial', 20, 'bold'), height=1,width=10, bd=4, command=DeleteData)
        self.btnDeleteData.grid(row=0, column=3)
        
        self.btnSearchData = Button(ButtonFrame, text="Search", font=('arial', 20, 'bold'), height=1,width=10, bd=4, command=searchDatabase)
        self.btnSearchData.grid(row=0, column=4)
        
        self.btnUpdateData = Button(ButtonFrame, text="Update", font=('arial', 20, 'bold'), height=1,width=10, bd=4, command = update)
        self.btnUpdateData.grid(row=0, column=5)
        
        self.btnExit = Button(ButtonFrame, text="Exit", font=('arial', 20, 'bold'), height=1,width=10, bd=4, command=iExit)
        self.btnExit.grid(row=0, column=6)
                          
if __name__=='__main__':
     root=Tk()
     application = Employee(root)
     root.mainloop()
