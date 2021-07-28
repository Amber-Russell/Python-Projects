#Parent class user
class Teacher:
    name = "Carl Thomas"
    email = "clarthomas@gmail.com"
    password = "Ilikecats"

    def getLoginInfo(self):
        entry_name = input("Enter your full name:")
        entry_email = input("Enter your email address:")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}".format(entry_name))
        else:
            print("The password or email is incorrect.")

    #child class employee
class Staff(Teacher):
    base_pay = 15.00
    department = "Teaching Assistant"
    pin_number = "1234"

    #this is the same method in the parent class "Teacher"
        #the difference is that, instead of using entry_password, we are using entry_pin.

    def getLoginInfo(self):
        entry_name = input("")
        entry_email = input("")
        entry_pin = input("")
        if(entry_email==self.email and entry_pin==self.pin_number):
            print("Welcome back, {}".format(entry_name))
        else:
            print("The password or email is incorrect.")

#the follwing code invokes the methods inside each class for User and Employee.
customer = Teacher()
customer.getLoginInfo()

manager = Staff()
manager.getLoginInfo()
