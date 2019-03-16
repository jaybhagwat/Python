#Write a program to accept two number and find their gcd
'''
def Gcd(no1,no2):
		if(no1>no2):
			x=no1
		else:
			x=no2
		while(x!=2):
			if((no1%x==0) & (no2%x==0)):
				return x
			x=x-1
			
def RecursiveGcd(no1,no2):
		if no1==no2:return no1
		if(no1>no2):
			return RecursiveGcd(no1-no2,no2)
		return RecursiveGcd(no1,no2-no1)	
			
def Gcd1(no1,no2):
		while(no1!=no2):
			if no1>no2:
				no1=no1-no2
			else:
				no2=no2-no1
		return no1	
				
def main():
	no1,no2=eval(input("Enter the numbers"))
	x=RecursiveGcd(no1,no2)
	print(x)
	x=Gcd(no1,no2)
	print(x)
	x=Gcd1(no1,no2)
	print(x)		
			
if __name__=="__main__":
	main()	
	
'''
"""	

#Write a program to accept two numbers from user , accept number of bits and different bit position, swap correspondinf bits of both the numbers from the given position

def BitsSwappint(no1,no2,bitno,bitpos1,bitpos2):
	x=(1<<bitno)-1
	x=x<<(bitpos1-bitno)
	y=(1<<bitno)-1
	y=y<<(bitpos2-bitno)
	if(bitpos1>bitpos2):
		x=x>>(bitpos1>bitpos2
	
	
	x=x&no1
	y=y&no2
	no1=no1&~x
	no2=no2&~y
	xres=no1|y
	yres=no2|x
	print("After swapping the bits numbers are",xres,yres)
	
def main():
	no1,no2=eval(input("Enter the numbers"))
	bitno,bitpos1,bitpos2=eval(input("Enter the number of bits and their position"))
	BitsSwappint(no1,no2,bitno,bitpos1,bitpos2)
	
			
if __name__=="__main__":
	main()			
	
	
"""	
"""
howework
		1.make menu driven program of bitwise operatorsssss
		2. Write a program to add two numbers without using arithmatic operator (hint:or,and,shift)
		3.Draw stack frame with input 128,24 for recursive Gcd
		4.Write a recursive program to find the length of a string
		5.Write a recursive program to extarct digits from the string input:j4wbwejt323nk output:4323
		6.Write a recursive program to coount number of 1 bits in it without using arithmatic operator
		
Recursion:
			A function calling itslef is nothing but recursion 
			there are two types of recursion 
			1.Direct
			2.Indirect
			
		
		"""	

#Write a recursive program to find factorial of a number

def RecFactorial(no):
	if(no==0 | no==1):
		return 1
	if no==2:
		return 2
	return no*RecFactorial(no-1)

	
def main():
	print(RecFactorial(4))
	
if __name__=='__main__':
	main()