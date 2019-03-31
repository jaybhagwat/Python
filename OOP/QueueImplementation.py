#HW:Implement Queue class

class Queue:
	def __init__(self,size):
		print("We are insinde Construction %d",size)
		self.__queue=[]
		self.__size=size
		
	def __del__(self):
		print("we are insinde distructor")
		del self.__queue
		

	def Enqueue(self,data):
		if self.isfull():
			print("Queue is full")
			
		else:
			self.__queue.append(data)
			print("queue after adding element is:",self.__queue)
		
	def Dequeue(self):
		if self.isempty():
			print("Queue is empty")
		else:	
			ele=self.__queue.pop(0)
			print("Popped ele is",ele)
			
	def isempty(self):
		return self.__queue == []
		
	def isfull(self):
		return len(self.__queue) == self.__size
	
def main():
	q=Queue(10)
	q.Enqueue(12)
	q.Enqueue(13)
	q.Enqueue(14)
	q.Enqueue(15)
	q.Dequeue()
	
if __name__=='__main__':
	main()
	
	
"""
F:\Jay\Python Programs\OOPS>Queue.py
('We are insinde Construction %d', 10)
('queue after adding element is:', [12])
('queue after adding element is:', [12, 13])
('queue after adding element is:', [12, 13, 14])
('queue after adding element is:', [12, 13, 14, 15])
('Popped ele is', 12)
we are insinde distructor

"""	
	
	
