from abc import ABC, abstractmethod
class car(ABC):
    def paySlip(self, amount):
        print("Your purchse amount: ",amount)
#this function is telling us to pass in as argument, but we wont tell you how
#or what kind  of data it will be.
    @abstractmethod
    def payment(self, amount):
        pass

class DebitCardPayment(car):
#here we've defined how to impliment the payment function from it's parent paySlip class.
    def payment(self, amount):
        print('Your purchase amount of {} exceeded your $100 limit '.format(amount))

obj = DebitCardPayment()
obj.paySlip("$400")
obj.payment("$400")
