num1 = 11101
num2 = 1101

a=[1,1,1]
b=[1,1,1]

def mult(a,b):
	print 'a='+str(a)
	print 'b='+str(b)
	mx = max(a,b)
	if mx==a:
		mn=b
	else:
		mn=a
	shift=0
	l=len(mn)
	i=0
	sum=[]
	mx1=[]
	print 'mx='+str(mx)
	print 'mn='+str(mn)

	while(shift<l):
		if(mn[shift]==1):
			sum=add(mx,sum)
			print 'sum='+str(sum)

		mx=prependZero(mx)
		shift+=1
	print 'mult returned'+' product='+str(sum)
	print '================='
	print '================='
	return sum


def add(a,b):
	print 'adding: a= '+str(a)+' and b= '+str(b)
	carry=0
	mx = max(a,b)
	if mx==a:
		while len(a)!=len(b):
			b.append(0)
	else:
		while len(b)!=len(a):
			a.append(0)
	print 'a='+str(a)
	print 'b='+str(b)
	row=[]
	for i in range(len(a)):
		row.append('')
		row[i]=0
		row[i]+=a[i]
		row[i]+=b[i]
		row[i]+=carry
		if row[i]==2:
			carry=1
			row[i]=0
		elif row[i]==3:
			row[i]=1
			carry=1
		else:
			carry=0
	row.append(carry)
	j=len(row)-1
	while(row[j]==0):
		del row[j]
		j=-1
	print 'add returned '+str(row)
	print '================='
	print '================='
	return row

def delZeros(numList):
	if numList==[]:
		return []
	j=len(numList)-1
	print 'len(numList)='+str(len(numList))
	print 'numList='+str(numList)
	while(numList[j]==0):
		del numList[j]
		if numList==[]:
			break
		j=-1
	print 'delZeros returned '+str(numList)
	print '================='
	print '================='
	return numList

def max(a,b):	
	print 'max function first: a= '+str(a)+' and b='+str(b)
	a=delZeros(a)
	b=delZeros(b)
	print 'max function sec: a= '+str(a)+' and b='+str(b)
	if len(a)<len(b):
		max=b
	elif len(b)<len(a):
		max=a
	elif len(b)==len(a):
		if (a==[]):
			max=b
		elif (b==[]):
			max=a
		elif b[(len(b)-1)]<a[(len(a)-1)]:
			max=a
		else:
			max=b
	return max

def prependZero(binaryNumList):
	newList=[0]
	newList.extend(binaryNumList)
	print 'prependZero returned '+str(newList)
	print '================='
	print '================='
	return newList


def test_suite():
	passed = True
	passed = (mult([1,1,1],[1,1,1]) == [1,0,0,0,1,1]) and passed
	print 'passed 1?'+str(passed)
	
	passed = (mult([1,0,1,0,1],[1,1,1,0,1]) == [1,1,0,0,0,1,1,1,1]) and passed
	print 'passed 2?'+str(passed)
	passed = (mult([0,1,1],[1,0,0,1,1]) == [0,1,1,0,1,0,0,1]) and passed
	print 'passed 3?'+str(passed)
	passed = (mult([0,0,1,1,0,1],[1,0,1,1]) == [0,0,1,1,1,1,0,0,0,1]) and passed
	print 'passed 4?'+str(passed)
	passed = (mult([0,0,1,1,0],[1,1,1]) == [0,0,1,0,1,0,1]) and passed
	print 'passed 5?'+str(passed)
	passed = (mult([0,0,1,1,0],[1,1,1,0,1]) == [0,0,1,0,1,0,0,0,1]) and passed
	print 'passed 6?'+str(passed)
	
	return passed

print mult(a,b)
test_suite()
