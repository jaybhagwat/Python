#Check for palindrome string

def StringPalindrome(str_input):
	str_new=str_input[::-1]
	if(str_input==str_new):
		return True
	else:
		return False

def main():
	str=input("Enter the String")
	ret=StringPalindrome(str)		
	
	if(ret==True):
		print("Sring is palindrome")
	else:	
		print("String is not palindrome")

if __name__=='__main__':
	main()
	
