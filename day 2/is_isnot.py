a=1
b=1
if(a is b):
	print('a and b have same identity')
else:
	print('a and b have different identities')
b=0
if(a is not b):
	print('a and b have different identities')
else:
	print('a and b have same identity')