
	uid=[]
	result={}
	newresult={}
	f1=open("suid.txt",'r')
	f2=open("tuid.txt",'r')
	Fdegree=open("users' degree.txt",'w')
	for line1 in f1:
		str1=line1.strip('\n')
		if str1 in result:
			result[str1]+=1
		else:
			uid.append(str1)
			result[str1]=1
	for line2 in f2:
		str2=line2.strip('\n')
		if str2 in result:
			result[str2]+=1
		else:
			uid.append(str2)
			result[str2]=1
	print result.values()
	n = 1
	for i in result.keys():
		newresult[n] = result[i]
		n=n+1
	for i,j in newresult.items():
		Fdegree.write(str(i)+' '+str(j)+'\n')
	f1.close()
	f2.close()
	Fdegree.close()


