class Plan:
    
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost


class Phonecall(Plan):

    def __init__(self, customer, duration):
        self.customer = customer
        self.duration = duration

        customer.history.append(self)
        self.customer.balance -= self.cost()

    def cost(self):
        return self.duration * self.customer.plan.cost

        
    
class Customer(Plan):

    def __init__(self, name, balance, plan, history):
        self.name = name
        self.balance = balance
        self.plan = plan
        self.history = []

    def __str__(self):
        return  '\n'+ '\n'.join(('{} = {}'.format(item, self.__dict__[item]) for item in self.__dict__))
        # return "name : " + str(self.name) + " ; balance = " + str(self.balance) +  " ; plan = " + str(self.plan) + " ; history = " + str(self.history) 
    


default = Plan('default', 2) 
alice = Customer('Alice', 200, default, []) 
call1 = Phonecall(alice, 20) 
call2 = Phonecall(alice, 40) 


assert call1.cost() == 40 
assert call2.cost() == 80 
assert alice.history == [call1, call2] 
assert alice.balance == 80
print(alice)

expensive = Plan('expensive', 20)

bob = Customer('Bob', 600, expensive, [])

call3 = Phonecall(bob, 20)

assert call3.cost() == 400
assert bob.balance == 200

call4 = Phonecall(bob, 5)
call5 = Phonecall(bob, 5)

assert call4.cost() == 100
assert call5.cost() == 100

assert bob.history == [call3, call4, call5]
assert bob.balance == 0
print(bob)