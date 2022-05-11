import mysql.connector as connector

class Receipt:
    def __init__(self):
        self.connect = connector.connect(host='localhost', user='root', password='', database='super_shop')
        query = 'create table if not exists receipt(transaction_no int primary key,product_name varchar(255),quantity int,cashier_name varchar(255),price float,total_amount float, date_time datetime,productId int,customerId int,FOREIGN KEY (productId) REFERENCES product(product_Id) ON DELETE CASCADE,FOREIGN KEY (customerId) REFERENCES customer(Id) ON DELETE CASCADE)'
        cur = self.connect.cursor()
        cur.execute(query)
        print("table creatd succsesfuly")
    def insert__receipt(self,transaction_no,product_name,quantity,cashier_name,price,total_amount, date_time,productId,customerId):
        query = "insert into receipt(transaction_no,product_name,quantity,cashier_name,price,total_amount, date_time,productId,customerId) values({},'{}',{},'{}',{},{},'{}',{},{})".format(transaction_no,product_name,quantity,cashier_name,price,total_amount, date_time,productId,customerId)
        cur = self.connect.cursor()
        cur.execute(query)
        self.connect.commit()
        print("insert sucsess")

    def display__all(self):
        query = ('select * from receipt')
        cur = self.connect.cursor()
        cur.execute(query)
        for row in cur:
            print("transaction no:", row[0])
            print("product name:", row[1])
            print("quantity:", row[2])
            print("cahier name ", row[3])
            print("recipt price ", row[4])
            print("recipt total amount: ", row[5])
            print("receipt data time: ", row[6])
            print("product id: ", row[7])
            print("customer id",row[8])

            print()
            print()

    def delete__receipt(self, no):
        query = 'delete from receipt where transaction_no={}'.format(no)
        print(query)
        cur = self.connect.cursor()
        cur.execute(query)
        self.connect.commit()
        print("deleted")
    def update__receipt(self,transaction_no,product_name,quantity,cashier_name,price,total_amount, date_time,productId,customerId):
        query = 'update receipt set product_name ="{}", quantity = {},cashier_name = "{}",price="{}",  total_amount = "{}",date_time ="{}",productId = {},customeId = {} where transaction_no={}'.format(product_name,quantity,cashier_name,price,total_amount, date_time,productId,customerId,transaction_no)
        cur = self.connect.cursor()
        cur.execute(query)
        self.connect.commit()
        print("update customer succsessfully")
    def join_recipt(self):
        query='select customer.Name,receipt.cashier_name from receipt inner join customer on receipt.customerId = customer.id'
        cur = self.connect.cursor()
        cur.execute(query)
        for row in cur:
            print("customer name: ", row[0])
            print("chashier name: ", row[1])
    def sum_of_totalamount(self):
        query='select sum(total_amount) FROM receipt'
        cur = self.connect.cursor()
        cur.execute(query)
        for row in cur:
            print("sum of total amount all product: ", row[0])

