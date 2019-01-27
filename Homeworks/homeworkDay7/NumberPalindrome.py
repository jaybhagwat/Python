#Write a program to accept a number from user and check if it is palindrome or not 

def NumberPalindrome(no):
	rev=0
	no2=no
	while(no>0):
		dig=no%10
		rev=rev*10+dig
		no=no//	10
		
	if(no2==rev):
		return True
	else:	
		return False
	
def main():
	print("now you are in main")
	no1=eval(input("Enter the number"))
	ret=NumberPalindrome(no1)		
	
	if(ret==True):
		print("Nummber is palindrome")
	else:	
		print("Number is not palindrome")

if __name__=='__main__':
	main()
	