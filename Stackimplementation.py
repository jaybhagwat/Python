#Write a program to implement Stack operations

def Push(list,data):
	list.append(data)
	print(list)
	
def Pop(list):
	return list.pop()

def Peep(list):
	return list[-1]

def IsFull(list):
	return len(list)==10
	
def IsEmpty(list):
	return list==[]
	

def Stimulate_Stack_operations(list):
	print("Enter the operation you want to perform")
	print("1.Push elemtntprint 2.Pop element 3.peep 4.To see the stack")
	print("press q to exit")
	choice=eval(input("Enter Your choice"))
	
	if choice==1:
		data=eval(input("Enter the element"))
		if IsFull(list):
			print("Stack is Full")
			print("\r")
		else:
			Push(list,data)
		
	elif choice==2:
		if IsEmpty(list):
			print("Stack is empty")
			print('\r')
		else:
			result=Pop(list)
			print(result)
			print('\r')
		
	elif choice==3:
		result=Peep(list)
		print(result)
		print('\r')
	
	elif choice==4:
		print(list)
		print('\r')
		print('\r')
		
	
	elif choice=='q':
		print("Exitting from the stack")
		return
		
	else:
		print("Invalid input")
		Stimulate_Stack_operations(list)
		
	Stimulate_Stack_operations(list)
	

def main():
	print("Stack")
	list=eval(input("Enter the list"))
	Stimulate_Stack_operations(list)

if __name__=='__main__':
	main()

