import mysql.connector as connector

class Orderlist:
    def __init__(self):
        self.connect = connector.connect(host='localhost', user='root', password='', database='super_shop')
        query = 'create table if not exists orderlist(orderId int primary key,orderDate date,deliveryDate date,suplierId int,productId int,foreign key(suplierId) references supplier(suplier_Id),foreign key(productId) references product(product_Id) ON DELETE CASCADE) '
        cur = self.connect.cursor()
        cur.execute(query)
        print("table creatd succsesfuly")
    def insert__order(self,id,orderDate,deliveryDate,suplierId,productId):
        query = "insert into orderlist(orderId,orderDate,deliveryDate,suplierId,productId) values({},'{}','{}',{},{})".format(id,orderDate,deliveryDate,suplierId,productId)
        cur = self.connect.cursor()
        cur.execute(query)
        self.connect.commit()
        print("insert sucsess")

    def display__all(self):
        query = ('select * from orderlist')
        cur = self.connect.cursor()
        cur.execute(query)
        for row in cur:
            print("order ID: ", row[0])
            print("Order date: ", row[1])
            print("Delivery date ",row[2])
            print("suplier id ",row[3])
            print("product id: ",row[4])
            print()
            print()

    def delete_order(self, id):
        query = 'delete from orderlist where orderId={}'.format(id)
        print(query)
        cur = self.connect.cursor()
        cur.execute(query)
        self.connect.commit()
        print("deleted")
    def update__order(self, id,orderDate,deliveryDate,suplierId,productId):
        query = 'update orderlist set orderDate="{}", deliveryDate ="{}", suplierId = {},productId = {} where orderId={}'.format(orderDate,deliveryDate,suplierId,productId, id)
        cur = self.connect.cursor()
        cur.execute(query)
        self.connect.commit()
        print("update customer succsessfully")

    def join(self):
        query = 'select orderId,suplier_Name from orderlist right outer join supplier on orderlist.suplierId=supplier.suplier_Id'
        cur = self.connect.cursor()
        cur.execute(query)
        for row in cur:
            print("order ID: ", row[0])
            print("sulllier name: ", row[1])
