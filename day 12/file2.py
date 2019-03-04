def main():
    buffersize=50000#assume buffersize
    infile=open('olives.jpg','rb')
    outfile=open('new2.jpg','wb')
    buffer=infile.read(buffersize)
    while(len(buffer)):
          outfile.write(buffer)
          print('.',end='')
          buffer=infile.read(buffersize)
          print()
    print('done.......')
main()