#Write a program to accept three numbers from user and print minimum out of them
'''
a,b,c=eval(input("Enter three numbers"))
if a<b and b<c:
	print(a)
elif b<c:
	print(b)
else:
	print(c)
'''	
#Rewrite the validation of string rotation code using if else
j=str(input("Enter first String"))
k=str(input("Enter second String"))
if(len(j)==len(k)):
	temp=j+j
	if(k in temp):
		print("String is rotational")
	else:
		print("String is not rotational")

#write a program to accept number of donuts as an input if number of donuts are greater than 10 then print "Number of donuts : many" else "Number of donuts: respective count"
'''
x=eval(input("Enter the number of donuts"))
if x>10:
	print("Number of donuts :","many")
else:
	print("Number of donuts :",x)
'''	
#write a program to accept a string from user and return a string having frst two and last two characters of input string ex if input is "spring then op "spng"
'''
input_string=str(input("Enter the string"))
if(len(input_string)>4):
	result=input_string[:2]+input_string[-2:]
else:
	result=input_string
print(result)
'''	
