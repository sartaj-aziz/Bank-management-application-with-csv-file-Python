import csv
class bank:
    acc_details = []

    def __init__(self,name,number,pin,amount):
        self.name = name
        self.number = number
        self.pin = pin
        self.amount=amount

        bank.acc_details.append(self)
    def __repr__(self):
        return f"Name: {self.name}\t Number:{self.number}\t Pin:{self.pin} \t Amount:{self.amount}"
    @classmethod
    def instantiate_from_csv(cls):
        with open('customer.csv','r') as f:
            read=csv.reader(f)
            global items
            items=list(read)


            for item in items:

                if item:
                    bank(
                        name=item[0],
                        number=item[1],
                        pin=item[2],
                        amount=item[3]
                    )





    def create_acc(a,b,c,d):
        row_data=[a,b,c,d]
        items.append(row_data)
        with open('customer.csv', 'w', newline='') as writer:
            writer = csv.writer(writer)
            writer.writerows(items)

    def login(a,b,c,d):

        for i in items:
            ctr=0
            if i==[a,b,c,d]:
                print("logging password corrct")
                ans=int(input("Select options\nPress 1 for deposit\nPress 2 for withdrawl\nPress 3 for money trasfer\nPress 4 for log out"))
                if ans==1:
                    bank.deposit(c)
                    ctr=ctr+1
                    break
                elif ans==2:
                    bank.withdrawl(c)
                    ctr=ctr+1
                    break
                elif ans==3:
                    bank.payment(c)
                    ctr=ctr+1
                    break
            else:
                pass
        if ctr==0:
            print("Wrong Passcode")

    def deposit(pin):
        dep_mon=int(input("Amount of money for deposit: "))
        for i in items:
            if i:
                if i[2] == pin:
                    i[3] = str(int(i[3]) + dep_mon)
                    print(f"Transiction Successful\nAccount Balance: {i[3]}")
        with open('customer.csv','w',newline='') as writer:
            writer=csv.writer(writer)
            writer.writerows(items)




    def withdrawl(pin):
        withdrawl_mon=int(input("Withdrawl Amount: "))
        for i in items:
            if i:
                if i[2]==pin:
                    i[3]=str(int(i[3])-withdrawl_mon)
                    print(f"Transiction Successful\nAccount Balance: {i[3]}")
        with open('customer.csv','w',newline='') as writer:
            writer=csv.writer(writer)
            writer.writerows(items)
    def payment(pin):
        other_pin=input("Enter the other account pin: ")
        other_amount=int(input("Enter the payment amount: "))
        for i in items:
            if i:
                if i[2]==pin:
                    i[3]=str(int(i[3])-other_amount)
                    print(f"Transiction Successful\nAccount Balance: {i[3]}")
        for j in items:
            if j:
                if j[2]==other_pin:
                    j[3]=str(int(j[3])+other_amount)
        with open('customer.csv','w',newline='') as writer:
            writer=csv.writer(writer)
            writer.writerows(items)




