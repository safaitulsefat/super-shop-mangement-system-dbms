from customer import Customer
from employee import Employee
from product import Product
from receipt import Receipt

def main():
    customer = Customer()
    employee = Employee()
    product = Product()
    receipt = Receipt()
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
        print("press 17 exit program")
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
                price = int(input("enter product price"))
                product.insert__product(id,name,p_type,company_name,exp_date,mfg_date,bar_code,price)
            elif choice==10:
                product.display__all()
            elif choice==11:
                id = int(input("enter employee id"))
                product.delete__product(id)
            elif choice==12:
                id = int(input("enter product id: "))
                name = input("enter product name: ")
                p_type = input("enter product type : ")
                company_name = input("enter company name: ")
                exp_date = input("enter product exp date: ")
                mfg_date = input("enter product mfg date")
                bar_code = input("enter  product bar code: ")
                price = int(input("enter product price"))
                product.insert__product(id, name, p_type, company_name, exp_date, mfg_date, bar_code, price)
            elif choice==13:
                t_no = int(input("enter transaction no: "))
                p_name = input("enter product name: ")
                quantity = int(input("enter quantity : "))
                cashier_name = input("enter cashier name: ")
                price = int(input("enter price: "))
                total_amount = int(input("enter product mfg date"))
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
                price = int(input("enter price: "))
                total_amount = int(input("enter product mfg date"))
                date_time = input("enter  date_time: ")
                p_id = int(input("enter product id"))
                c_id = int(input("enter customer id"))
                receipt.update__receipt(t_no, p_name, quantity, cashier_name, price, total_amount, date_time, p_id,
                                        c_id)
            elif choice==17:
                break
            else:
                print("invalid input")
        except Exception as e:
            print(e)
            print("invalid details")

if __name__ == "__main__":
    main()