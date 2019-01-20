from sqlp import *
c='y'
while c is 'y':
    c=input('Enter your choice:\n1.Insert to table\n2.Update table\n3.Delete from table\n4.Search in table\n5.View complete table')

    if c is '1':
        insert1()
    elif c is '2':
        update2()
    elif c is '3':
            delete3()
    elif c is '4':
        search4()
    elif c is '5':
        view()
    c=input('Do you want to continue?(y/n)')