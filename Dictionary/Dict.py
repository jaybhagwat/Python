#WAP to accept a sentence from user and return dictionary containing count of each characters occuring in it.
def Dictionary(inp_str):
	result={}
	for ch in inp_str:
		if result.get(ch) != None:
			result[ch] += 1
		else:
			result[ch]=1
	
	return result
		

def main():
	inp_str=eval(input("Enter a sentence"))
	d1=Dictionary(inp_str)
	 	
	print(d1)
	

if __name__=='__main__':
	main()
	
#WAP to accept a paragraph from user and return a dictionary of count of words in the given paragraph	
	
def Dictionary(inp_str):
	result={}
	for ch in inp_str.split():
		if result.get(ch) != None:
			result[ch] += 1
		else:
			result[ch]=1
	
	return result

def main():
	inp_str=eval(input("Enter a sentence")
	result=Dictionary(inp_str)
	
	for x in result
		print(result,result[x])
	

if __name__=='__main__':
	main()
		

#Homework
#WAP to accept a sentence which contains uppercase and lowercase characters, return a dictionary containing 
#count of total number of lower case characters and total number of uppercase characters.

def Dictionary4(inp_str):
	uppercase=0
	lowercase=0
	for ch in inp_str:
		if chr(ch)>=65 and chr(ch)<=90:
			dict[uppercase]+=1
		elif chr(ch) >=97 and chr(ch)<=122:
			dict[lowercase]+=1
			
	return dict		

def main():
	inp_str = "i Am Jay Bhagwat"
	res=Dictionary4(inp_str)
	print(inp_str)
	
	print(res)

if __name__=='__main__':
	main()



#WAP to acccept number from user and return a dictionary of squares from 1 till that number


def Dictionary3(num):
	result={}
	while num !=0:
		result[num]=num*num
		num = num-1
	
	return result
		

def main():
	inp=eval(input("Enter a numeber"))
	d1=Dictionary3(inp)
	 	
	print(d1)
	

if __name__=='__main__':
	main()
	
