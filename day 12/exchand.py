'''try:
    fh=open('lines.txt')
    for line in fh:
        print(line.strip())
except IOError as e:
    print('file does not exists!',e)
    '''
def main():
    try:
        for line in readfile('lines.txt'):
            print(line.strip())
    except IOError as e:
        print('cannot read file: ',e)
    except ValueError as e:
        print('Bad file name: ',e)
def readfile(filename):
    if filename.endswith('.txt'):
        fh=open(filename)
        return fh.readlines()
    else:
        raise ValueError('Filename must end with .txt')
main()