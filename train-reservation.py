from tabulate import tabulate
import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="Hari@392002hp", database="python_vv")


def insert(name, journey_date, coach,seat_no,gender,train_no,train_name,origin,destination,Rs):
    res = con.cursor()
    sql = "insert into tickets_vv (name,journey_date,coach,seat_no,gender,train_no,train_name,origin,destination,Rs) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    user = (name, journey_date, coach,seat_no,gender,train_no,train_name,origin,destination,Rs)
    res.execute(sql, user)
    con.commit()
    print("Data Insert Success")


def update(name, journey_date, coach,seat_no,gender,train_no,train_name,origin,destination,Rs, id):
    try:
        sql = "UPDATE tickets_vv SET name=%s, journey_date=%s, coach=%s,seat_no=%s,gender=%s,train_no=%s,train_name=%s,origin=%s,destination=$s,Rs=%s WHERE id=%s"
        user= (name, journey_date, coach,seat_no,gender,train_no,train_name,origin,destination,Rs, id)
        res=con.cursor()
        res.execute(sql,user)
        print("Data Updated Successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")



def select():
    res = con.cursor()
    sql = "SELECT ID,NAME,JOURNEY_DATE,COACH,SEAT_NO,GENDER,TRAIN_NO,TRAIN_NAME,ORIGIN,DESTINATION,RS from tickets_vv"
    res.execute(sql)
    result = res.fetchall()
    print(tabulate(result, headers=["ID","NAME","JOURNEY_DATE","COACH","SEAT_NO","GENDER","TRAIN_NO","TRAIN_NAME","ORIGIN","DESTINATION","RS"]))


def delete(id):
    res = con.cursor()
    sql = "delete from tickets_VV where id=%s"
    user = (id,)
    res.execute(sql, user)
    con.commit()
    print("Data Delete Success")



while True:
    print("1.Insert Data")
    print("2.Update Data")
    print("3.Select Data")
    print("4.Delete Data")
    print("5.Exit")
    choice = int(input("Enter Your Choice : "))
    if choice == 1:
        NAME = input("ENTER NAME : ")
        JOURNEY_DATE = input("ENTER JOURNEY-DATE : ")
        COACH = input("ENTER COACH : ")
        SEAT_NO = input("ENTER SEAT-NO: ")
        GENDER = input("ENTER GENDER: ")
        TRAIN_NO = input("ENTER TRAIN_NO : ")
        TRAIN_NAME = input("ENTER TRAIN_NAME : ")
        ORIGIN = input("ENTER START : ")
        DESTINATION = input("ENTER DESTINATION : ")
        RS = input("ENTER AMOUNT : ")
        insert(NAME,JOURNEY_DATE,COACH,SEAT_NO,GENDER,TRAIN_NO,TRAIN_NAME,ORIGIN,DESTINATION,RS)
    elif choice == 2:
        Id = input("Enter The ID : ")
        NAME = input("ENTER NAME : ")
        JOURNEY_DATE = input("ENTER JOURNEY-DATE : ")
        COACH = input("ENTER COACH : ")
        SEAT_NO = input("ENTER SEAT-NO: ")
        GENDER = input("ENTER GENDER: ")
        TRAIN_NO = input("ENTER TRAIN_NO : ")
        TRAIN_NAME = input("ENTER TRAIN_NAME : ")
        ORIGIN = input("ENTER START : ")
        DESTINATION = input("ENTER DESTINATION : ")
        RS = input("ENTER AMOUNT : ")
        update(NAME,JOURNEY_DATE,COACH,SEAT_NO,GENDER,TRAIN_NO,TRAIN_NAME,ORIGIN,DESTINATION,RS,Id)
    elif choice == 3:
        select()
    elif choice == 4:
        id = input("Enter The Id to Delete : ")
        delete(id)
    elif choice == 5:
        quit()
    else:
        print("Invalid Selection . Please Try")