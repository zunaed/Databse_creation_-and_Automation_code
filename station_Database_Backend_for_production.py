import sqlite3
#Backend

def stationData():
    con = sqlite3.connect("station.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS station(id INTEGER PRIMARY KEY, Line text, Shift text, WorkstationID text, WorkstationName text, TesterID text, TesterName text,InspectionItemID text, InspectionItemType text,\
                 Descripton text, InspectionGroupID text, Test1 text, Test2 text, Test3 text, Test4 text, Test5 text, NumericVal1 text, NumericVal2 text, NumericVal3 text, NumericVal4 text, NumericVal5 text,\
                 Checklist1 text, Checklist2 text, Checklist3 text, Checklist4 text, Checklist5 text)")
    con.commit()
    con.close()


def addStnRec(Line, Shift, WorkstationID, WorkstationName, TesterID, TesterName,InspectionItemID, InspectionItemType, Descripton, InspectionGroupID, \
              Test1, Test2, Test3, Test4, Test5, NumericVal1, NumericVal2, NumericVal3, NumericVal4, NumericVal5,Checklist1, Checklist2, Checklist3, Checklist4, Checklist5):
    con = sqlite3.connect("station.db")
    cur = con.cursor()
    cur.execute("INSERT INTO station VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(Line, Shift, WorkstationID, WorkstationName, TesterID, TesterName,InspectionItemID, InspectionItemType,\
                                                                     Descripton, InspectionGroupID, Test1, Test2, Test3, Test4, Test5, NumericVal1, NumericVal2, NumericVal3, NumericVal4, NumericVal5,\
                                                                     Checklist1, Checklist2, Checklist3, Checklist4, Checklist5))
    con.commit()
    con.close()


def viewData():
    con = sqlite3.connect("station.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM station")
    rows = cur.fetchall()
    con.close()
    return rows

def deleteRec(id):
    con = sqlite3.connect("station.db")
    cur = con.cursor()
    cur.execute("DELETE FROM station WHERE id=?",(id,))
    con.commit()
    con.close()
    

def searchData(Line="",Shift="",WorkstationID="",WorkstationName="",TesterID="",TesterName="",InspectionItemID="",InspectionItemType="",\
               Descripton="", InspectionGroupID="", Test1="", Test2="", Test3="", Test4="", Test5="", NumericVal1="", NumericVal2="", NumericVal3="", NumericVal4="", NumericVal5="",\
                                                                     Checklist1="", Checklist2="", Checklist3="", Checklist4="", Checklist5=""):
    con = sqlite3.connect("station.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM station WHERE Line=? OR Shift=? OR WorkstationID =? OR WorkstationName =? OR TesterID =? OR TesterName =? OR InspectionItemID =? OR InspectionItemType =? OR Descripton =? OR InspectionGroupID =? OR Test1 =? OR Test2 =?\
                 OR Test3 =? OR Test4  =? OR Test5 =? OR NumericVal1 =? OR NumericVal2 =? OR NumericVal3 =? OR NumericVal4 =? OR NumericVal5 =?\
                 OR Checklist1 =? OR Checklist2 =? OR Checklist3 =? OR Checklist4 =? OR Checklist5 =?",(Line, Shift, WorkstationID, WorkstationName,\
                                                                     TesterID, TesterName,InspectionItemID, InspectionItemType,\
                                                                     Descripton, InspectionGroupID, Test1, Test2, Test3, Test4, Test5, NumericVal1, NumericVal2, NumericVal3, NumericVal4, NumericVal5,\
                                                                     Checklist1, Checklist2, Checklist3, Checklist4, Checklist5))            
    rows = cur.fetchall()
    con.close()
    return rows

def dataUpdate(id,Line="",Shift="",WorkstationID="",WorkstationName="",TesterID="",TesterName="",InspectionItemID="",InspectionItemType="",\
               Descripton="", InspectionGroupID="", Test1="", Test2="", Test3="", Test4="", Test5="", NumericVal1="", NumericVal2="", NumericVal3="", NumericVal4="", NumericVal5="",\
                                                                     Checklist1="", Checklist2="", Checklist3="", Checklist4="", Checklist5=""):
    con = sqlite3.connect("station.db")
    cur = con.cursor()
    cur.execute("UPDATE station SET Line=?,Shift=?,WorkstationID=?,WorkstationName=?,TesterID=?,TesterName=?,InspectionItemID=?,InspectionItemType=?,\
               Descripton=?, InspectionGroupID=?, Test1=?, Test2=?, Test3=?, Test4=?, Test5=?, NumericVal1=?, NumericVal2=?, NumericVal3=?, NumericVal4=?, NumericVal5=?,\
                                                                     Checklist1=?, Checklist2=?, Checklist3=?, Checklist4=?, Checklist5=?, WHERE id=? ", (Line, Shift, WorkstationID, WorkstationName,\
                                                                     TesterID, TesterName,InspectionItemID, InspectionItemType,\
                                                                     Descripton, InspectionGroupID, Test1, Test2, Test3, Test4, Test5, NumericVal1, NumericVal2, NumericVal3, NumericVal4, NumericVal5,\
                                                                     Checklist1, Checklist2, Checklist3, Checklist4, Checklist5,id))            
    con.commit()
    con.close()


stationData()
