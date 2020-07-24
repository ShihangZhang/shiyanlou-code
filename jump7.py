for i in range(1,101):
	if isinstance(i/7,int):
		continue
	elif i%10==7:
		continue
	elif i//10==7:
		continue
	else:	
		print(i)

