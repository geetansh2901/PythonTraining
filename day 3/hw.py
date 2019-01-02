usa=['atlanta','new york','chicago','baltimore']
uk=['london','bristol','cambrige']
india=['mumbai','delhi','banglore']
x=input('Enter a city: ')
if x in usa:
    print('usa')
if x in uk:
    print('uk')
if x in india:
    print('india')
    
x=input('Enter a city: ')
y=input('Enter another city: ')
if x in usa and y in usa:
    print('both cities are in usa')
if x in uk and y in uk:
    print('both cities are in uk')
if x in india and y in india:
    print('both cities are in india')