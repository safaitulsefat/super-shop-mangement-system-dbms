from customer import Customer
from employee import Employee
from product import Product
from receipt import Receipt
from supplier import Supplier
from orderlist import  Orderlist
from shopstatus import Shopstatus
def main():
    customer = Customer()
    employee = Employee()
    product = Product()
    receipt = Receipt()
    supplier = Supplier()
    orderlist = Orderlist()
    shopstatus = Shopstatus()

    while True:
        print("************welcome*********")
        print()
        print("Press 1 to insert new customer: ")
        print("press 2 to display all customer: ")
        print("press 3 to delete customer")
        print("press 4 to update customer information: ")
        print("*****************************")
        print("press 5 to insert new employee")
        print("press 6 to display all employee")
        print("press 7 to delete employee")
        print("press 8 update employee information")
        print("*********************************")
        print("press 9 to insert new product")
        print("press 10 to display all product")
        print("press 11 to delete product")
        print("press 12 update product information")

        print("press 13 to insert new receipt")
        print("press 14 to display all receipt")
        print("press 15 to delete receipt")
        print("press 16 update receipt information")
        print("Press 17 to insert new supplier: ")
        print("press 18 to display all supplier: ")
        print("press 19 to delete supplier")
        print("press 20 to update supplier information: ")
        print("press 21 insert order")
        print("Press 22 to display all: ")
        print("press 23 to delete orderlist: ")
        print("press 24 to update order list")
        print("press 25 to search customer name")
        print("press 26 to orderlist and supplier right join: ")
        print("enter 27 to customer and recipt inner join")
        print("enter 28 maximum salary")
        print("enter 29 shop status")
        print("enter 30 display shop status")
        print("enter 31 find range of product price")
        print("enter 32 sum all amount of product")
        print("enter 33 groupby product type sum: ")
        print("enter 34 increase employee salary when selling product properly: ")
        print("enter 35 exit")
        print()
        try:
            choice = int(input())
            if (choice == 1):
                id = int(input("enter customer id: "))
                name = input("enter customer name: ")
                nid = input("enter customer nid : ")
                address = input("enter customer address: ")
                contractno = input("enter  customer contract no: ")
                customer.insert__customer(id,name,nid,address,contractno)
            elif choice == 2:
                customer.display__all()
            elif choice == 3:
                id = int(input("enter customer id who is deleted from customer table: "))
                customer.delete__customer(id)
            elif choice == 4:
                id = int(input("enter customer id: "))
                name = input("enter customer name: ")
                nid = input("enter customer nid : ")
                address = input("enter customer address: ")
                contractno = input("enter  customer contract no: ")
                customer.update__customer(id,name,nid,address,contractno)
            elif choice == 5:
                id = int(input("enter employee id: "))
                name = input("enter employee name: ")
                nid = input("enter employee nid : ")
                joiningdate = input("enter employee joiningdate: ")
                salary = int(input("enter employee salary"))
                contractno = input("enter  employee contract no: ")
                address = input("enter employee address: ")
                designstion = input("enter designstion")
                employee.insert__employee(id,name,nid,joiningdate,salary,contractno,address,designstion)
            elif choice==6:
                employee.display__all()
            elif choice == 7:
                id = int(input("enter employee id"))
                employee.delete__employee(id)
            elif choice==8:
                id = int(input("enter employee id: "))
                name = input("enter employee name: ")
                nid = input("enter employee nid : ")
                joiningdate = input("enter employee joiningdate: ")
                salary = int(input("enter employee salary"))
                contractno = input("enter  employee contract no: ")
                address = input("enter employee address: ")
                designstion = input("enter designstion")
                employee.update__employee(id, name, nid, joiningdate, salary, contractno, address, designstion)
            elif choice==9:
                id = int(input("enter product id: "))
                name = input("enter product name: ")
                p_type = input("enter product type : ")
                company_name = input("enter company name: ")
                exp_date = input("enter product exp date name: ")
                mfg_date = input("enter product mfg date")
                bar_code = input("enter  product bar code: ")
                price = float(input("enter product price"))
                product.insert__product(id,name,p_type,company_name,exp_date,mfg_date,bar_code,price)
            elif choice==10:
                product.display__all()
            elif choice==11:
                id = int(input("enter product id"))
                product.delete__product(id)
            elif choice==12:
                id = int(input("enter product id: "))
                name = input("enter product name: ")
                p_type = input("enter product type : ")
                company_name = input("enter company name: ")
                exp_date = input("enter product exp date: ")
                mfg_date = input("enter product mfg date")
                bar_code = input("enter  product bar code: ")
                price = float(input("enter product price"))
                product.insert__product(id, name, p_type, company_name, exp_date, mfg_date, bar_code, price)
            elif choice==13:
                t_no = int(input("enter transaction no: "))
                p_name = input("enter product name: ")
                quantity = int(input("enter quantity : "))
                cashier_name = input("enter cashier name: ")
                price = float(input("enter price: "))
                total_amount = float(input("enter product total amount"))
                date_time = input("enter  date_time: ")
                p_id = int(input("enter product id"))
                c_id = int(input("enter customer id"))
                receipt.insert__receipt(t_no,p_name,quantity,cashier_name,price,total_amount,date_time,p_id,c_id)
            elif choice==14:
                receipt.display__all()
            elif choice==15:
                t_no = int(input("enter transaction no: "))
                receipt.delete__receipt(t_no)
            elif choice==16:
                t_no = int(input("enter transaction no: "))
                p_name = input("enter product name: ")
                quantity = int(input("enter quantity : "))
                cashier_name = input("enter cashier name: ")
                price = float(input("enter price: "))
                total_amount = float(input("enter total amount"))
                date_time = input("enter  date_time: ")
                p_id = int(input("enter product id"))
                c_id = int(input("enter customer id"))
                receipt.update__receipt(t_no, p_name, quantity, cashier_name, price, total_amount, date_time, p_id,c_id)

            elif choice==17:
                s_id = int(input("enter customer id: "))
                s_name = input("enter customer name: ")
                address = input("enter customer address: ")
                contractno = input("enter  customer contract no: ")
                supplier.insert__supplier(s_id,s_name,address,contractno)
            elif choice==18:
                supplier.display__all()
            elif choice==19:
                s_id = int(input("enter supplier id"))
                supplier.delete__supplier(s_id)
            elif choice==20:
                s_id = int(input("enter customer id: "))
                s_name = input("enter customer name: ")
                address = input("enter customer address: ")
                contractno = input("enter  customer contract no: ")
                supplier.update__supplier(s_id, s_name, address, contractno)
            elif choice == 21:
                o_id = int(input("enter order  id: "))
                order_date = input("enter order date: ")
                delivery_date = input("enter delivery date: ")
                suplier_id = int(input("enter  supplier id: "))
                product_id = int(input("enter product id"))
                orderlist.insert__order(o_id, order_date, delivery_date, suplier_id, product_id)
            elif choice == 22:
                orderlist.display__all()
            elif choice == 23:
                o_id = int(input("enter supplier id"))
                orderlist.delete_order(o_id)
            elif choice == 24:
                o_id = int(input("enter order  id: "))
                order_date = input("enter order date: ")
                delivery_date = input("enter delivery date: ")
                suplier_id = int(input("enter  supplier id: "))
                product_id = int(input("enter product id"))
                orderlist.insert__order(o_id, order_date, delivery_date, suplier_id, product_id)
            elif choice==25:
                name = input("enter name")
                customer.search_customer(name)
            elif choice==26:
                orderlist.orderlist_join()
            elif choice==27:
                receipt.join_recipt();
            elif choice==28:
                employee.max_salary();
            elif choice==29:
                p_id = int(input("enter product id"))
                p_name = input("enter product name")
                current_price = float(input("enter current price"))
                future_price = float(input("enter future price"))
                profit = input("enter profit null")
                percentage = input("enter percentage null")
                status = input("enter status null")
                shopstatus.insert__shopstatus(p_id,p_name,current_price,future_price,profit,percentage,status)
            elif choice==30:
                shopstatus.display__all()
            elif choice==31:
                price1=float(input("enter price1: "))
                price2=float(input("enter price2: "))
                product.search_rangeOf_price(price1,price2)
            elif choice==32:
                receipt.sum_of_totalamount()
            elif choice==33:
                product.groupby_product_sum()
            elif choice==34:
                percent = float(input("enter percentage:"))
                total_amount = float(input("enter total amount: "))
                employee.increase_employ_salary(percent,total_amount)
            elif choice == 35:
                break
            else:
                print("invalid input")
        except Exception as e:
            print(e)
            print("invalid details")

if __name__ == "__main__":
    main()