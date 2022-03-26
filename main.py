from customer import Customer

def main():
    customer = Customer()
    while True:
        print("************welcome*********")
        print()
        print("Press 1 to insert new customer: ")
        print("press 2 to display all customer: ")
        print("press 3 to delete customer")
        print("press 4 to update customer information: ")
        print("press 5 to exit program")
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
                break
            else:
                print("invalid input")
        except Exception as e:
            print(e)
            print("invalid details")

if __name__ == "__main__":
    main()