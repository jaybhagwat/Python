

#WAP to acccpet number and number of bits to turn ON from given position.(hint: use OR and just shift without compliment)
'''
def Bitwise(no1,nbit,pos):
		x=(1<<nbit)-1
		x=x<<(pos-nbit)
		return no1|x
		
def main():
	no1=eval(input("Enter the number"))
	bit,pos=eval(input("Enter number of bits and postion"))
	print(Bitwise(no1,bit,pos))
	
			
if __name__=="__main__":
	main()	
	
'''
#Write a program to check whether given number is multiple of 512 or not without using arithmatic operator
'''	
def MultipleOf512(no):
	count=0
	while(no!=0):
		no1=no%2
		if(no1==1):
			count=count+1
		no=no/10
	if(count!=1):
		return False
	else:
		return True
		
def main():
	no1=eval(input("Enter the number"))
	x=MultipleOf512(no1)
	
	if(x==True):
		print("Number is multiple of 512")
	else:
		print("It is not multiple of 512")
	
			
if __name__=="__main__":
	main()	


'''
'''
#Write a program to accept any 2's power and print its table upto 10 in binary	
def Twospower(no):
	for i in range(10):
		print(bin(no))
		no=no<<1
		
def main():
	no1=eval(input("Enter the number"))
	x=Twospower(no1)
	
			
if __name__=="__main__":
	main()	

'''	
'''
#Write a program to accept a number from user and count number of 0 bits in it(check processor bit)
def Numberofzero(no):
	count=0
	while(no!=0):
		count+=1
		no=no&(no-1)
	return 64-count	
	
def main():
	no1=eval(input("Enter the number"))
	print(Numberofzero(no1))
	
			
if __name__=="__main__":
	main()	

'''	
'''
#Write a program to accept two numbers from user , accept number of bits and bit position, swap correspondinf bits of both the numbers from the given position
	Ex input: no1:01000100 no2:00110110 pos:3 
	   output:no1:01101100 no2:00100110
		1.Get xpart and ypart
		2.Turn off respecive bits from both the numbers
		3.x|ypart and y|xpart

	   
def BitsSwappint(no1,no2,bitno,bitpos):
	x=(1<<bitno)-1
	x=x<<(bitpos-bitno)
	y=x
	x=x&no1
	y=y&no2
	no1=no1&~x
	no2=no2&~y
	xres=no1|y
	yres=no2|x
	print("After swapping the bits numbers are",xres,yres)
	
def main():
	no1,no2=eval(input("Enter the numbers"))
	bitno,bitpos=eval(input("Enter the number of bits and their position"))
	BitsSwappint(no1,no2,bitno,bitpos)
	
			
if __name__=="__main__":
	main()				
	
'''