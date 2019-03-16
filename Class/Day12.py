#.Write a recursive program to coount number of 1 bits in it without using arithmatic operator
'''		
def CountRecBits(no)
	if no == 0
		return 0
	return 1+CountRecBits(no & (no-1))	
	
def main():
	x=eval(input("Enter the number"))
	CountRecBits(x)
	
if __name__=='__main__':
	main()
	
	 
	 

'''

'''
List in Python:It is a collection of heterogeneous elements.
- List is a mutable container.
-List follows same indexing and slicing model of string.

>>> x=[1,2,'jay',4]
>>> type(x)
<class 'list'>
>>> x.append('bhagwat')
>>> print(x)
[1, 2, 'jay', 4, 'bhagwat']
>>> x.append([4,5,6])
>>> print(x)
[1, 2, 'jay', 4, 'bhagwat', [4, 5, 6]]
>>> x.extend([4,5,6])
>>> print(x)
[1, 2, 'jay', 4, 'bhagwat', [4, 5, 6], 4, 5, 6]
>>> x.extend(8)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not iterable
>>> x.insert(1,0)
>>> print(x)
[1, 0, 2, 'jay', 4, 'bhagwat', [4, 5, 6], 4, 5, 6]
>>> x.insert(3,'veer')
>>> print(x)
[1, 0, 2, 'veer', 'jay', 4, 'bhagwat', [4, 5, 6], 4, 5, 6]
>>> x[::-1]
[6, 5, 4, [4, 5, 6], 'bhagwat', 4, 'jay', 'veer', 2, 0, 1]
>>> x.pop
<built-in method pop of list object at 0x000001F5CA8A3F88>
>>> x.pop()
6
>>> x.pop(4)
'jay'
>>> print(x)
[1, 0, 2, 'veer', 4, 'bhagwat', [4, 5, 6], 4, 5]
>>> x.remove(3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
>>> x.remove('veer')
>>> print(x)
[1, 0, 2, 4, 'bhagwat', [4, 5, 6], 4, 5]


'''
'''
# Write a program to remove all occurances of given data from the list

def RmOccurance(list,data):
	while data in list:
		list.remove(data)

def main():
	y=eval(input("Enter the list"))
	x=eval(input("Enter the data"))
	RmOccurance(y,x)
	print(y)

if __name__=='__main__':
	main()
'''	
'''
	Output:
	
F:\Jay\Python Programs>python Day12.py
Enter the list[1,2,3,'jay',3]
Enter the data3
[1, 2, 'jay']	

'''

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

	
#Write a program to demonstrate queue data structure with following opetaions 1.enque 2.deque 3.is queue emoty 4.is queue full

#WAP to accept a integer list from user and check if it is sorted or not.
'''
def ChkSorting(list):
	for x in range(len(list)-1):
		if list[x]<list[x+1]:
			continue
		else:
			return False
			
	return True	

def main():
	print("Sorting")
	list=eval(input("Enter the list of integeers"))
	x=ChkSorting(list)
	if x==True:
		print("List of integer is sorted")
	else:
		print("List is not sorted")
	
if __name__=='__main__':
	main()

'''
"""	
#WAP to accept unsorted list of numbers and sort it.
	
def Sorting(list):
	for x in range(len(list)-1):
		for y in range(x+1,len(list)):	
			if list[x]>list[y]:
				temp=list[x]
				list[x]=list[y]
				list[y]=temp
			

def main():
	print("Sorting")
	list=eval(input("Enter the list of integeers"))
	Sorting(list)
	print(list)
	
if __name__=='__main__':
	main()
"""	
'''
Output:
F:\Jay\Python Programs>python Day12.py
Sorting
Enter the list of integeers[3,2,1,8,5,6]
[1, 2, 3, 5, 6, 8]
'''	

#HW:Implement BUBBLE sort and INSERTION sort.
