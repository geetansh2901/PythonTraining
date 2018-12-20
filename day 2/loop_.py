i=0
for i in range(5):
    print('i is now ',i)
    
for f in ['Margot','Scarlett','Emilia']:
    invitation='Hi '+f+'. Please come to the party!!!!'
    print(invitation)
    
'''#The While Statement
name='Harrison'
guess=input("So I'm thinking of a person's name. Try to guess it: ")
pos=0
while guess!=name and pos<len(name):
    print("Nope, that's not it! Hint: letter ",end="")
    print(pos+1,"is",name[pos]+".",end="" )
    guess=input(' Guess Again: ')
    pos=pos+1
if pos==len(name) and name!=guess:
        print("Too bad , you couldn't get it. The name was ",name+".")
else:
    print("\nGreat, you got it in ",pos+1," guess(es)")'''
    
for i in [12,16,17,24,29,30,51]:
    if i>25:
        print('passed')
        pass
    elif i%2==1:
        continue
    elif i%5==0:
        break
    print(i)