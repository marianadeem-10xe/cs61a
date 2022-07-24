# Lecture 16
class Clown:
    nose = 'big and red'
    def dance():
        return 'No thanks'

def wwpd_clown():
    Clown.nose
    Clown.dance
    Clown.dance()
    nose
    dance()


class Account:
	def __init__(self, account_holder):
		self.balance = 0
		self.holder = account_holder

def wwpd_simple_account():
    a = Account("Catherine")
    a
    Account
    a.holder
    __init__
    Account.__init__
    self
    balance
    holder
    a.holder
    Account.holder 
    Account.balance

class Account:
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        """Add amount to balance."""
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        """Subtract amount from balance if funds are available."""
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance

def wwpd_account_methods():
    a = Account("Catherine")
    a.deposit(100)
    Account.deposit
    a.deposit # these are different - bound method
    Account.deposit(a, 1000)
    Account.deposit(1000)
    a.deposit(1000)
    a.deposit(a, 1000)
    f = Account.deposit
    f(a, 1000)
    a.balance

def attributes_demo():
    catherine = Account('Catherine')
    catherine.balance
    getattr
    getattr(catherine, 'balance')
    catherine.deposit(100)
    getattr(catherine, 'balance')
    catherine.balance
    catherine.balance = 5000000
    catherine.balance
    hasattr(catherine, 'balance')
    hasattr(catherine, 'lance')

# Attribute lookup example

class Account:

    interest = 0.02  # A class attribute

    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        """Add amount to balance."""
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        """Subtract amount from balance if funds are available."""
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance

def attribute_lookups():
    tom = Account("Tom")
    amy = Account("Amy")
    tom.interest
    amy.interest = 0.05 # Tom has been in debt too much!
    tom.interest
    amy.interest 
    print(Account.interest)



class Cat:
	species = 'Cat'
	def __init__(self, name):
		self.name = name
	def speak(self):
		print("My name is", self.name, "and I am a ", self.species)



