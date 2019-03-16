"""
homework	1
1
1 2
1 2 3
1 2 3 4 
1 2 3
1 2
1

Homework 2

1 2
2 4 8
3 6 12 24
4 8 16 32 64

"""
"""
def Pattern(n):
	for i in range(1,n+1):
		k=i
		for j in range(1,i+2):
			print(i,end='')
			k*=2
		print()	

def main():
	Pattern(5)
			
if __name__=="__main__":
	main()
"""	
	
"""

HOmework 3
1 2
2 4 6
3 6 9 12	
4 8 12 16 20

"""

"""
homework 4
4 3 2 1 *
3 2 1 * *
2 1 * * *
1 * * * *
* * * * *

"""

#WAP to acccpet number and number of bits to turn ON from given position.(hint: use OR and just shift without compliment)
"""
def Bitwise(no1,nbit,pos):
		
	

def main():
	no1=eval(input("Enter the number"))
	nbit=3
	pos=4
	Bitwise(no1,nbit,pos)
	
			
if __name__=="__main__":
	main()	
	
"""	
"""
homweowk
Write a program to check whether given number is multiple of 512 or not without using arithmatic operator
Write a program to accept any 2's power and print its table upto 10 in binaryk
	
"""

#Write a program to accept a number from user and accept the bit position and number of bit to toggle to the given position
#input:00000111010 4
#output:00000110101

"""
def Bitwise(no1,pos,bits):
	x=(1<<bits)-1
	x=x<<(pos-bits)
	return no^x

def main():
	no1=eval(input("Enter the number"))
	pos=4
	bits=3
	print(Bitwise(no1,pos,bits))
	
			
if __name__=="__main__":
	main()	
"""
#Write a program to accept a number from user and turn off right most 1 bit from it.	
def bit(no):
	x=1
	while(no&x)==0:
		x=x<<1
	return no&~x	
	
def bit2(no)
	return no&(no-1)
	
def main():
	no=eval(input("Enter the number"))
	print(bit(no))
	print(bit2(no))
	
			
if __name__=="__main__":
	main()		
	
#Write a program to count number of 1 bits in a given number 	
def bit2(no)
	count=0
	while(no!=0):
		count+=1
		no=no&(no-1)
	return count	
	
def main():
	no=eval(input("Enter the number"))
#	print(bit(no))
	print(bit2(no))

if __name__=="__main__":
	main()	

"""	
#homework	
#Write a program to accept a number from user and count number of 0 bits in it(check processor bit)
#Write a program to accept two numbers from user , accept number of bits and bit position, swap correspondinf bits of both the numbers from the given position
	Ex input: no1:01000100 no2:001101101 pos:3 
	   output:no1:01101100 no2:001001101
		1.Get xpart and ypart
		2.Turn off respecive bits from both the numbers
		3.x|ypart and y|xpart
		
	   
				
