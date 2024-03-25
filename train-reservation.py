from tabulate import tabulate
import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="Hari@392002hp", database="python_aa")


def insert(name, age, mobile_no, train_name,train_number,destination):
    res = con.cursor()
    sql = "insert into tickets_aa (name,age,mobile_no,train_name,train_number,destination) values (%s,%s,%s,%s,%s,%s)"
    user = (name, age, mobile_no,train_name,train_number,destination)
    res.execute(sql, user)
    con.commit()
    print("Data Insert Success")


def update(name, age, mobile_no, train_name, train_number, destination, id):
    try:
        sql = "UPDATE tickets_aa SET name=%s, age=%s, mobile_no=%s, train_name=%s, train_number=%s, destination=%s WHERE id=%s"
        user= (name, age, mobile_no, train_name, train_number, destination, id)
        res=con.cursor()
        res.execute(sql,user)
        print("Data Updated Successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")



def select():
    res = con.cursor()
    sql = "SELECT ID,NAME,AGE,MOBILE_NO,TRAIN_NAME,TRAIN_NUMBER,DESTINATION from tickets_aa"
    res.execute(sql)
    result = res.fetchall()
    print(tabulate(result, headers=["ID", "NAME", "AGE", "MOBILE_NO", "TRAIN_NAME", "TRAIN_NUMBER", "DESTINATION"]))


def delete(id):
    res = con.cursor()
    sql = "delete from tickets_aa where id=%s"
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
        name = input("Enter Name : ")
        age = input("Enter Age : ")
        mobile_no = input("Enter mobile_no: ")
        train_name = input("Enter train_name : ")
        train_number = input("Enter train_number: ")
        destination = input("Enter destination: ")
        insert(name, age, mobile_no, train_name, train_number, destination )
    elif choice == 2:
        id = input("Enter The Id : ")
        name = input("Enter Name : ")
        age = input("Enter Age : ")
        mobile_no = input("Enter mobile_no: ")
        train_name = input("Enter train_name : ")
        train_number = input("Enter train_number: ")
        destination = input("Enter destination: ")
        update(name, age, mobile_no, train_name, train_number, destination ,id)
    elif choice == 3:
        select()
    elif choice == 4:
        id = input("Enter The Id to Delete : ")
        delete(id)
    elif choice == 5:
        quit()
    else:
        print("Invalid Selection . Please Try")