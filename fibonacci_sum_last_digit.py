def pisano(m):
	a,b=0,1
	for i in range(0,m*m):
		c=(a+b)%m
		a,b=b,c
		if(a==0 and b==1):
			return i+1
def huge(n,m):
	a,b=0,1	
	sum=1
	p=pisano(m)	
	n=n%p
	if(n<=1):
		return n
	for i in range(2,n+1):
		c=a+b
		b,a=c,b
		sum=sum+c
	return sum%10
n=int(input())
print(huge(n,10))