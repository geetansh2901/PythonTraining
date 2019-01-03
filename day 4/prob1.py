class vehicle:
    def __init__(self,name='Blank',color='Blank',Type='Blank',worth=0.0):
        self.n=name
        self.c=color
        self.t=Type
        self.w=worth
    def showd(self):
        print('{} is a {} {} worth {}.'.format(self.n,self.c,self.t,self.w))
veh1=vehicle('Fer','red','convertible',60000.0)
veh2=vehicle('Jump','blue','van',10000.0)
veh1.showd()
veh2.showd()