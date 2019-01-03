class vehicle:
    def general_use(self):
        print('General use is transportation')
class car(vehicle):
    def __init__(self):
        print('Hey, This is car')
        self.wheels=4
        self.roof=True
    def specific_use(self):
        self.general_use()
        print('Specific uses are:\nCommute to work\nVacation with family')
class motorcycle(vehicle):
    def __init__(self):
        print('Hey, This is bike')
        self.wheels=2
        self.roof=False
    def specific_use(self):
        self.general_use()
        print('Specific uses are:\nRoad trip\nRacing')
        
c=car()
c.specific_use()
c.general_use()
b=motorcycle()
b.specific_use()
b.general_use()

print(isinstance(c,car))
print(isinstance(c,motorcycle))
print(isinstance(c,vehicle))
print(isinstance(b,vehicle))
print(issubclass(car,vehicle))
