import sqlite3
#Backend

def EmployeeData():
    con = sqlite3.connect("Employee.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Employee (id INTEGER PRIMARY KEY, Reference text, Firstname text, Surname text, Address text, Gender text, Mobile text,\
    NINumber text, stdLoan Text, Tax text, Pension text, Deductions text, NetPay text, GrossPay text)")
    con.commit()
    con.close()


def addEmployeeRec(Reference,Firstname,Surname,Address,Gender,Mobile,NINumber,stdLoan,Tax,Pension,Deductions,NetPay,GrossPay):
    con = sqlite3.connect("Employee.db")
    cur = con.cursor()
    cur.execute("INSERT INTO Employee VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?)", \
                (Reference,Firstname,Surname,Address,Gender,Mobile,NINumber,stdLoan,Tax,Pension,Deductions,NetPay,GrossPay))
    con.commit()
    con.close()


def viewData():
    con = sqlite3.connect("Employee.db")
    cur = con.cursor("SELECT * FROM Employee")
    rows = cur.fetchall()
    con.close()
    return rows

def deleteRec(id):
    con = sqlite3.connect("Employee.db")
    cur = con.cursor("DELETE * FROM Employee WHERE id=?", (id,))
    con.commit()
    con.close()
    return rows

def searchData(Reference="",Firstname="",Surname="",Address="",Gender="",Mobile="",NINumber="",stdLoan="",Tax="",Pension="",Deductions="",Netpay="",GrossPay=""):
    con = sqlite3.connect("Employee.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM Employee WHERE Reference=? OR Firstname=? OR Surname =? OR Address =? OR Gender =? OR Mobile =? \
                 OR NINumber =? OR stdLoan =? OR Tax =? OR Pension =? OR Deductions =? OR Netpay =? OR GrossPay)", \
                (Reference,Firstname,Surname,Address,Gender,Mobile,NINumber,stdLoan,Tax,Pension,Deductions,Netpay,GrossPay))            
    rows = cur.fetchall()
    con.close()
    return rows

def dataUpdate(Reference="",Firstname="",Surname="",Address="",Gender="",Mobile="",NINumber="",stdLoan="",Tax="",Pension="",Deductions="",Netpay="",GrossPay=""):
    con = sqlite3.connect("Employee.db")
    cur = con.cursor()
    cur.execute("UPDATE Employee SET Reference=?, Firstname=?,Surname=?, Address =?, Gender =?, Mobile =? \
                 ,NINumber =?, stdLoan =?, Tax =?, Pension =?, Deductions =?, Netpay =?, GrossPay)", \
                (Reference,Firstname,Surname,Address,Gender,Mobile,NINumber,stdLoan,Tax,Pension,Deductions,Netpay,GrossPay,id))            
    con.commit()
    con.close()


EmployeeData()
