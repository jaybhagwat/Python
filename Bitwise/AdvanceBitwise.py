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
	
	
#.Write a recursive program to coount number of 1 bits in it without using arithmatic operator

def CountRecBits(no)
	if no == 0
		return 0
	return 1+CountRecBits(no & (no-1))	
	
def main():
	x=eval(input("Enter the number"))
	CountRecBits(x)
	
if __name__=='__main__':
	main()
	
	