'''class MyClass:
    variable='blah'
    def function(self):
        a=10
        print('This message is inside the class.')
        return a
myobjx=MyClass()
print(myobjx.variable)
myobjx.function()
print(myobjx.function())'''

class complexn:
    def __init__(self,r=0,i=0):
        self.real=r
        self.imag=i
    def getData(self):
        print("{0}+{1}j".format(self.real,self.imag))
myobj=complexn(10,5)
myobj.getData()
