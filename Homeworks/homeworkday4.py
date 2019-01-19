#Write a program to accept a string from user and check if it starts with capital 't'

s=str(input("Enter the String"))
print('T' in s[0])

#Write a program to accept two strings from user and check if second string is rotation of first  Input:1.manager 2.germana Output=True
j=str(input("Enter first String"))
k=str(input("Enter second String"))
if(len(j)==len(k)):
	temp=j+j
	if(k in temp):
		print("String is rotational")
	else:
		print("String is not rotational")

#write a program to accept a string from user and convert it to lowercase, upppercase.
z=str(input("Enter the string"))
if(z.islower()):
	print(z.upper())
else:
	print(z.lower())