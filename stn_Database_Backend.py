import sqlite3
#Backend

def employeeData():
    con = sqlite3.connect("employee.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(id INTEGER PRIMARY KEY, EmpID text, Testname text, Eqpname text, Shift text, StationID text, Testtype text,Result text, Date text)")
    con.commit()
    con.close()


def addEmpRec(EmpID,Testname,Eqpname,Shift,StationID,Testtype,Result,Date):
    con = sqlite3.connect("employee.db")
    cur = con.cursor()
    cur.execute("INSERT INTO employee VALUES (NULL,?,?,?,?,?,?,?,?)",(EmpID,Testname,Eqpname,Shift,StationID,Testtype,Result,Date))
    con.commit()
    con.close()


def viewData():
    con = sqlite3.connect("employee.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM employee")
    rows = cur.fetchall()
    con.close()
    return rows

def deleteRec(id):
    con = sqlite3.connect("employee.db")
    cur = con.cursor()
    cur.execute("DELETE FROM employee WHERE id=?",(id,))
    con.commit()
    con.close()
    

def searchData(EmpID="",Testname="",Eqpname="",Shift="",StationID="",Testtype="",Result="",Date=""):
    con = sqlite3.connect("employee.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM employee WHERE EmpID=? OR Testname=? OR Eqpname =? OR Shift =? OR StationID =? OR Testtype =? OR Result =? OR Date =? ",(EmpID,Testname,Eqpname,Shift,StationID,Testtype,Result,Date))            
    rows = cur.fetchall()
    con.close()
    return rows

def dataUpdate(id,EmpID="",Testname="",Eqpname="",Shift="",StationID="",Testtype="",Result="",Date=""):
    con = sqlite3.connect("employee.db")
    cur = con.cursor()
    cur.execute("UPDATE employee SET EmpID=?, Testname=?,Eqpname=?, Shift =?,StationID =?, Testtype =?,Result =?, Date =?, WHERE id=? ", (EmpID,Testname,Eqpname,Shift,StationID,Testtype,Result,Date,id))            
    con.commit()
    con.close()


employeeData()
