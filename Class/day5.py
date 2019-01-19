#Control flow 
"""
	-Sequence of statements
	-Selection:if- else
				ex,
					if<condition>:
						<body of if> 
						<body of if>
						<body of if>
						
						
						
		#write a program to accept two numbers from user and substract minimum from maximum
		
		"""
"""
x,y=eval(input("enter the nunbers"))
#y=int(input("Enter another number"))
if(x>y):
	print(x-y)
else:
	print(y-x)
					
					
#write a program to accept 3 numbers from user and print maximum out of it					
a,b,c=eval(input("Enter the numbers"))
if(a>b and a>c):
	print(a)
elif(b>c):
	print(b)
else:
	print(c
	
#Write a program to accept three numbers from user and print minimum out of them
#Rewrite the validation of string rotation code using if else


	-Python doesnt have switch case
	

#Write a program to accept a sentence from user and replace the not bad construct if found with good 
j=str(input("Enter the sentence"))
if("not bad" in j):
	print(j.replace("not bad","good"))
else:
	print(j)
	
		
#another solution
input_string=input("Enter statement having not bad")
not_index=input_string.find("not")
if not_index!=-1:
	bad_index=input_string.find("bad")
	if bad_index!=-1 and bad_index>not_index:
		result=input_string[:not_index]
		result+="good"
		result+=input_string[bad_index+3:]
print(result)
	"""
#write a program to accept a string from user and perform verbing operations on it
'''length should be grater than or equal to 3
add ing to its end it its not present
if it is ending with ing then ing should be replaced by ly	'''
input_str=input("Enter the sring")

if(len(input_str)>=3):
	bad_index=input_str.find("ing")
	if bad_index!=-1:
		result=input_str[:"ing"]
		result+="ly"
		print(result)
	else:
		result=input_str+"ing"
		
if(len(s))>=3:
	if s.endswith('ing'):
		s=s[:-3]+'ly'
	else:
		s+='ing'
print(s)


#homework
"""
#write a program to accept number of donuts as an input if number of donuts are greater than 10 then print "Number of donuts : many" else "Number of donuts: respective count"
#write a program to accept a string from user and return a string having frst two and last two characters of input string ex if input is "spring then op "spng"
		