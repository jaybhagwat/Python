#Write a program to demonstrate queue data structure with following opetaions 1.enque 2.deque 3.is queue empty 4.is queue full(FIFO or LILO)

def Enqueue(list,data):
	list.insert(0,data)
	print(list)
	
def Dequeue(list):
	return list.pop()

def IsFull(list):
	return len(list)==10
	
def IsEmpty(list):
	return list==[]
	

def Queue_operations(list):
	print("Enter the operation you want to perform")
	print("1.Enqueue elemtnt 2.Dequeue element 3.To see the queue")
	print("press q to exit")
	choice=eval(input("Enter Your choice"))
	
	if choice==1:
		data=eval(input("Enter the element"))
		if IsFull(list):
			print("Queue is Full")
			print("\r")
		else:
			Enqueue(list,data)
		
	elif choice==2:
		if IsEmpty(list):
			print("Queue is empty")
			print('\r')
		else:
			result=Dequeue(list)
			print(result)
			print('\r')
	
	elif choice==3:
		print(list)
		print('\r')
		print('\r')
			
	elif choice=='q':
		print("Exitting from the Queue")
		return
		
	else:
		print("Invalid input")
		Queue_operations(list)
		
	Queue_operations(list)
	

def main():
	print("Queue implementation")
	list=eval(input("Enter the list"))
	Queue_operations(list)

if __name__=='__main__':
	main()