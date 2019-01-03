class person:
    def __init__(self,first,last):
        self.firstname=first
        self.lastname=last
    def __str__(self):
        return self.firstname+" "+self.lastname
class person1:
    def __init__(self,first,last):
        self.name=first+last
    def __str__(self):
        return self.name
class employee(person,person1):
    def __init__(self,first,last,staffno):
        super().person.__init__(first,last)
        super().person1.__init__(first,last)
        self.staffnum=staffno
x=person('Rick','Sanchez')
z=person1('')
y=employee('Jerry','Mouse','420')
print(x)

print(y)