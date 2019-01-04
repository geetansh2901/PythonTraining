    fh=open('lines.txt')
    for line in fh:
        print(line.strip())
except IOError as e:
    print('file does not exists!',e)
finally:
    print('No matter what block')
    fh.close()