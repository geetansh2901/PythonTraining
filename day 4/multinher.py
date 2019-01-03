'''class father():
    def skills(self):
        print('I love gardening')
class mother():
    def skills(self):
        print('I love cooking')
class child(mother,father):
    def skills(self):
        father.skills(self)
        mother.skills(self)
        print('I enjoy sports')
c=child()
c.skills()'''
class human():
    def __init__(self,n='',g='',o='',s='',d=''):
        self.l=dict(name=n,gender=g,occupation=o,speaks=s,do_work=d)
    def show(self):
        print(self.l)
a=human('Tom Cruise','Male','Actor','I am Ethan Hunt of Mission Impossible','Shoots Movie')
b=human('Maria Sharapova''Female','Tennis Player','I won 5 grand slams','Play Tennis')
a.show()
b.show()