import mysql.connector as a
import datetime
import numpy as np

con = a.connect(host="localhost", user="root", passwd="")
c = con.cursor()
c.execute("show databases")
dl = c.fetchall()
dl2 = []
for i in dl:
    dl2.append(i[0])
if "rest3" in dl2:
    sql = "use rest3"
    c.execute(sql)
else:
    sql1 = "create database rest3"
    c.execute(sql1)
    sql2 = "use rest3"
    c.execute(sql2)
    sql3 = "create table if not exists dish(Dish_name varchar(20),Cost int ,Cook_name varchar(30),Dish_id int primary key)"
    c.execute(sql3)
    sql4 = "create table if not exists orders(Dish_id varchar(30),Cost int,Date varchar(15),Time varchar(15),Customer_phone_no varchar(30) primary key,Customer_name varchar(30)," \
           "Table_no varchar(10),Status varchar(10),Bill varchar(10))"
    c.execute(sql4)
    sql5 = "create table if not exists cook(Cook_id varchar(10) primary key,Cook_name varchar(30),Cook_adhar bigint(11) ,Phone_phone_no bigint(11),Salary int ,Bank_account varchar(20), Doj varchar(30)," \
           "Recipe_specialist varchar(40))"
    c.execute(sql5)
    sql6 = "create table if not exists cleaner(Cleaner_id varchar(10) primary key,Cleaner_name varchar(30),Cleaner_adhar bigint(11) ,Cleaner_phone_no bigint(11),Salary int ,Bank_account varchar(20), Doj varchar(30))"
    c.execute(sql6)
    sql7 = "create table if not exists manager(Manager_id varchar(10) primary key,Manager_name varchar(30),Manager_adhar bigint(11) ,Manager_phone_no bigint(11),Salary int ,Bank_account varchar(20), Doj varchar(30))"
    c.execute(sql7)
    sql8 = "create table if not exists salary(Job_id varchar(30),Employee_name varchar(30),Date_of_paid varchar(15),Working_days int,Bank_account_no varchar(30),Salary int,Net_salary int)"
    c.execute(sql8)
    sql9 = "create table if not exists Expenditure(Type varchar(30),cost int,date varchar(30))"
    c.execute(sql9)
    sql10 = "create table if not exists completed_orders(Dish_id varchar(30),Cost int ,Date varchar(15),Time varchar(15),Customer_phone_no bigint(11),Customer_name varchar(30),Table_no varchar(10)," \
            "Order_status varchar(10),Bill varchar(10))"
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
            dishfuc()
        elif (choice == "2"):
            cookfunc()
        elif(choice=="3"):
            managerfunc()
        elif(choice=="4"):
            cleanerfunc()
        elif (choice == "5"):
            paysalaryfunc()
        elif (choice == "6"):
            neworderfunc()
        elif (choice == "7"):
            Netincome()
        elif (choice == "8"):
            expenditurefunc()
        elif(choice=="9"):
            billfunc()
        else:
            print("wrong choice")
            options()
            

class Dish:

    def Add_dish(self):
        print("\nAvailable Dishes ")
        sql = "select * from dish"
        c = con.cursor()
        c.execute(sql)
        d = c.fetchall()
        if (len(d) == 0):
            print("\nNo dish available")
        print("dish name -- dish cost -- cook by -- cook id")
        for i in d:
            print(i[0], " - ", i[1], " - ", i[2], " - ", i[3], "\n")

        did = int(input('Enter dish id :'))
        sql = "select Dish_id from dish"
        c = con.cursor()
        c.execute(sql)
        d = c.fetchall()

        for i in d:
            if (did in i):
                print("This dish is already present")
                return

        dn = input("Dish name : ")
        dc = input("Dish cost : ")
        sql = "Select Cook_name ,Recipe_specialist,Cook_id from cook"
        c = con.cursor()
        c.execute(sql)
        d = c.fetchall()
        if (len(d) == 0):
            print("\nno cook available")
            print("please add cook first ")
            options()

        print("\n")
        print("Available cooks with recipe type")
        print("\nCook name -- Recipe_specialist -- cook id")
        for i in d:
            print(i[0], "  -  ", i[1]," -  ",i[2])

        cb = input("Cook  (id):")

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
        # dn = input("dish name :")

        sql = "select * from dish"
        c = con.cursor()
        c.execute(sql)
        d = c.fetchall()
        did_list=np.array(d).flatten()
        if (len(d) == 0):
            print("No dish available so no need to delete ")

        else:
            did = int(input("Dish id :"))
            if(str(did)not in did_list):
                print("Enter correct dish id :")
                Dish.Remove_dish(self)
            print("confer dish before deleting")
            print("dish name -- dish cost -- cook by -- cook id")
            sql = f"select * from dish where Dish_id={did}"
            c=con.cursor()
            c.execute(sql)
            d = c.fetchall()
            for i in d:
                print(i[0], " - ", i[1], " - ", i[2], " - ", i[3], "\n")

            print("Is this dish you want to delete , Yes/No")
            ans = input()
            if (ans == "Yes" or ans == "yes"):

                sql = f"delete from dish where Dish_id='{did}'"
                c = con.cursor()
                c.execute(sql)
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
        if(len(d)==0):
            print("\nNo dish available")
            return
        print("dish name -- dish cost -- cook by -- cook id")
        for i in d:
            print(i[0], " - ", i[1], " - ", i[2], " - ", i[3], "\n")


def dishfuc():
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


def cookfunc():
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
        Cook.Display_cook(self)
        cid=input("Cood Id (c_): ")
        if(Cook.Check_id(self,cid)==0):
            print("This cook is already present , no need to insert")
            return
        cn = input("Cook Name : ")
        ca = int(input("Cook Adhar : "))
        cp = int(input("Cook phone_no : "))
        s = int(input("Cook salary : "))
        doj = input("Date of joining (yyyy/mm/dd): ")
        rs=input("recipe specialist : ")
        ba = input("Bank account no. :")
        data = (cid, cn, ca, cp, s, ba,doj, rs)
        sql = "INSERT INTO cook VALUES (%s, %s, %s, %s, %s, %s,%s, %s)"

        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("data inserted successfully")
        return

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

        print("\nC_id", "-- ","C_name", "--", "C_adhar", "--","C_phone", "--","C_salary","C_bank", "--","C_DOJ", "--","Recipe specialist")
        for i in d:
            print(i[0], " - ", i[1], " - ", i[2], " - ", i[3], " - ", i[4], " - ", i[5], " - ", i[6]," - ",i[7])

        cId = input("cook id :")
        flag=0
        for i in d:
            if(cId in i):
                print(i[0], " - ", i[1], " - ", i[2], " - ", i[3], " - ", i[4], " - ", i[5], " - ", i[6])
                flag=1
        if(flag==0):
            print("This cook is not available,so no need to delete")
            return

        print("confirm cook before deleting ")
        print("Want to remove this cook Yes/No")
        ans=input()
        if(ans=="yes" or ans=='Yes'):

            sql = f"delete from cook where Cook_id='{cId}'"
            c = con.cursor()
            c.execute(sql)
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
        print("\nC_id", "-- ","C_name", "--", "C_adhar", "--","C_phone", "--","C_salary","C_bank", "--","C_DOJ", "--","Recipe specialist")
        for i in d:
            print(i[0], " - ", i[1], " - ", i[2], " - ", i[3], " - ", i[4], " - ", i[5], " - ", i[6]," - ",i[7])
        print("\n")


def managerfunc():
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
        Manager.Display_manager(self)
        mid = input("Manager Id (m_) : ")
        if (Manager.Check_id(self, mid) == 0):
            print("This Manager is already present , no need to insert")
            return
        mn = input("Manager Name : ")
        ma = int(input("Manager Adhar : "))
        mp = int(input("Manager phone_no : "))
        s = int(input("Manager salary : "))
        ba=input("Bank account no. :")
        doj = input("Date of joining (yyyy/mm/dd): ")

        data = (mid, mn, ma, mp, s,ba, doj )
        sql = "INSERT INTO manager VALUES (%s, %s, %s, %s, %s, %s,%s)"

        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("data inserted successfully")
        return
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

        print("\nM_id", "-- ", "M_name", "--", "M_adhar", "--", "M_phone", "--", "M_salary","M_bank", "--", "M_DOJ")
        for i in d:
            print(i[0], " - ", i[1], " - ", i[2], " - ", i[3], " - ", i[4], " - ", i[5]," - ",i[6])


        MId = input("Manager id :")
        flag=0
        for i in d:
            if (MId in i):
                print("\nM_id", "-- ", "M_name", "--", "M_adhar", "--", "M_phone", "--", "M_salary", "M_bank", "--",
                      "M_DOJ")
                print(i[0], " - ", i[1], " - ", i[2], " - ", i[3], " - ", i[4], " - ", i[5]," - ",i[6])
                flag = 1
        if (flag == 0):
            print("This manager is not available,so no need to delete")
            return
        print("Want to remove this Manager Yes/No")
        ans = input()
        if (ans == "yes" or ans == 'Yes'):
            sql = f"delete from manager where Manager_id='{MId}'"
            c = con.cursor()
            c.execute(sql)
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
        print("\nM_id", "-- ", "M_name", "--", "M_adhar", "--", "M_phone", "--", "M_salary","M_bank", "--", "M_DOJ")
        for i in d:
            print(i[0], " - ", i[1], " - ", i[2], " - ", i[3], " - ", i[4], " - ", i[5]," - ",i[6])

    print("\n")

def cleanerfunc():
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
        Cleaner.Display_cleaner(self)
        clid = input("Cleaner Id (cl_) : ")
        if (Cleaner.Check_id(self, clid) == 0):
            print("This Cleaner is already present , no need to insert")
            return
        cln = input("Cleaner Name : ")
        cla = int(input("Cleaner Adhar : "))
        clp = int(input("Cleaner phone_no : "))
        s = int(input("Cleaner salary : "))
        ba=input("Bank Account No. :")
        doj = input("Date of joining (yyyy/mm/dd): ")

        data = (clid, cln, cla, clp, s,ba, doj )
        sql = "INSERT INTO cleaner VALUES (%s, %s, %s, %s, %s, %s,%s)"

        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("data inserted successfully")
        return
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

        print("\ncl_id", "-- ", "cl_name", "--", "cl_adhar", "--", "cl_phone", "--", "cl_salary","cl_bank", "--", "cl_DOJ")

        for i in d:
            print(i[0], " - ", i[1], " - ", i[2], " - ", i[3], " - ", i[4], " - ", i[5]," - ",i[6])

        clId = input("Cleaner id :")
        flag=0
        for i in d:
            if (clId in i):
                print("\ncl_id", "-- ", "cl_name", "--", "cl_adhar", "--", "cl_phone", "--", "cl_salary", "cl_bank",
                      "--", "cl_DOJ")
                print(i[0], " - ", i[1], " - ", i[2], " - ", i[3], " - ", i[4], " - ", i[5]," - ",i[6])
                flag=1
        if (flag == 0):
            print("This Cleaner is not available,so no need to delete")
            return
        print("Want to remove this Cleaner Yes/No")
        ans = input()
        if (ans == "yes" or ans == 'Yes'):
            sql = f"delete from cleaner where Cleaner_id='{clId}'"
            c = con.cursor()
            c.execute(sql)
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
        print("\ncl_id", "-- ", "cl_name", "--", "cl_adhar", "--", "cl_phone", "--", "cl_salary","cl_bank", "--", "cl_DOJ")
        for i in d:
            print(i[0], " - ", i[1], " - ", i[2], " - ", i[3], " - ", i[4], " - ", i[5]," - ",i[6])

    print("\n")


# pay cook's salary
def paysalaryfunc():
    print("Select The role whose salary you want to pay ")
    choice=input("\n1. Cook \n2. Manager \n3. Cleaner\n5. main menu")
    # choice = input("\n1. Cook \n2. Manager \n3. Cleaner\n4. Display salary paid employee \n5. main menu")
    paysalary = Paysalary()
    if choice == "1":
        paysalary.paycook_salary()
    elif choice == "2":
        paysalary.paymanager_salary()
    elif choice == "3":
        paysalary.paycleaner_salary()
    # elif choice=='4':
    #     role=input("\nEnter the role of employee :")
    #     paysalary.salary_paid_employee(role)
    elif choice=="5":
        options()
    else:
        options()

class Paysalary(Cook,Cleaner,Manager):
    def paymanager_salary(self):
        role="manager"
        Manager.Display_manager(self)
        Paysalary.pay_salary(self,role)
    def paycook_salary(self):
        role = "cook"
        Cook.Display_cook(self)
        Paysalary.pay_salary(self, role)
    def paycleaner_salary(self):
        role = "cleaner"
        Cleaner.Display_cleaner(self)
        Paysalary.pay_salary(self, role)
    def pay_salary(self,role):
        sql = f"select * from {role}"
        c = con.cursor()
        c.execute(sql)
        d = c.fetchall()
        if(len(d)==0):
            print(f'there is no {role}')
            return
        cid = input(f"Enter {role} Id : ")
        employee_list=np.array(d).flatten()
        for i in d:
            if(cid==i[0]):
                print(f"\n{role}_id", "-", f"{role}_name", "-", f"{role}_adhar", "-", f"{role}_phone", "-", f"{role}_salary", "-",f"{role}_bank", "-",
                      f"{role}_DOJ")
                print(i[0], " - ", i[1], " - ", i[2], " - ", i[3], " - ", i[4]," - ",i[5]," - ",i[6])
                break
        else:
                print("no employee with this id , please enter valid id")
                Paysalary.pay_salary(self,role)
        print("confirm employee before playing")
        ans=input("Is this employee ,you want to pay salary (yes/no)")
        if((ans=='Yes')or(ans=='yes')):

            cn = str(employee_list[1])
            ba = str(employee_list[5])
            date = datetime.datetime.today()
            s = employee_list[4]
            working_day = int(input("Working days : "))
            sa=int(s)

            ns = (sa / 30) * working_day
            data = (str(cid), cn, date,working_day,ba,int( s), int( ns))
            sql = "insert into salary values(%s,%s,%s,%s,%s,%s,%s)"
            c = con.cursor()
            c.execute(sql, data)
            con.commit()
            print("data inserted successfully")
        elif((ans=="no") or(ans=='No')):
            Paysalary.pay_salary(self,role)
            return
    def salary_paid_employee(self,role):
        sql=f"select * from {role}"
        c=con.cursor()
        c.execute(sql)
        d=c.fetchall()
        print("\n\n")
        if(len(d)==0):
            print(f"There is no {role}")
            return
        for i in d:
            print(i[0], " - ", i[1], " - ", i[2], " - ", i[3], " - ", i[4], " - ", i[5], " - ", i[6])



# make new order
def neworderfunc():
    print("1. New order \n2. Pending orders\n3. Update completed order\n4. Main menu")
    ch=int(input())
    neworder = Neworder()
    if(ch==1):
        neworder.take_order()
    elif(ch==2):
        neworder.display_pending_orders()
    elif(ch==3):
        neworder.update_status()
    elif(ch==4):
        options()
    else:
        print('Enter valid choice')
        neworderfunc()

class Neworder:

    def take_order(self):
        dil = []
        sql = "SELECT * FROM dish"
        c = con.cursor()
        c.execute(sql)
        d = c.fetchall()
        menulist = np.array(d).flatten()
        print("dishid --- name --- Cost --- cook")
        for i in d:
            print(i[3], " - ", i[0], " - ", i[1])
        print("\n")
        print("Select dishId which you want to order (enter 0 when done selection)")
        flag = 1


        while flag != 0:
            did = int(input())

            if did == 0:
                flag = 0
            #
            # print(menulist)
            elif not np.isin(str(did), menulist):
                print("Please enter a valid dish id: ")

            elif did != 0:
                dil.append(did)
        dishlist = np.array(d).flatten()
        cost = 0
        for i in dil:
            str1 = str(i)
            id_index = np.where(dishlist == str1)[0][0]
            index_of_cost = id_index - 2
            cost += int(dishlist[index_of_cost])
        print(cost)
        cn = input("Customer name : ")

        cp=input("Customer phone no. :")
        tn=input("table no. :")
        status="pending"
        bill='pending'
        dt = datetime.datetime.today()
        dt1 = str(dt)
        date = dt1[:10]
        time = dt1[11:19]

        data = (str(dil),cost,date,time, cp, cn, tn,status,bill)
        sql = "insert into orders values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("Data entered successfully")
        return
    def display_pending_orders(self):
        sql="select * from orders where Status='pending'"
        c=con.cursor()
        c.execute(sql)
        d=c.fetchall()
        if(len(d)==0):
            print("None of order is pending")
            return 0
        print(f"Dish_id--  Cost--  Date--  Time--  Customer_phone_no--  Customer_name--  Table_no--  Status--  Bill")
        for i in d:
            print(i[0], "- ", i[1], "- ", i[2], "- ", i[3], "- ", i[4], '- ', i[5], "- ", i[6], "- ", i[7],'- ',i[8])
        return 1

    def update_status(self):
        if(Neworder.display_pending_orders(self)==0):
            return
        print("\nWhich order is completed")
        cp=input("Enter customer phone number to update :")
        sql=f"update orders set Status='Completed' where Customer_phone_no='{cp}'"
        c=con.cursor()
        c.execute(sql)
        con.commit()
        print("Status updated successfully")

def billfunc():
    print('1. Bill update to paid \n2. display paid orders \n3. display pending Bills\n4. Main menu')
    ch=int(input())
    bill = Bill()
    if(ch==1):
        bill.update_bill_status()
    elif(ch==2):
        bill.display_bill_paid_orders()
    elif(ch==3):
        bill.display_bill_pending_orders()
    elif(ch==4):
        options()
    else:
        print('Enter valid choice')
        billfunc()

class Bill:
    def update_bill_status(self):
        sql="select * from orders where Status='Completed' and Bill='pending'"
        c=con.cursor()
        c.execute(sql)
        d=c.fetchall()
        painding_bill_list=np.array(d).flatten()
        if(len(d)==0):
            print("\n\nNone of order is pending \n")
            return
        print(f"Dish_id--  Cost--  Date--  Time--  Customer_phone_no--  Customer_name--  Table_no--  Status--  Bill")
        for i in d:
            print(i[0], "- ", i[1], "- ", i[2], "- ", i[3], "- ", i[4], '- ', i[5], "- ", i[6],"- ",i[7])
        print("\nWhich order is completed")
        cp = input("Enter customer phone number to update :")
        if not np.isin(cp,painding_bill_list):
            print("\n\nEnter correct customer phone number")
            Bill.update_bill_status(self)
        sql=f"update orders set Bill='Paid' where Customer_phone_no='{cp}'"
        c=con.cursor()
        c.execute(sql)
        con.commit()
        print("Status updated successfully")

        # Add that order record in completed_orders table and remove from orders tabled
        sql=f"select * from orders where Customer_phone_no='{cp}'"
        c=con.cursor()
        c.execute(sql)
        d=c.fetchall()
        datalist=[]
        for i in d:
            datalist.append(i[0])
            datalist.append(i[1])
            datalist.append(i[2])
            datalist.append(i[3])
            datalist.append(i[4])
            datalist.append(i[5])
            datalist.append(i[6])
            datalist.append(i[7])
            datalist.append(i[8])
        if len(datalist) > 7:
            table_no = str(datalist[7])
        else:
            table_no = ''
        print(datalist)
        if len(datalist) > 8:
            data = (
                datalist[0],
                int(datalist[1]) if datalist[1] is not None else 0,
                datalist[2] if datalist[2] is not None else '',
                datalist[3] if datalist[3] is not None else '',
                datalist[4] if datalist[4] is not None else '',
                datalist[5] if datalist[5] is not None else '',
                datalist[6] if datalist[6] is not None else '',
                table_no,
                datalist[8] if datalist[8] is not None else '',
            )
        else:
            return
        sql="insert into completed_orders values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        c=con.cursor()
        c.execute(sql,data)
        con.commit()
        print("data insert into completed_order")

        sql=f"delete from orders where Customer_phone_no='{cp}'"
        c=con.cursor()
        c.execute(sql)
        con.commit()
        print("record deleted form orders")
    def display_bill_paid_orders(self):
        sql="select * from completed_orders where Bill='paid' "
        c=con.cursor()
        c.execute(sql)
        d=c.fetchall()
        if(len(d)==0):
            print("\nNo record\n")
            return
        print(f"Dish_id--  Cost--  Date--  Time--  Customer_phone_no--  Customer_name--  Table_no--  Status--  Bill")
        for i in d:
            print(i[0], "- ", i[1], "- ", i[2], "- ", i[3], "- ", i[4], '- ', i[5], "- ", i[6], "- ", i[7], '- ', i[8])
    def display_bill_pending_orders(self):
        sql = "select * from orders where Bill='pending' and Status='Completed' "
        c = con.cursor()
        c.execute(sql)
        d = c.fetchall()
        if(len(d)==0):
            print("None of order remaining to paid bill")
            return

        print(f"Dish_id--  Cost--  Date--  Time--  Customer_phone_no--  Customer_name--  Table_no--  Status--  Bill")
        for i in d:
            print(i[0], "- ", i[1], "- ", i[2], "- ", i[3], "- ", i[4], '- ', i[5], "- ", i[6], "- ", i[7], '- ', i[8])


def Netincome():
    t = input("\n1. All   2. Year   3. Month   4. Date   5. main menu")
    if t == "1":
        sql = "select Cost from completed_orders"
        c=con.cursor()
        c.execute(sql)
        d = c.fetchall()
        total_income=0
        for i in d:

            total_income = total_income + i[0]
        print("Total income from orders : ", total_income, " Rs")
    elif(t=='2'):
        sql='select Cost,Date from completed_orders'
        c=con.cursor()
        c.execute(sql)
        d=c.fetchall()
        total_income=0
        y=input('Enter year : ')
        for i in d:
            if(y in str(i[1])):

                total_income+=i[0]
        print(total_income)

    elif t == "3":
        y = input("Enter year: ")
        m = input("Enter month :")
        sql = "select cost,date from completed_orders"
        c=con.cursor()
        c.execute(sql)
        d = c.fetchall()
        total_income=0
        for i in d:
            if ((y in str(i[1])) and (m in str(i[1]))):
                total_income+=i[0]
        print(total_income)

    elif t == "4":
        y = input("Enter year: ")
        m = input("Enter month: ")
        d = input("Enter date: ")
        sql = "select cost,date from completed_orders"
        c=con.cursor()
        c.execute(sql)
        result = c.fetchall()
        total_income=0

        for row in result:
            if (d in str(row[1])) and (m in str(row[1])) and (y in str(row[1])):
                total_income+=row[0]
        print(total_income)

    else:
        options()

def expenditurefunc():
    choice = int(input("\n1. Bill entry   2. show bills   3. main menu  :"))
    expenditure = Expenditure()
    if choice == 1:
        expenditure.store_paid_bill()
    elif choice == 2:
        expenditure.show_bill()
    elif choice==3:
        options()

# make new expenditure
class Expenditure:
    def store_paid_bill(self):
        t = input("type of bill : ")
        c = int(input("cost : "))
        d = datetime.date.today()
        data = (t, c, d)
        sql = "insert into Expenditure values(%s,%s,%s)"
        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("Data Entered successfully")

    def show_bill(self):
        c = con.cursor()
        t = input("1. All   2. Year   3. Month   4. Date : ")
        if t == "1":
            sql = "select * from Expenditure"
            c.execute(sql)
            d = c.fetchall()
            for i in d:

                print(i[0],"- ",i[1],'- ',i[2])
                # print(type(i[0],type(i[1]),type(i[2])))
        elif t == "2":
            y = input("Enter year : ")
            sql = "Select * from Expenditure"
            c.execute(sql)
            d = c.fetchall()
            year_list=[]
            for i in d:
                if(y in str(i[3])):
                    year_list.append(i)
            if (len(year_list) == 0):
                print("No bill paid in this month")
                return
            for i in year_list:
                print(i)
        elif t == "3":
            y = input("Enter year: ")
            m=input("Enter month :")
            sql = "select * from Expenditure"
            c.execute(sql)
            d = c.fetchall()
            Month_wise_list=[]
            for i in d:
                if((y in str(i[3])) and(m in str(i[3]))):
                    Month_wise_list.append(i)
            if(len(Month_wise_list)==0):
                print("No bill paid in this month")
                return
            for i in Month_wise_list:
                print(i)
        elif t == "4":
            y = input("Enter year: ")
            m = input("Enter month: ")
            d = input("Enter date: ")
            sql = "select * from expenditure"
            c.execute(sql)
            result = c.fetchall()
            Date_wise_list = []

            for row in result:
                if (d in str(row[3])) and (m in str(row[3])) and (y in str(row[3])):
                    Date_wise_list.append(row)

            if len(Date_wise_list) == 0:
                print("No bill paid on this day")
                return

            for row in Date_wise_list:
                print(row)
singin()

