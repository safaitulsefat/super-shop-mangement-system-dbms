import mysql.connector as connector

class Customer:
    def __init__(self):
        self.connect = connector.connect(host='localhost', user='root', password='', database='super_shop')
        query = 'create table if not exists customer(Id int primary key, Name varchar(255), Nid varchar(255), Address varchar(255),Contract_no varchar(255))'
        cur = self.connect.cursor()
        cur.execute(query)
        print("table creatd succsesfuly")
    def insert__customer(self,id,name,nid,address,cotractno):
        query = "insert into customer(Id,Name,Nid,Address,Contract_no) values({},'{}','{}','{}','{}')".format(id, name, nid, address, cotractno )
        cur = self.connect.cursor()
        cur.execute(query)
        self.connect.commit()
        print("insert sucsess")

    def display__all(self):
        query = ('select * from customer')
        cur = self.connect.cursor()
        cur.execute(query)
        for row in cur:
            print("customer ID:", row[0])
            print("customer Name:", row[1])
            print("customer Nid:", row[2])
            print("customer Adress ",row[3])
            print("customer contarct no ",row[4])
            print()
            print()

    def delete__customer(self, id):
        query = 'delete from customer where Id={}'.format(id)
        print(query)
        cur = self.connect.cursor()
        cur.execute(query)
        self.connect.commit()
        print("deleted")
    def update__customer(self, id, name, nid, address, contract):
        query = 'update customer set Name ="{}", Nid = "{}", Address ="{}", Contract_no = "{}" where Id={}'.format(name, nid, address, contract, id)
        cur = self.connect.cursor()
        cur.execute(query)
        self.connect.commit()
        print("update customer succsessfully")
    def search_customer(self,name):
        query = "select name,Address from customer where Name like '{}%'".format(name)
        cur = self.connect.cursor()
        cur.execute(query)
        for row in cur:
            print("customer name:", row[0])
            print("customer Address",row[1]);




