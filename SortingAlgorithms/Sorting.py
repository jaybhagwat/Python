#WAP to accept a integer list from user and check if it is sorted or not.

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
	
'''
Output:
F:\Jay\Python Programs>python Day12.py
Sorting
Enter the list of integeers[3,2,1,8,5,6]
[1, 2, 3, 5, 6, 8]
'''
