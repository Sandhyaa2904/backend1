from flask import Flask, request
import sqlite3
app=Flask(__name__)
@app.get('/')
def hi():
    return "good night"

@app.post('/r')
def hi1():
    con = sqlite3.Connection("C:/Users/trc/Desktop/mycode/task/Scripts/task.db")
    cur=con.cursor()
    data = request.get_json()
    Name=data["Name"]
    Rollno=data["Rollno"]
    Mark=data["Mark"]
    students=(Name,Rollno,Mark)
    cur.execute("create table if not exists students(name varchar(255),Rollno varchar(255),Mark int)")
    cur.execute("insert into students values(?,?,?)",students)
    con.commit()
    con.close()
    print(data)
    return "we got the data"


app.run(debug=True)