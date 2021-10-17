######################################################33
## create class employee 
import psycopg2
con = psycopg2.connect(database='postgres', user='postgres', password='postgres',
                       host='127.0.0.1', port='5433')
print('Database opened successfully')
cur = con.cursor()
cur.execute('''create table employee(
          #  ID serial primary key,
           # First_name text not null,
           #   Last_name text not null,
            #  Age int not null,
            #  Department char(50),
              #Salary int
            # );''')
con.commit()
cur.execute('''create table Managers(
          #  managed_department varchar(50)
              
           # ) INHERITS (employee);''') 
con.commit()

class employee:
    emp_list=[]
    def __init__(self,First_name,Last_name,Age,Department,Salary):

        self.First_name=First_name
        self.Last_name=Last_name
        self.Age=Age
        self.Department=Department
        self.Salary=Salary
        employee.emp_list.append(self)
      
    def insertion(self):  
        cur.execute(f'''Insert into employee(First_name, Last_name, Age, Department, Salary) values ('{self.First_name}','{self.Last_name}',{self.Age},'{self.Department}',{self.Salary}) ''')
        print('Record inserted successfully') 

    def transfer(self,dep):
        cur.execute(f''' Update employee set department = '{dep}' where Age = {self.Age} ''')
        print('Record updated successfully') 

    def fire(self):
        employee.emp_list.remove(self)
        cur.execute(f'''Delete from employee where Age = {self.Age} ''')

    def show(self):
        cur.execute(f'''select * from employee where Age = {self.Age}''')
        rec=cur.fetchone()
        print(rec)

    def list_employees(self):
        cur.execute('select * from employee')
        rows = cur.fetchall()
        for row in rows:
            print(row)    

class manager(employee):
    def __init__(self,First_name,Last_name,Age,Department,Salary,managed_department):

        self.managed_department=managed_department
        self.Salary="confidentional"

        super().__init__(First_name,Last_name,Age,Department,Salary)

    def insertion(self):  
        cur.execute(f'''Insert into Managers(First_name, Last_name, Age, Department, Salary,managed_department) values ('{self.First_name}','{self.Last_name}',{self.Age},'{self.Department}',{self.Salary},'{self.managed_department}') ''')
        print('Record inserted successfully')     

    def show(self):
        cur.execute(f'''select First_name , Last_name , Age ,Department , managed_department from Managers where Age = {self.Age}''')
        rec=cur.fetchone()
        print(rec)

##creating a menu for the user to choose the operation 
print("For adding new employee enter add : ")
op_select=input("if the manager press 'M' /if the employee press 'E' : ")

#inserting data of objects into table employee
if op_select == "E":
    First_name=input("enter your first name ")
    Last_name=input("enter your last name ")
    Age=int(input("enter your age "))
    Department=input("enter your department ")
    Salary=int(input("enter your salary "))
    employee1= employee(First_name,Last_name,Age,Department,Salary)
    employee1.insertion()
    con.commit()
    choose_ap=input("enter the operation 'update', 'remove' ,'show' ,'display','exit' ")

    if choose_ap == "update":
        up_dep=input("enter the new department ")
        employee1.transfer(up_dep)
        con.commit()    

    elif choose_ap == "remove":
        employee1.fire()
        con.commit()

    elif choose_ap == "show":
        employee1.show()
        con.commit()

    elif choose_ap == "display":
        employee1.list_employees()
        con.commit()

    else : 
        print("Exit the Program ")
        con.close()

elif op_select == "M":
    First_name=input("enter your first name ")
    Last_name=input("enter your last name ")
    Age=int(input("enter your age "))
    Department=input("enter your department ")
    Salary=int(input("enter your salary "))
    managed_department=input("enter your managed department ") 
    Mang=manager(First_name,Last_name,Age,Department,Salary,managed_department)
    Mang.insertion()
    Mang.show()
    con.commit()
####################################################################

