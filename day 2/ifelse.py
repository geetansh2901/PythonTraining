import random
'''food='spam'
if(food=='spam'):
    print('Ummm, my favorite!')
    print('I feel like saying it 100 times...')
    print(100*(food+'!'))
   ''' 
    
# if value>43 print large
# if value>35 and <=43  medium
#if value >25 and <=35  small
# if <25 not eligible
# The value 43 is samll


a=random.randint(0,45)
if(a<=25):
    print('The value of a={} which is not eligible'.format(a))
elif(a>25 and a<35):
 print('The value of a={} which is small'.format(a))
elif(a<43 and a>35):
 print('The value of a={} which is medium'.format(a))
else:
     print('The value of a={} which is large'.format(a))