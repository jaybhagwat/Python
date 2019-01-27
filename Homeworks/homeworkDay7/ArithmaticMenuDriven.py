#Write a program to convert arithmatic.py into menu driven program

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
		
def menu():
	print("1.Addition")
	print("2.Substraction")
	print("3.Multiplication")
	print("4.Division")
	
	ch=eval(input("Enter your choice"))
	
	if(ch==1):
		x,y=eval(input("Enter the values"))
		print("addition is "+ str(add(x,y)))
	elif(ch==2):
		x,y=eval(input("Enter the values"))
		print("substraction is "+ str(sub(x,y)))
	elif(ch==3):
		x,y=eval(input("Enter the values"))
		print("multiplication is "+ str(mul(x,y)))
	elif(ch==4):
		x,y=eval(input("Enter the values"))
		print("division is "+ str(div(x,y)))
		
def main():

	ch1='y'
	while(ch1=='y'):
		ch1=str(input("to continue press 'y' else press any other character"))
		menu()
	else:
		print("exit")
	
	
if __name__=='__main__':
	main()
