class curr:
    def __init__(self,code,extd):
        self.amt=0.00
        self.code=code
        self.extd=extd
    def setamt(self,amt):
        self.amt=amt
    def in_curr(self,amt):
        return amt/self.extd
    def td(self,amt=None):
        tc=self.amt
        return tc*self.extd
    def __eq__(self,o):
        return self.td()==o.td()
    def __gt__(self,o):
        return self.td()>o.td()
    def __lt__(self,o):
        pass
    def __le__(self,o):
        pass
    def __ge__(self,o):
        pass
    