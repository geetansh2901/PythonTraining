l=['Geetansh','Karan','Harsh','Mayank','Nitin']
infile=open('names.txt','r')
outfile=open('names1.txt','w')
for line in infile:
        for word in line.split():
            if word not in l:
                print(word,file=outfile,end='\n')
print('done')