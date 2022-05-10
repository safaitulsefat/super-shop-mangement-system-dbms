import mysql.connector as connector

class Employee:
    def __init__(self):
        self.connect = connector.connect(host='localhost', user='root', password='', database='super_shop')
        query = 'create table if not exists employee(emp_Id int primary key, emp_Name varchar(255), Nid varchar(255), joining_date date,salary int,Contract_no varchar(255),address varchar(255),designation varchar(255))'
        cur = self.connect.cursor()
        cur.execute(query)
        print("table creatd succsesfuly")
    def insert__employee(self,id,name,nid,joiningdate,salary,cotractno,address,designation):
        query = "insert into employee(emp_Id,emp_Name,Nid,joining_date,salary,Contract_no,address,designation) values({},'{}','{}','{}',{},'{}','{}','{}')".format(id, name, nid,joiningdate,salary,cotractno, address,designation)
        cur = self.connect.cursor()
        cur.execute(query)
        self.connect.commit()
        print("insert sucsess")

    def display__all(self):
        query = ('select * from employee')
        cur = self.connect.cursor()
        cur.execute(query)
        for row in cur:
            print("employee ID:", row[0])
            print("employee Name:", row[1])
            print("employee Nid:", row[2])
            print("employee joining data ", row[3])
            print("employee salary ", row[4])
            print("employee contractno: ", row[5])
            print("employee address: ", row[6])
            print("employee designation: ", row[7])
            print()
            print()

    def delete__employee(self, id):
        query = 'delete from employee where emp_Id={}'.format(id)
        print(query)
        cur = self.connect.cursor()
        cur.execute(query)
        self.connect.commit()
        print("deleted")
    def update__employee(self, id,name,nid,joiningdate,salary,cotractno,address,designation):
        query = 'update employee set emp_Name ="{}", Nid = "{}",joining_date = "{}",salary={},  Contract_no = "{}",Address ="{}",designation="{}" where emp_Id={}'.format(name, nid,joiningdate,salary,cotractno, address, designation, id)
        cur = self.connect.cursor()
        cur.execute(query)
        self.connect.commit()
        print("update customer succsessfully")
    def max_salary(self):
        query = 'select emp_Name,salary from employee where salary=(select max(salary) from employee)'
        cur = self.connect.cursor()
        cur.execute(query)
        for row in cur:
            print("employee name:", row[0])
            print("maximum employee salary:", row[1])



