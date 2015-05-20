f = open('Lastresult.txt','r')
f1 = open('exchange.txt','a+')

for line in f:
    a,b=line.strip('\n').split(' ')
    c = b+' '+a
    f1.write(c+'\n')
f.close()
f1.close()
