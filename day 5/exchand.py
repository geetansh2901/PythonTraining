try:
    fh=open('lines.txt')
    for line in fh:
        print(line.strip())
except IOError as e:
    print('file does not exists!',e)