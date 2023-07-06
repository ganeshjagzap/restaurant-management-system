"""
Note:
    project in progress

"""

import mysql.connector as a
import datetime

con = a.connect(host="localhost", user="root", passwd="")
c = con.cursor()
c.execute("show databases")
dl = c.fetchall()
dl2 = []
for i in dl:
    dl2.append(i[0])
if "rest1" in dl2:
    sql = "use rest1"
    c.execute(sql)
else:
    sql1 = "create database rest1"
    c.execute(sql1)
    sql2 = "use rest1"
    c.execute(sql2)
    sql3 = "create table if not exists dish(Dish_name varchar(20),Cost int ,Cook_name varchar(30),Dish_id int primary key)"
    c.execute(sql3)
    sql4 = "create table if not exists orders(Dish_id int,Cost int,Time varchar(30),Customer_phone_no varchar(30) primary key,Customer_name varchar(30)," \
           "Table_no int(3))"
    c.execute(sql4)
    sql5 = "create table if not exists cook(Cook_id varchar(10) primary key,Cook_name varchar(30),Cook_adhar bigint(11) ,Phone_phone_no bigint(11),Salary int , Doj varchar(30)," \
           "Recipe_specialist varchar(40))"
    c.execute(sql5)
    sql6 = "create table if not exists cleaner(Cleaner_id varchar(10) primary key,Cleaner_name varchar(30),Cleaner_adhar bigint(11) ,Cleaner_phone_no bigint(11),Salary int , Doj varchar(30))"
    c.execute(sql6)
    sql7 = "create table if not exists manager(Manager_id varchar(10) primary key,Manager_name varchar(30),Manager_adhar bigint(11) ,Manager_phone_no bigint(11),Salary int , Doj varchar(30))"
    c.execute(sql7)

    sql8 = "create table if not exists salary(Job_id varchar(30),Employee_name varchar(30),Date_of_paid varchar(15),Working_days int,Bank_account_no varchar(30),Salary int,Net_salary int)"
    c.execute(sql8)
    sql9 = "create table if not exists Expenditure(Type varchar(30),cost int,date varchar(30))"
    c.execute(sql9)
    sql10 = "create table if not exists Bill_c(Customer_phone_no bigint(11),Customer_name varchar(30),Order_dish_id int,Order_dish_cost int)"
    c.execute(sql10)
    con.commit()

def singin():
    print("\n")
    print("------------------------------- Welcome to DPU cafe -------------------------------\n")
    p = input("password:")
    if (p == "1111"):
        options()

    else:
        singin()

# Display optons

def options():
    print("\n1. Dish\n2. Cook \n3. Manager \n4. Cleaner \n5. salary\n6. Orders\n7. income\n8. Expenditure\n9. Bill")
    print("\n")
    choice = input("Select option : ")
    while True:
        if (choice == "1"):
            Dishfuc()
        elif (choice == "2"):
            Cookfunc()
        elif(choice=="3"):
            Managerfunc()
        elif(choice=="4"):
            Cleanerfunc()
        elif (choice == "5"):
            Paysalary()
        elif (choice == "6"):
            Neworder()
        elif (choice == "7"):
            Netincome()
        elif (choice == "8"):
            Expenditure()
        elif(choice=="9"):
            Bill()
        else:
            print("wrong choice")

class Dish:

    def Add_dish(self):
        print("Available Dishes ")
        sql = "select * from dish"
        c = con.cursor()
        c.execute(sql)
        d = c.fetchall()
        if (len(d) == 0):
            print("No dish available")
        for i in d:
            print(i[0], " - ", i[1], " - ", i[2], " - ", i[3], "\n")

        did = int(input('Enter dish id :'))
        sql = "select Dish_id from dish"
        c = con.cursor()
        c.execute(sql)
        d = c.fetchall()
        print(d)
        for i in d:
            if (did in i):
                print("This dish is already present")
                return

        dn = input("Dish name : ")
        dc = input("Dish cost : ")
        sql = "Select Cook_name ,Recipe_specialist from cook"
        c = con.cursor()
        c.execute(sql)
        d = c.fetchall()
        if (len(d) == 0):
            print("no cook available")
            print("please add cook first ")
            options()
        for i in d:
            print(i[0], " - ", i[1])

        print("\n")
        print("Available cooks with recipe type")
        cb = input("Cook by :")

        if(Dish.Cook_select(self,cb,d)==1):
            data = (dn, dc, cb, did)
            sql = "insert into dish values(%s,%s,%s,%s)"
            c = con.cursor()
            c.execute(sql, data)
            con.commit()
            print("data entered ")


    def Cook_select(self,cb,d):
        for i in d:
            if (cb not in i):
                print('this cook is not in the list, please select available cook')
                cb=input("Cook by")
                Dish.Cook_select(self,cb,d)
        return 1


    def Remove_dish(self):
        dn = input("dish name :")
        did = int(input("Dish id :"))
        sql = "select * from dish"
        c = con.cursor()
        c.execute(sql)
        d = c.fetchall()
        if (len(d) == 0):
            print("No dish available so no did to delete ")
        else:
            print("confer dish before deleting")
            sql = f"select * from dish where Dish_id={did}"
            c=con.cursor()
            c.execute(sql)
            d = c.fetchall()
            for i in d:
                print(i[0], " - ", i[1], " - ", i[2], " - ", i[3], "\n")

            print("Is this dish you want to delete , Yes/No")
            ans = input()
            if (ans == "Yes" or ans == "yes"):
                data = (dn, did)
                sql = "delete from dish where Dish_name=%s and Dish_id=%s"
                c = con.cursor()
                c.execute(sql, data)
                con.commit()
                print("data updated successfully")
            else:
                Dish()


    def Display_dish(self):
        print("\n")
        sql = "select * from dish"
        c = con.cursor()
        c.execute(sql)
        d = c.fetchall()
        for i in d:
            print(i[0], " - ", i[1], " - ", i[2], " - ", i[3], "\n")


def Dishfuc():
    choice = input("\n1. Add \n2. Remove \n3. display\n4. main menu")
    dish = Dish()
    if choice == "1":
        dish.Add_dish()
    elif choice == "2":
        dish.Remove_dish()
    elif choice == "3":
        dish.Display_dish()
    else:
        options()


def Cookfunc():
    choice = input("\n1. Add \n2. Remove \n3. display\n4. main menu")
    cook=Cook()
    if choice == "1":
        cook.Add_cook()
    elif choice == "2":
        cook.Remove_cook()
    elif choice == "3":
        cook.Display_cook()
    else:
        options()


class Cook:

    def Add_cook(self):
        cid=input("Cood Id : ")
        if(Cook.Check_id(self,cid)==0):
            print("This cook is already present , no need to insert")
            return
        cn = input("Cook Name : ")
        ca=int(input("Cood Adhar : "))
        cp = int(input("Cook phone_no : "))
        s = int(input("Cook salary : "))
        doj = input("Date of joining (yyyy/mm/dd): ")
        rs=input("recipe specialist : ")

        data = (cid, cn, ca, cp, s, doj, rs)
        sql = "INSERT INTO cook VALUES (%s, %s, %s, %s, %s, %s, %s)"

        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("data inserted successfully")

    def Check_id(self,cid):
        sql="select * from cook"
        c=con.cursor()
        c.execute(sql)
        d=c.fetchall()
        for i in d:
            if(cid in i):
                return 0
        return 1

    def Remove_cook(self):
        print("\ntotal cook")
        sql = "select * from cook"
        c = con.cursor()
        c.execute(sql)
        d = c.fetchall()
        if(len(d)==0):
            print("No cook available , so can't remove anyone")
            return

        print("\nC_id", "-- ","C_name", "--", "C_adhar", "--","C_phone", "--","C_salary", "--","C_DOJ", "--","Recipe specialist")
        for i in d:
            print(i[0], " - ", i[1], " - ", i[2], " - ", i[3], " - ", i[4], " - ", i[5], " - ", i[6])

        cId = input("cook id :")
        cn=input("Cook name :")
        print("confirm cook before deleting ")
        for i in d:
            if(cId in i):
                print(i[0], " - ", i[1], " - ", i[2], " - ", i[3], " - ", i[4], " - ", i[5], " - ", i[6])
        print("Want to remove this cook Yes/No")
        ans=input()
        if(ans=="yes" or ans=='Yes'):
            data = (cId,cn)
            sql = "delete from cook where Cook_id=%s and Cook_name=%s"
            c = con.cursor()
            c.execute(sql, data)
            con.commit()
            print("data updated successfully")
        else:
            return
    def Display_cook(self):
        sql = "select * from cook"
        c = con.cursor()
        c.execute(sql)
        d = c.fetchall()
        if(len(d)==0):
            print("No cook available ")
            return
        print("\nC_id", "-- ","C_name", "--", "C_adhar", "--","C_phone", "--","C_salary", "--","C_DOJ", "--","Recipe specialist")
        for i in d:
            print(i[0], " - ", i[1], " - ", i[2], " - ", i[3], " - ", i[4], " - ", i[5], " - ", i[6])
        print("\n")


def Managerfunc():
    choice = input("\n1. Add \n2. Remove \n3. display\n4. main menu")
    manager=Manager()
    if choice == "1":
        manager.Add_Manager()
    elif choice == "2":
        manager.Remove_manager()
    elif choice == "3":
        manager.Display_manager()
    else:
        options()

class Manager():
    def Add_Manager(self):
        mid = input("Manager Id : ")
        if (Manager.Check_id(self, mid) == 0):
            print("This Manager is already present , no need to insert")
            return
        mn = input("Manager Name : ")
        ma = int(input("Manager Adhar : "))
        mp = int(input("Manager phone_no : "))
        s = int(input("Manager salary : "))
        doj = input("Date of joining (yyyy/mm/dd): ")

        data = (mid, mn, ma, mp, s, doj )
        sql = "INSERT INTO manager VALUES (%s, %s, %s, %s, %s, %s)"

        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("data inserted successfully")

    def Check_id(self, mid):
        sql = "select * from manager"
        c = con.cursor()
        c.execute(sql)
        d = c.fetchall()
        for i in d:
            if (mid in i):
                return 0
        return 1

    def Remove_manager(self):
        print("\ntotal manager")
        sql = "select * from manager"
        c = con.cursor()
        c.execute(sql)
        d = c.fetchall()
        if (len(d) == 0):
            print("No manager available , so can't remove anyone")
            return

        print("\nM_id", "-- ", "M_name", "--", "M_adhar", "--", "M_phone", "--", "M_salary", "--", "M_DOJ")
        for i in d:
            print(i[0], " - ", i[1], " - ", i[2], " - ", i[3], " - ", i[4], " - ", i[5])

        MId = input("Manager id :")
        Mn = input("Manager name :")
        print("confirm Manager before deleting ")
        for i in d:
            if (MId in i):
                print(i[0], " - ", i[1], " - ", i[2], " - ", i[3], " - ", i[4], " - ", i[5])
        print("Want to remove this Manager Yes/No")
        ans = input()
        if (ans == "yes" or ans == 'Yes'):
            data = (MId, Mn)
            sql = "delete from manager where Manager_id=%s and Manager_name=%s"
            c = con.cursor()
            c.execute(sql, data)
            con.commit()
            print("data updated successfully")
        else:
            return

    def Display_manager(self):
        sql = "select * from manager"
        c = con.cursor()
        c.execute(sql)
        d = c.fetchall()
        if (len(d) == 0):
            print("No manager available ")
            return
        print("\nM_id", "-- ", "M_name", "--", "M_adhar", "--", "M_phone", "--", "M_salary", "--", "M_DOJ")
        for i in d:
            print(i[0], " - ", i[1], " - ", i[2], " - ", i[3], " - ", i[4], " - ", i[5])

    print("\n")

def Cleanerfunc():
    choice = input("\n1. Add \n2. Remove \n3. display\n4. main menu")
    cleaner=Cleaner()
    if choice == "1":
        cleaner.Add_cleaner()
    elif choice == "2":
        cleaner.Remove_cleaner()
    elif choice == "3":
        cleaner.Display_cleaner()
    else:
        options()

class Cleaner():
    def Add_cleaner(self):
        clid = input("Cleaner Id : ")
        if (Cleaner.Check_id(self, clid) == 0):
            print("This Cleaner is already present , no need to insert")
            return
        cln = input("Cleaner Name : ")
        cla = int(input("Cleaner Adhar : "))
        clp = int(input("Cleaner phone_no : "))
        s = int(input("Cleaner salary : "))
        doj = input("Date of joining (yyyy/mm/dd): ")

        data = (clid, cln, cla, clp, s, doj )
        sql = "INSERT INTO cleaner VALUES (%s, %s, %s, %s, %s, %s)"

        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("data inserted successfully")

    def Check_id(self, clid):
        sql = "select * from cleaner"
        c = con.cursor()
        c.execute(sql)
        d = c.fetchall()
        for i in d:
            if (clid in i):
                return 0
        return 1

    def Remove_cleaner(self):
        print("\ntotal Cleaner")
        sql = "select * from cleaner"
        c = con.cursor()
        c.execute(sql)
        d = c.fetchall()
        if (len(d) == 0):
            print("No Cleaner available , so can't remove anyone")
            return

        print("\ncl_id", "-- ", "cl_name", "--", "cl_adhar", "--", "cl_phone", "--", "cl_salary", "--", "cl_DOJ")
        for i in d:
            print(i[0], " - ", i[1], " - ", i[2], " - ", i[3], " - ", i[4], " - ", i[5])

        MId = input("Cleaner id :")
        Mn = input("Cleaner name :")
        print("confirm Cleaner before deleting ")
        for i in d:
            if (MId in i):
                print(i[0], " - ", i[1], " - ", i[2], " - ", i[3], " - ", i[4], " - ", i[5])
        print("Want to remove this Cleaner Yes/No")
        ans = input()
        if (ans == "yes" or ans == 'Yes'):
            data = (MId, Mn)
            sql = "delete from cleaner where Cleaner_id=%s and Cleaner_name=%s"
            c = con.cursor()
            c.execute(sql, data)
            con.commit()
            print("data updated successfully")
        else:
            return

    def Display_cleaner(self):
        sql = "select * from cleaner"
        c = con.cursor()
        c.execute(sql)
        d = c.fetchall()
        if (len(d) == 0):
            print("No Cleaner available ")
            return
        print("\ncl_id", "-- ", "cl_name", "--", "cl_adhar", "--", "cl_phone", "--", "cl_salary", "--", "cl_DOJ")
        for i in d:
            print(i[0], " - ", i[1], " - ", i[2], " - ", i[3], " - ", i[4], " - ", i[5])

    print("\n")


# pay cook's salary

def Paysalary():
    sql = "select * from cook"
    c = con.cursor()
    c.execute(sql)
    d = c.fetchall()
    for i in d:
        print(i[0], " - ", i[1], " - ", i[2], " - ", i[3], " - ", i[4])
        print("_________________________________________________________________")
    cn = input("cook name : ")
    cp = input("cook phone number : ")
    ba = input("bank account : ")
    date = input("Date(yyyy/mm/dd) : ")
    s = int(input("salary : "))
    d = int(input("Working days : "))
    ns = (s / 30) * d
    data = (cn, cp, date,ba,  s,  ns)
    sql = "insert into salary values(%s,%s,%s,%s,%s,%s)"
    c = con.cursor()
    c.execute(sql, data)
    con.commit()

    print("Net salary paid : ", ns, " Rs ")
    print("---------------------------------------------")
    xy = input("1. salary menu    2. main menu")
    print("----------------------------------------------")
    if xy == "1":
        Paysalary()
    elif xy == '2':
        options()
    else:
        options()


# make new order

def Neworder():
    sql = "select * from dish"
    c = con.cursor()
    c.execute(sql)
    d = c.fetchall()
    print("dishid --- name --- Cost ---cook")
    for i in d:
        print(i[0], " - ", i[1], " - ", i[2], " - ", i[3])
    print("\n")
    dil = []
    while True:
        di = input("Select Dish Id {0 When Done} :")
        if di == "0":
            break
        else:
            dil.append(di)
    sql = "select Did,Dcost from dish"
    c = con.cursor()
    c.execute(sql)
    d = c.fetchall()
    dicl = {}
    for i in d:
        dicl[i[0]] = i[1]
    tc = 0
    for i in dil:
        dc = dicl[i]
        tc = tc + dc
    dt = input("Date (yyyy/mm/dd) : ")
    cn = input("Customer name : ")
    cp = input("customer phone number")
    lis = input("enter dish ids : ")
    data = (lis, tc, dt, cn, cp)
    sql = "insert into orders values(%s,%s,%s,%s,%s)"
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("Total amount : ", tc, " Rs")
    print("Data entered successfully")
    print("--------------------------------------------")
    xy = input("1. order menu         2. main menu : ")
    if xy == '1':
        Neworder()
    else:
        options()

def Bill():
    pass
# monthly net income

def Netincome():
    c = con.cursor()
    t = input("\n1. All   2. Year   3. Month   4. Date   5. main menu")
    if t == "1":
        sql = "select cost from orders"
        c.execute(sql)
        d = c.fetchall()
        oi = 0
        for i in d:
            oi = oi + i[0]
        print("Total income from orders : ", oi, " Rs")
    else:
        options()


# make new expenditure
def Expenditure():
    choice = input("\n1. Bill entry   2. show bills   3. main menu  :")
    if choice == "1":
        t = input("type : ")
        c = int(input("cost : "))
        d = input("Date : ")
        data = (t, c, d)
        sql = "insert into Expenditure values(%s,%s,%s)"
        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("Data Entered successfully")
        options()
    elif choice == "2":
        c = con.cursor()
        t = input("1. All   2. Year   3. Month   4. Date : ")
        if t == "1":
            sql = "select * from Expenditure"
            c.execute(sql)
            d = c.fetchall()
            for i in d:
                print(i)
        elif t == "2":
            y = input("Enter year : ")
            sql = "Select * from Expenditure"
            c.execute(sql)
            d = c.fetchall()
            for i in d:
                if y in i[2]:
                    print(i)
        elif t == "3":
            y = input("Enter : year/month : ")
            sql = "select * from Expenditure"
            c.execute(sql)
            d = c.fetchall()
            for i in d:
                if y in i[2]:
                    print(i)
        elif t == "4":
            y = input("Enter Data : ")
            sql = "select * from Expenditure"
            c.execute(sql)
            d = c.fetchall()
            for i in d:
                if y in i[2]:
                    print(i)
        else:
            options()
    elif choice=='3':
        options()
singin()

