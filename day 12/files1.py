'''file object=open(fiename[,access model])
fileobject.close();
fileobject.write(string)
'''


'''def main():
    infile=open('lines.txt','r')
    outfile=open('new.txt','w')
    for line in infile:
        print(line,file=outfile,end='')
    print('Done  ')
main()

'''
def main():
    buffersize=50000#assume buffersize
    infile=open('bigfile.txt','r')
    outfile=open('new1.txt','w')
    buffer=infile.read(buffersize)
    while(len(buffer)):
          outfile.write(buffer)
          print('.',end='')
          buffer=infile.read(buffersize)
          print()
    print('done.......')
main()