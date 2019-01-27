'''
def main():
	print("its an entry point function")
	
if __name__==__main__:
	main()
'''	
	
'''
F:\Jay\Python Programs>python
Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import day7
>>>
>>> day7.main()
its an entry point function
>>> day7.__name__
'day7'
>>>

#for each python module __name__ is assigned with two values
if __name__ is run as individual script they its default value is __main__ or else if its imported then __name__ variable has default value is name of the file

'''	

#Write a program in arithmatic.py and it contains add, substract, multiply and division operations
'''
def add(no1,no2):
	return(no1+no2)

def sub(no1,no2):
	return(no1-no2)
	
def mul(no1,no2):
	return(no1*no2)
	
def div(no1,no2):
	if(no2==0):
		print("Division is not Possible")
	else:	
		return(no1/no2)
	
def main():
	x,y=eval(input("Enter the values"))
	print("addition is "+ str(add(x,y)))
	print("substraction is "+ str(sub(x,y)))
	print("multiplication is "+ str(mul(x,y)))
	print("division is "+ str(div(x,y)))
	

if __name__=='__main__':
	main()
	
'''	

"""
#Keyword arguments  (new feature of python)
def add(a,b,c):
	return a+b+c

print(add(10,20,30))
#print(add(b=10,c=20,40))this will show error argument follows keyword argument (intermixing error)
print(add(10,c=19,b=30)) #works fine because of the new functionality of python that is kayword arguments
#print(add(c=10,19,b=30)) intermixing error
		
"""

#Homework
#Write a program to accept a number from user and check if it is palindrome or not 
#Check for palindrome string
#Write a program to convert arithmatic.py into menu driven program
#Write a program to accept a number from user and check if its prime or not
#Write a program to print following patter
		'''	*
			* *
			* * *
			* * * *
			print statement takes you directly to new line'''	
			