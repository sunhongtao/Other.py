_author_='Hunter'
'''
	统计每个用户的出度和入度
'''
f=open('Lastresult.txt','r')

def Dealin(self,name):
	Output = open('%.txt'%name,'w')
	degree = {}
	list1 = []
	for line in f:
		a,b = line.strip('\n').split(',')
		a = int(a)
		b = int(b)
		if b not in degree:
			degree[b] = 1
		else:
			degree[b] += 1
	for key in degree.keys():
		list1.append(int(key))
	list1 = sorted(list1)
	for i in range(len(list1)):
		fout.write(str(list1[i])+','+str(degree[list1[i]])+'\n')
	f.close()
	fout.close()

def Dealout(self,name):
	Output = open('%.txt'%name,'w')
	degree = {}
	list1 = []
	for line in f:
		a,b = line.strip('\n').split(',')
		a = int(a)
		b = int(b)
		if a not in degree:
			degree[a] = 1
		else:
			degree[a] += 1
	for key in degree.keys():
		list1.append(int(key))
	list1 = sorted(list1)
	for i in range(len(list1)):
		fout.write(str(list1[i])+','+str(degree[list1[i]])+'\n')
	f.close()
	fout.close()
	
if __name__ =="__main__":
	Dealin('indegree') #compute the indegree
	Dealout('outdegree') # compute the outdegree