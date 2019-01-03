class employee:
    flag=0
    def __init__(self,name='Blank',salary=0.0):
        self.n=name
        self.s=salary
        self.l=[self.n,self.s]
        employee.flag+=1
    def showd(self):
        print(self.l)
emp1=employee('Zara',2000.0)
emp2=employee('Nishant',67000.0)
emp1.showd()
emp2.showd()
print('Total Employee: ',employee.flag)