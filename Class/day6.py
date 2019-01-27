'''
#Write a program to accept two strings from user and swap their first two characters
#input : dog dinner output:dig donner

x=input("Enter the first two strings")
y=input("Enter the first two strings")
str1=x[:2]
str2=y[:2]
x=str2+x[2:]
y=str1+y[2:]
print(x)
print(y)

#Control flow continue

	For loop-
		syntax= for <loop-variale> in <iterable-container>:
					<body of for>
					
		*range is an inbuilt function in python for iteration
			ex. for x in range(10)
					print(x)// it will print fro 0 to 9
				>>>for x in "india":
				...     print(x)
				...
				i
				n
				d
				i	
				a
				
				>>>for _ in range(10000) // here _ (underscore) is anonymous variable
						pass // this is time delay loop , it just delays time
						
				>>>#nested for loop
				>>>for x in range(10)
				>>>	   for y in range(5)
				>>>        print(x,y) #this is nested for loop
				
	'''
	
#write a program to accept integer from user and print its table
'''
x=eval(input("Enter the number"))
for y in range(1,11):
	print(x*y)
else:
	print("The table is complete")
'''	
	
#Homework=Write a program to accept an n integer form user and print tables from 2 to n

'''
	while loop-
		syntax=while <condition>
					<body>
					
				ex.
				>>>while ch!='n'
				>>>		print(ch)
				>>>		ch=input("Enter String, to stop enter n")
				
				
				
				
	Jump Statements=
		they help you to come out of the loop
			-Break,return,continue are the jump statements in python
	'''		
'''
i=0
while i<10:
	if(i%2==0):
		i+=1
		continue
	print(i)
	i+=1
else:
	print("Executed else of whilie")
	
'''				
#Write a program to accept a number from user and find its factorials
'''
x=eval(input("Enter the number"))
c=1
for y in range(1,x+1):
	c*=y
print(c)	
'''


#FUNCTIONS in python 
'''
Syntex(for declrating the function)=

		def function_name(argument to the Function):
			<body of the function>
			
'''

#ex.
def Factorial(n):
	result=1
	for x in range(2,n+1):
		result*=x;
	return result
	
print(Factorial(3))	

#Homework=Write all the programs to functions until then
