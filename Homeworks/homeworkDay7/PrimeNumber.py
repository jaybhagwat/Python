#Write a program to accept a number from user and check if its prime or not

def ChkPrime(num):
	flag=0
	if(num%2==0):
		return False
	
	else:
		for i in range(3,num//2,2):
			if(i%num==0):
				flag=1
				
		if(flag==0):
			return True
		else:
			return False
			

def main():
	num=eval(input("Enter the Number"))
	ret=ChkPrime(num)
	
	if(ret==True):
		print("It is Prime number")
	else:
		print("It is not Prime Number")
	
	
if __name__=='__main__':
	main()
