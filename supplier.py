import mysql.connector as connector

class Supplier:
    def __init__(self):
        self.connect = connector.connect(host='localhost', user='root', password='', database='super_shop')
        query = 'create table if not exists supplier(suplier_Id int primary key, suplier_Name varchar(255), Address varchar(255),Contract_no varchar(255))'
        cur = self.connect.cursor()
        cur.execute(query)
        print("table creatd succsesfuly")
    def insert__supplier(self,id,name,address,cotractno):
        query = "insert into supplier(suplier_Id,suplier_Name,Address,Contract_no) values({},'{}','{}','{}')".format(id, name, address, cotractno )
        cur = self.connect.cursor()
        cur.execute(query)
        self.connect.commit()
        print("insert sucsess")

    def display__all(self):
        query = ('select * from supplier')
        cur = self.connect.cursor()
        cur.execute(query)
        for row in cur:
            print("suplier ID:", row[0])
            print("suplier Name:", row[1])
            print("suplier Adress ",row[2])
            print("suplier contarct no ",row[3])
            print()
            print()

    def delete__supplier(self, id):
        query = 'delete from supplier where suplier_Id={}'.format(id)
        print(query)
        cur = self.connect.cursor()
        cur.execute(query)
        self.connect.commit()
        print("deleted")
    def update__supplier(self, id, name, address, contract):
        query = 'update supplier set suplier_Name="{}", Address ="{}", Contract_no = "{}" where suplier_Id={}'.format(name, address, contract, id)
        cur = self.connect.cursor()
        cur.execute(query)
        self.connect.commit()
        print("update customer succsessfully")


