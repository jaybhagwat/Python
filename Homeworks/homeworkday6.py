#Programs using functions
'''
#Write a program to accept a string from user and check if it starts with capital 't'
s=str(input("Enter the String"))
def StringChk(s):
	print('T' in s[0])

StringChk(s)	
'''

#Write a program to accept two strings from user and check if second string is rotation of first  Input:1.manager 2.germana Output=True
'''
j=str(input("Enter first String"))
k=str(input("Enter second String"))

def Rotational(j,k):
	if(len(j)==len(k)):
	temp=j+j
	if(k in temp):
		print("String is rotational")
	else:
		print("String is not rotational")
	
Rotational(j,k)

'''
#write a program to accept a string from user and convert it to lowercase, upppercase.
'''
z=str(input("Enter the string"))
def CaseFlip(z):
	if(z.islower()):
		print(z.upper())
	else:
		print(z.lower())
		
CaseFlip(z)

'''

#Write a program to accept three numbers from user and print minimum out of them
'''
No1,No2,No3=eval(input("Enter three numbers"))

def MinimumNo(n1,n2,n3):
	if(n1<n2 and n1<n3):
		print(n1,"is the minimum")
	elif(n2<n3):
		print(n2,"is Minimum")
	else:
		print(n3,"is minimum")
	
MinimumNo(No1,No2,No3)

'''
#write a program to accept number of donuts as an input if number of donuts are greater than 10 then print "Number of donuts : many" else "Number of donuts: respective count"
'''
x=eval(input("Enter the number of donuts"))
def Donuts(x):
	if x>10:
		print("Number of donuts :","many")
	else:
		print("Number of donuts :",x)		
		
Donuts(x)
'''
#write a program to accept a string from user and return a string having frst two and last two characters of input string ex if input is "spring then op "spng"

input_string=str(input("Enter the string"))

def StringTrim(str):
	if(len(input_string)>4):
		result=input_string[:2]+input_string[-2:]
	else:
		result=input_string
	print(result)
	
StringTrim(str)	
