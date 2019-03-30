
class Stack:
	
	def __init__(self,size):
		print("sTACK CONSTRUCTED OF SIZE %d"%size)
		self.__stack=[]
		self.__size=size
	
	def __del__(self):
		print("Inside Distructor")
		del self.__stack
	
	
	def isfull(self):
		return len(self.__stack) == self.__size
	
	def isempty(self):
		return self.__stack == []
		
	def push(self,num):
		if self.isfull():
			print("stack is full")
			status="FAILED"
		else:
			self.__stack.append(num)
			print(self.__stack)
			status="SUCCESS"
		return status	
	
	def pop(self):
	
		if self.isempty():
			print("stack is empty")
			status="FAILED"
		else:
			data=self.__stack.pop()
			print(self.__stack)
			status="SUCCESS"
			
		return status	
		
	
			
def main():
	st=Stack(10)
	
	print("Enter Your Choice for exit press 'q'")
	num=eval(input("1.Push  2.Pop"))
	
	while num==1 or num==2:
		
		if num==1:
			data=eval(input("Enter the data"))
			st.push(data)
		
		elif num==2:
			st.pop()
	
		num=eval(input("1.Push  2.Pop"))
	
	
			
if __name__=='__main__':
	main()


"""
1.Push  2.Pop1
Enter the data34
[34]
1.Push  2.Pop1
Enter the data56
[34, 56]
1.Push  2.Pop1
Enter the data76
[34, 56, 76]
1.Push  2.Pop2
[34, 56]
1.Push  2.Pop2
[34]
1.Push  2.Pop2
[]
1.Push  2.Pop2
stack is empty
"""
