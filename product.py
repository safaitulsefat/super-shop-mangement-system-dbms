import mysql.connector as connector

class Product:
    def __init__(self):
        self.connect = connector.connect(host='localhost', user='root', password='', database='super_shop')
        query = 'create table if not exists product(product_Id int primary key, product_Name varchar(255), product_type varchar(255), company_name varchar(255),exp_date date,mfg_date date,bar_code varchar(255),price float)'
        cur = self.connect.cursor()
        cur.execute(query)
        print("table creatd succsesfuly")
    def insert__product(self,p_id,p_name,p_type,c_name,exp_date,mfg_date,bar_code,price):
        query = "insert into product(product_Id,product_Name,product_type,company_name,exp_date,mfg_date,bar_code,price) values({},'{}','{}','{}','{}','{}','{}',{})".format(p_id,p_name,p_type,c_name,exp_date,mfg_date,bar_code,price)
        cur = self.connect.cursor()
        cur.execute(query)
        self.connect.commit()
        print("insert sucsess")

    def display__all(self):
        query = ('select * from product')
        cur = self.connect.cursor()
        cur.execute(query)
        for row in cur:
            print("product ID:", row[0])
            print("product Name:", row[1])
            print("product type:", row[2])
            print("company name ", row[3])
            print("product exp date ", row[4])
            print("product mfg date: ", row[5])
            print("product bar code: ", row[6])
            print("product price: ", row[7])

            print()
            print()

    def delete__product(self, id):
        query = 'delete from product where product_Id={}'.format(id)
        print(query)
        cur = self.connect.cursor()
        cur.execute(query)
        self.connect.commit()
        print("deleted")
    def update__product(self, p_id,p_name,p_type,c_name,exp_date,mfg_date,bar_code,price):
        query = 'update product set product_Name ="{}", product_type = "{}",comany_name = "{}",exp_date="{}",  mfg_date = "{}",bar_code ="{}",price = {} where product_Id={}'.format(p_name,p_type,c_name,exp_date,mfg_date,bar_code,price,p_id)
        cur = self.connect.cursor()
        cur.execute(query)
        self.connect.commit()
        print("update customer succsessfully")


