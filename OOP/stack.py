
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
	st.push(10)
	st.push(40)
	st.push(99)
	st1=Stack(23)
	st1.default=23
	st1.push(23)
	
	print(st.pop())		
	print(st._Stack__size)#accessing the psudo private variable of the class by using name mangling
	#print("Object Dictionary:",st.__dict__)
	#print("class Dictionary:",Stack.__dict__)
	
	
			
if __name__=='__main__':
	main()
