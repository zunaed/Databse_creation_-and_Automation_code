from tkinter import*

#from tkcalendar import*
#import pymysql
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
     self.StudentID = StringVar()
     self.Firstname = StringVar()
     self.Surname = StringVar()
     self.Address = StringVar()
     self.PostCode = StringVar()
     self.Gender = StringVar()
     self.DOB = StringVar()
     self.Mobile = StringVar()
     self.Email = StringVar()
     self.ParentGuidance = StringVar()
     self.pgFirstname = StringVar()
     self.pgSurname = StringVar()
     self.pgAddress = StringVar()
     self.pgWorkPhone = StringVar()
     self.pgMobile = StringVar()
     self.pgEmail = StringVar()
     self.Course = StringVar()
     self.CourseCode = StringVar()
     self.Faculty = StringVar()
     self.Dean = StringVar()
     self.Head_of_School = StringVar()
     self.ProgramLeader = StringVar()
     self.CourseTutor = StringVar()
     self.Building = StringVar()
     self.HomeStudent = StringVar()
     self.Oversea = StringVar()
     self.Accomodation = StringVar()
     self.ExchangeProg = StringVar()
     self.Scholarship = StringVar()

     self.BA = StringVar()
     self.BSc = StringVar()
     self.MA = StringVar()
     self.MSc = StringVar()
     self.Phd = StringVar()

     self.DataScience = StringVar()
     self.EventDrivenPro = StringVar()
     self.ObjectOriented = StringVar()
     self.Spreadsheet = StringVar()
     self.SystemAnalysis = StringVar()
     self.InformTechnology = StringVar()
     self.DigitalGraphics = StringVar()

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

     RightFrame1 = Frame(TopFrame3, bd=5, width = 320, height = 400,padx=2, bg="cadetblue", relief = RIDGE)
     RightFrame1.pack(side=RIGHT, pady=1)

     InnerRightFrame = Frame(RightFrame1, bd=5, width = 310, height = 300,padx=2, relief = RIDGE)
     InnerRightFrame.pack(side=TOP, pady=2)

     CalenderFrame = Frame(InnerRightFrame, bd=5, width = 310, height = 300,padx=2, relief = RIDGE)
     CalenderFrame.pack(side=TOP, pady=1)

     UnitsFrame = Frame(InnerRightFrame, bd=5, width = 310, height = 300,padx=2, relief = RIDGE)
     UnitsFrame.pack(side=TOP, pady=1)

     ResultFrame = Frame(InnerRightFrame, bd=5, width = 330, height = 50,padx=2, relief = RIDGE)
     ResultFrame.pack(side=TOP, pady=1)

     ResultFrameLeft = Frame(ResultFrame, bd=0, width = 130, height = 50,padx=2, relief = RIDGE)
     ResultFrameLeft.grid(row=0,column=0,pady=1)

     ResultFrameRight = Frame(ResultFrame, bd=0, width = 200, height = 50,padx=2, relief = RIDGE)
     ResultFrameRight.grid(row=0,column=1)

     UnitNo = Frame(UnitsFrame, bd=0, width=50, height=300, padx=2, relief=RIDGE)
     UnitNo.grid(row=0, column=0, pady=2)

     UnitSubject = Frame(UnitsFrame, bd=1, width=210, height=300, padx=2,pady=4, relief=RIDGE)
     UnitSubject.grid(row=0, column=1, pady=2)

     UnitScore = Frame(UnitsFrame, bd=0, width=50, height=300, padx=2,pady=3, relief=RIDGE)
     UnitScore.grid(row=0, column=2, pady=1)

#+++++++++++++++++++++++++++++++++++Frames+++++++++++++++++++++++++++
     LeftFrame = Frame(TopFrame3, bd=5, width = 1340, height = 400,padx=2, bg="cadetblue", relief = RIDGE)
     LeftFrame.pack(side=RIGHT, pady=0)
     CourseFrame = Frame(LeftFrame, bd=5, width = 600, height = 180,padx=4, relief = RIDGE)
     CourseFrame.pack(side=TOP, pady=2)

     LeftFrame2 = Frame(LeftFrame, bd=5, width = 600, height = 180,padx=2, bg="cadetblue", relief = RIDGE)
     LeftFrame2.pack(side=TOP)
     StudentStatusFrame = Frame(LeftFrame2, bd=5, width = 300, height = 170,padx=2, relief = RIDGE)
     StudentStatusFrame.pack(side=LEFT)
     DegreeFrame = Frame(LeftFrame2, bd=5, width = 300, height = 170,padx=2, relief = RIDGE)
     DegreeFrame.pack(side=RIGHT)

     ButtonFrame = Frame(LeftFrame, bd=5, width = 320, height = 50,padx=3, relief = RIDGE)
     ButtonFrame.pack(side=LEFT, pady=3)

     RightFrame2 = Frame(TopFrame3, bd=5, width = 300, height = 400,padx=2, bg="cadetblue", relief = RIDGE)
     RightFrame2.pack(side=LEFT, pady=5)
     StudentFrame = Frame(RightFrame2, bd=5, width = 280, height = 50,padx=2, relief = RIDGE)
     StudentFrame.pack(side=TOP, pady=3)
     ParentFrame = Frame(RightFrame2, bd=5, width = 280, height = 50,padx=3, relief = RIDGE)
     ParentFrame.pack(side=TOP)

     TopFrame11 = Frame(Tab2Frame, bd=10, width = 1340, height = 60, relief = RIDGE)
     TopFrame11.grid(row=0, column=0)
     TopFrame12 = Frame(Tab2Frame, bd=10, width = 1340, height = 100, relief = RIDGE)
     TopFrame12.grid(row=1, column=0)

     TopFrame12a = Frame(TopFrame12, bd=10, width = 1000, height = 100, relief = RIDGE)
     TopFrame12a.grid(row=1, column=0)

     TopFrame12b = Frame(TopFrame12, bd=10, width = 340, height = 100, relief = RIDGE)
     TopFrame12b.grid(row=1, column=0)


#+++++++++++++++++++++++++++++++++++Frames+++++++++++++++++++++++++++
     self.lblStudentID = Label(StudentFrame, font=('arial',12,'bold'), text='Star ID', bd=7, anchor='w', justify=LEFT)
     self.lblStudentID.grid(row=0,column=0, sticky = W, padx=5, pady=5)
     self.txtStudentID = Entry(StudentFrame, font=('arial',12,'bold'),bd=5, width = 25, justify = 'left', textvariable = self.StudentID)
     self.txtStudentID.grid(row=0,column=1)

     self.lblFirstname = Label(StudentFrame, font=('arial',12,'bold'), text='st name', bd=7, justify=LEFT)
     self.lblFirstname.grid(row=1,column=0, sticky = W, padx=5)
     self.txtFirstname = Entry(StudentFrame, font=('arial',12,'bold'),bd=5, width = 25, justify = 'left', textvariable = self.Firstname)
     self.txtFirstname.grid(row=1,column=1)

     self.lblSurname = Label(StudentFrame, font=('arial',12,'bold'), text='st code', bd=5)
     self.lblSurname.grid(row=2,column=0, sticky = W, padx=5)
     self.txtSurname = Entry(StudentFrame, font=('arial',12,'bold'),bd=5, width = 25, textvariable = self.Surname)
     self.txtSurname.grid(row=2,column=1)

     self.lblAddress = Label(StudentFrame, font=('arial',12,'bold'), text='st id', bd=5)
     self.lblAddress.grid(row=3,column=0, sticky = W, padx=5)
     self.txtAddress = Entry(StudentFrame, font=('arial',12,'bold'),bd=5, width = 25, textvariable = self.Address)
     self.txtAddress.grid(row=3,column=1)
     
     self.lblPostCode = Label(StudentFrame, font=('arial',12,'bold'), text='Code', bd=5)
     self.lblPostCode.grid(row=4,column=0, sticky = W, padx=5)
     self.txtPostCode = Entry(StudentFrame, font=('arial',12,'bold'),bd=5, width = 25, textvariable = self.PostCode)
     self.txtPostCode.grid(row=4,column=1)

     self.lblGender = Label(StudentFrame, font=('arial',12,'bold'), text='shift', bd=5)
     self.lblGender.grid(row=5,column=0, sticky = W, padx=5)
     self.cboGender = ttk.Combobox(StudentFrame,textvariable = self.Gender, width = 23, font=('arial',12,'bold'), state = 'readonly')
     self.cboGender['value'] = ('','day','night')
     self.cboGender.current(0)
     self.cboGender.grid(row=5,column=1)

     self.lblDOB = Label(StudentFrame, font=('arial',12,'bold'), text='date', bd=5)
     self.lblDOB.grid(row=6,column=0, sticky = W, padx=5)
     self.txtDOB = Entry(StudentFrame, font=('arial',12,'bold'),bd=5, width = 25, textvariable = self.DOB)
     self.txtDOB.grid(row=6,column=1)
     
     self.lblMobile = Label(StudentFrame, font=('arial',12,'bold'), text='inspec. id', bd=5)
     self.lblMobile.grid(row=7,column=0, sticky = W, padx=5)
     self.txtMobile = Entry(StudentFrame, font=('arial',12,'bold'),bd=5, width = 25, textvariable = self.Mobile)
     self.txtMobile.grid(row=7,column=1)

     self.lblEmail = Label(StudentFrame, font=('arial',12,'bold'), text='', bd=5)
     self.lblEmail.grid(row=7,column=0, sticky = W, padx=5)
     self.txtEmail = Entry(StudentFrame, font=('arial',12,'bold'),bd=5, width = 25, textvariable = self.Email)
     self.txtEmail.grid(row=8,column=1)
 
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

     self.lblParentGuidance = Label(ParentFrame, font=('arial',12,'bold'), text='test 1', bd=5)
     self.lblParentGuidance.grid(row=0,column=0, sticky = W, padx=5)
     self.cboParentGuidance = ttk.Combobox(ParentFrame,textvariable = self.ParentGuidance, width = 16, font=('arial',12,'bold'), state = 'readonly')
     self.cboParentGuidance['value'] = ('','option1','option2','option3','option4')
     self.cboParentGuidance.current(0)
     self.cboParentGuidance.grid(row=0,column=1)

     self.lblpgFirstname = Label(ParentFrame, font=('arial',12,'bold'), text='test 2', bd=7, justify=LEFT)
     self.lblpgFirstname.grid(row=1,column=0, sticky = W, padx=5)
     self.txtFirstname = Entry(ParentFrame, font=('arial',12,'bold'),bd=5, width = 17, justify = 'left', textvariable = self.pgFirstname)
     self.txtFirstname.grid(row=1,column=1)

     self.lblpgSurname = Label(ParentFrame, font=('arial',12,'bold'), text='test 3', bd=5)
     self.lblpgSurname.grid(row=2,column=0, sticky = W, padx=5)
     self.txtpgSurname = Entry(ParentFrame, font=('arial',12,'bold'),bd=5, width = 17, textvariable = self.pgSurname)
     self.txtpgSurname.grid(row=2,column=1)

     self.lblpgAddress = Label(ParentFrame, font=('arial',12,'bold'), text='test 4', bd=5)
     self.lblpgAddress.grid(row=3,column=0, sticky = W, padx=5)
     self.txtpgAddress = Entry(ParentFrame, font=('arial',12,'bold'),bd=5, width = 17, textvariable = self.pgAddress)
     self.txtpgAddress.grid(row=3,column=1)

     self.lblpgWorkPhone = Label(ParentFrame, font=('arial',12,'bold'), text='test 5', bd=5)
     self.lblpgWorkPhone.grid(row=4,column=0, sticky = W, padx=5)
     self.txtpgWorkPhone = Entry(ParentFrame, font=('arial',12,'bold'),bd=5, width = 17, textvariable = self.pgWorkPhone)
     self.txtpgWorkPhone.grid(row=4,column=1)
     
     self.lblpgMobile = Label(ParentFrame, font=('arial',12,'bold'), text='test 6', bd=5)
     self.lblpgMobile.grid(row=5,column=0, sticky = W, padx=5)
     self.txtpgMobile = Entry(ParentFrame, font=('arial',12,'bold'),bd=5, width = 17, textvariable = self.pgMobile)
     self.txtpgMobile.grid(row=5,column=1)

     self.lblpgEmail = Label(ParentFrame, font=('arial',12,'bold'), text='test 7', bd=5)
     self.lblpgEmail.grid(row=6,column=0, sticky = W, padx=5)
     self.txtpgEmail = Entry(ParentFrame, font=('arial',12,'bold'),bd=5, width = 17, textvariable = self.pgEmail)
     self.txtpgEmail.grid(row=6,column=1,pady =3)

#+++++++++++++++++++++++++++++++++++++++++++self.course++++++++++
     self.Course.set(" Selector")
     self.lblCourse = Label(CourseFrame, font=('arial',12,'bold'), text='Line name', bd=6,)
     self.lblCourse.grid(row=0,column=0, sticky = W, padx=5)
     self.cboCourse = ttk.Combobox(CourseFrame,textvariable = self.Course, width = 51, font=('arial',12,'bold'), state = 'readonly')
     self.cboCourse['value'] = ('','star','nimbus','vantage')
     self.cboCourse.current(0)
     self.cboCourse.grid(row=0,column=1)

     self.lblCourseCode = Label(CourseFrame, font=('arial',12,'bold'), text=' Code', bd=6)
     self.lblCourseCode.grid(row=1,column=0, sticky = W, padx=5)
     self.txtCourseCode = Entry(CourseFrame, font=('arial',12,'bold'),bd=5, width = 52, textvariable = self.CourseCode)
     self.txtCourseCode.grid(row=1,column=1)

     self.lblFaculty = Label(CourseFrame, font=('arial',12,'bold'), text='Name', bd=6)
     self.lblFaculty.grid(row=2,column=0, sticky = W, padx=5)
     self.txtFaculty = Entry(CourseFrame, font=('arial',12,'bold'),bd=5, width = 52, textvariable = self.Faculty)
     self.txtFaculty.grid(row=2,column=1)

     self.lblDean = Label(CourseFrame, font=('arial',12,'bold'), text='', bd=6)
     self.lblDean.grid(row=3,column=0, sticky = W, padx=5)
     self.txtDean = Entry(CourseFrame, font=('arial',12,'bold'),bd=5, width = 52, textvariable = self.Dean)
     self.txtDean.grid(row=3,column=1)

     self.lblHoS = Label(CourseFrame, font=('arial',12,'bold'), text='', bd=6)
     self.lblHoS.grid(row=4,column=0, sticky = W, padx=5)
     self.txtHoS = Entry(CourseFrame, font=('arial',12,'bold'),bd=5, width = 52, textvariable = self.Head_of_School)
     self.txtHoS.grid(row=4,column=1)

     self.lblProgramLeader = Label(CourseFrame, font=('arial',12,'bold'), text='', bd=6)
     self.lblProgramLeader.grid(row=5,column=0, sticky = W, padx=5)
     self.txtProgramLeader = Entry(CourseFrame, font=('arial',12,'bold'),bd=5, width = 52, textvariable = self.ProgramLeader)
     self.txtProgramLeader.grid(row=5,column=1)

     self.lblCourseTutor = Label(CourseFrame, font=('arial',12,'bold'), text='', bd=6)
     self.lblCourseTutor.grid(row=6,column=0, sticky = W)
     self.txtCourseTutor = Entry(CourseFrame, font=('arial',12,'bold'),bd=5, width = 52, textvariable = self.CourseTutor)
     self.txtCourseTutor.grid(row=6,column=1)

     self.lblBuilding = Label(CourseFrame, font=('arial',12,'bold'), text='', bd=6)
     self.lblBuilding.grid(row=7,column=0, sticky = W)
     self.txtBuilding = Entry(CourseFrame, font=('arial',12,'bold'),bd=5, width = 52, textvariable = self.Building)
     self.txtBuilding.grid(row=7,column=1)

#+++++++++++++++++++++++++++++++++++++++++++StudentStatusFrame++++++++++
     
     self.lblHomeStudent = Label(StudentStatusFrame, font=('arial',12,'bold'), text='chck 1', bd=6,)
     self.lblHomeStudent.grid(row=0,column=0, sticky = W)
     self.cboHomeStudent = ttk.Combobox(StudentStatusFrame,textvariable = self.HomeStudent, width = 14, font=('arial',12,'bold'), state = 'readonly')
     self.cboHomeStudent['values'] = ('No','Yes')
     self.cboHomeStudent.current(0)
     self.cboHomeStudent.grid(row=0,column=1, pady=8)

     self.lblOversea = Label(StudentStatusFrame, font=('arial',12,'bold'), text='chck 2', bd=6,)
     self.lblOversea.grid(row=1,column=0, sticky = W)
     self.cboOversea = ttk.Combobox(StudentStatusFrame,textvariable = self.Oversea, width = 14, font=('arial',12,'bold'), state = 'readonly')
     self.cboOversea['values'] = ('No','Yes')
     self.cboOversea.current(0)
     self.cboOversea.grid(row=1,column=1, pady=8)


     self.lblAccomodation = Label(StudentStatusFrame, font=('arial',12,'bold'), text='chck 3', bd=6,)
     self.lblAccomodation.grid(row=2,column=0, sticky = W)
     self.cboAccomodation = ttk.Combobox(StudentStatusFrame,textvariable = self.Accomodation, width = 14, font=('arial',12,'bold'), state = 'readonly')
     self.cboAccomodation['values'] = ('No','Yes')
     self.cboAccomodation.current(0)
     self.cboAccomodation.grid(row=2,column=1, pady=8)

     self.lblExchangeProg = Label(StudentStatusFrame, font=('arial',12,'bold'), text='chck 4', bd=6,)
     self.lblExchangeProg.grid(row=3,column=0, sticky = W)
     self.cboExchangeProg = ttk.Combobox(StudentStatusFrame,textvariable = self.Accomodation, width = 14, font=('arial',12,'bold'), state = 'readonly')
     self.cboExchangeProg['values'] = ('No','Yes')
     self.cboExchangeProg.current(0)
     self.cboExchangeProg.grid(row=3,column=1, pady=8)

     self.lblScholarship = Label(StudentStatusFrame, font=('arial',12,'bold'), text='chck 5', bd=6,)
     self.lblScholarship.grid(row=4,column=0, sticky = W)
     self.cboScholarship = ttk.Combobox(StudentStatusFrame,textvariable = self.Scholarship, width = 14, font=('arial',12,'bold'), state = 'readonly')
     self.cboScholarship['values'] = ('No','Yes')
     self.cboScholarship.current(0)
     self.cboScholarship.grid(row=4,column=1, pady=8)

#+++++++++++++++++++++++++++++++++++++++++++DegreeFrame++++++++++   
     self.lblBA = Label(DegreeFrame, font=('arial',12,'bold'), text='Range 1', bd=10)
     self.lblBA.grid(row=0,column=0, sticky = W)
     self.SpBA = ttk.Spinbox(DegreeFrame, from_=0, to=20,textvariable = self.BA, width = 9, font=('arial',12,'bold'))
     self.SpBA.grid(row=0,column=1, pady=5)

     self.lblBSc = Label(DegreeFrame, font=('arial',12,'bold'), text='Range 2 ', bd=10)
     self.lblBSc.grid(row=1,column=0, sticky = W)
     self.SpBSc  = ttk.Spinbox(DegreeFrame, from_=0, to=20,textvariable = self.BSc, width = 9, font=('arial',12,'bold'))
     self.SpBSc.grid(row=1,column=1, pady=5)

     self.lblMA = Label(DegreeFrame, font=('arial',12,'bold'), text='Range 3', bd=10)
     self.lblMA.grid(row=2,column=0, sticky = W)
     self.SpMA  = ttk.Spinbox(DegreeFrame, from_=0, to=20,textvariable = self.MA, width = 9, font=('arial',12,'bold'))
     self.SpMA.grid(row=2,column=1, pady=5)

     self.lblMSc = Label(DegreeFrame, font=('arial',12,'bold'), text='Range 3', bd=10)
     self.lblMSc.grid(row=3,column=0, sticky = W)
     self.SpMSc  = ttk.Spinbox(DegreeFrame, from_=0, to=20,textvariable = self.MSc, width = 9, font=('arial',12,'bold'))
     self.SpMSc.grid(row=3,column=1, pady=5)

     self.lblPhd = Label(DegreeFrame, font=('arial',12,'bold'), text='Range 4', bd=10)
     self.lblPhd.grid(row=4,column=0, sticky = W)
     self.SpPhd  = ttk.Spinbox(DegreeFrame, from_=0, to=20,textvariable = self.Phd, width = 9, font=('arial',12,'bold'))
     self.SpPhd.grid(row=4,column=1, pady=5)


#+++++++++++++++++++++++++++++calender frame+++++++++++++++++++++++
     
#+++++++++++++++++++++++++++Unit No++++++++++++++++++++++
     self.lblNo = Label(UnitNo, font=('arial',12,'bold'), text='No', padx=2, pady=4)
     self.lblNo.grid(row=0,column=0, sticky = W)
     self.lbl1 = Label(UnitNo, font=('arial',12,'bold'), text='1', padx=2, pady=4)
     self.lbl1.grid(row=1,column=0, sticky = W)
     self.lbl2 = Label(UnitNo, font=('arial',12,'bold'), text='2', padx=2, pady=4)
     self.lbl2.grid(row=2,column=0, sticky = W)
     self.lbl3 = Label(UnitNo, font=('arial',12,'bold'), text='3', padx=2, pady=4)
     self.lbl3.grid(row=3,column=0, sticky = W)
     self.lbl4 = Label(UnitNo, font=('arial',12,'bold'), text='4', padx=2, pady=4)
     self.lbl4.grid(row=4,column=0, sticky = W)
     self.lbl5 = Label(UnitNo, font=('arial',12,'bold'), text='5', padx=2, pady=4)
     self.lbl5.grid(row=5,column=0, sticky = W)
     self.lbl6 = Label(UnitNo, font=('arial',12,'bold'), text='6', padx=2, pady=4)
     self.lbl6.grid(row=6,column=0, sticky = W)
     self.lbl7 = Label(UnitNo, font=('arial',12,'bold'), text='7', padx=2, pady=4)
     self.lbl7.grid(row=7,column=0, sticky = W)
     self.lbl8 = Label(UnitNo, font=('arial',12,'bold'), text='8', padx=2, pady=4)
     self.lbl8.grid(row=8,column=0, sticky = W)
     

#+++++++++++++++++++++++++++++++Unit Subject+++++++++++++++
     self.lblSelectUnit = Label(UnitSubject, font=('arial',12,'bold'), text='Select the test', padx=2, pady=4)
     self.lblSelectUnit.grid(row=0,column=0, sticky = W)
     self.cboHomeStudent = ttk.Combobox(UnitSubject,textvariable = self.ExchangeProg, width = 18, font=('arial',12,'bold'), state = 'readonly')
     self.cboHomeStudent['values'] = ('','Event Driven Prog','Yes')
     self.cboHomeStudent.current(0)
     self.cboHomeStudent.grid(row=1,column=0,padx=2, pady=3)


     #+++++++++++++++++++++++++++++++UnitScore+++++++++++++++
     self.lblSUnit = Label(UnitScore, font=('arial',12,'bold'), text='Score', padx=2, pady=4)
     self.lblSUnit.grid(row=0,column=0, sticky = W)

     

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





















