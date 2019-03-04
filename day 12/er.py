'''try:
    fh=open('lines.txt')
    a=1/0
except IOError as e:
    print('file does not exists!',e)
finally:
    print('No matter what block')
    fh.close()
    
     given a list(channels)
    implement a  remote that allows to press next to go to next channel
    at last channel->first channel'''

a=['Aaj Tak','NDTV India','India TV','Star Sports','Sony SIX','Star Sports Select','Discovery','History TV 18','AXN','HBO']
b=iter(a)
count=-1
for i in range(len(a)):
    print(next(b)) 
    count+-1
b=reversed(a)
for i in range(len(a)):
    print(next(b))
