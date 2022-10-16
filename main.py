from bank import bank


bank.instantiate_from_csv()


print("....Welcome to bank mobile application....")
ans=int(input("Press 1 for creating new account\nPress 2 for login\n"))

if ans==1:
    x=input("Name: ")
    y=input("Number: ")
    z=input("Pin: ")
    k=input("Initial amount: ")
    bank.create_acc(x,y,z,k)
    print("New Account created")

elif ans==2:
    a = input("Login: \nName: ")
    b = input("NUmber: ")
    c = input("Pin: ")
    d = input("Amount: ")
    bank.login(a, b, c, d)

else:
    print("Thanks for your service. See you soon")






