class remote():
    def __init__(self):
        self.a=['Aaj Tak','NDTV India','India TV','Star Sports','Sony SIX','Star Sports Select','Discovery','History TV 18','AXN','HBO']
        self.index=-1
    def __iter__(self):
        return(self)
    def __next__(self):
        if self.index==len(self.a)-1:
            self.index=0
        else:
            self.index+=1
        return self.a[self.index]
r=remote()
itr=iter(r)
for i in range(12):
    print(next(itr))