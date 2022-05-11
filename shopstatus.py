import mysql.connector as connector

class Shopstatus:
    def __init__(self):
        self.connect = connector.connect(host='localhost', user='root', password='', database='super_shop')
        query = 'create table if not exists shopstatus(product_Id int, product_Name varchar(255),Current_price float,future_price float,Profit float,Percentage float,Status varchar(255))'
        cur = self.connect.cursor()
        cur.execute(query)
        print("table creatd succsesfuly")
    def insert__shopstatus(self,p_id,p_name,current_price,future_price,profit,percentage,status):
        query = "insert into shopstatus(product_Id,product_Name,Current_price,future_price,Profit,Percentage,Status) values({},'{}',{},{},{},{},'{}')".format(p_id,p_name,current_price,future_price,profit,percentage,status)
        cur = self.connect.cursor()
        cur.execute(query)
        self.connect.commit()
        print("insert sucsess")
    def display__all(self):
        query = ('select * from shopstatus')
        cur = self.connect.cursor()
        cur.execute(query)
        for row in cur:
            print("product ID:", row[0])
            print("product Name:", row[1])
            print("current price:", row[2])
            print("future price: ", row[3])
            print("profit: ", row[4])
            print("percentage: ", row[5])
            print("status: ", row[6])

            print()
            print()