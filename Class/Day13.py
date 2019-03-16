#Write a program to accept a list from user and print it reverse order using recursion
#Write a program to accept a string from user and print it reverse order using recursion
#this code will work on both string and list inputs.

'''
def RecusriveRev(list):
	if len(list)==0:
		return	
	RecusriveRev(list[1:])	
	print(list[0])
	
def main():
	input_list=eval(input("Enter the list"))
	RecusriveRev(input_list)

if __name__=='__main__':
	main()
'''	
	
#Write a program to accept a container from user and print it reverse order using recursion	
#incomplete code complete it at home.
'''
def RecusriveContainer(l1):
	if len(list)==0:
		return	l1
	x=RecusriveRev(l1[1:])	
		return x.append(l1[0])
	
def main():
	input_list=eval(input("Enter the list"))
	RecusriveRev(input_list)

if __name__=='__main__':
	main()
'''	
	
#HW:Write a program to accept two list from user sort them and write the function to merge the two sorted list preserving the sort order.
'''
def Bubblesort(input_list):
	x=len(input_list)
	while x!=0:
		for i in range(x-1):
			if input_list[i]>input_list[i+1]:
				temp=input_list[i]
				input_list[i]=input_list[i+1]
				input_list[i+1]=temp
		x=x-1		


def SortingTwoString(l1,l2):
	Bubblesort(l1)
	Bubblesort(l2)
	l3=[]
	i=0
	j=0
	while i < len(l1) and j < len(l2) :
		if l1[i]>l2[j]:
			l3.append(l2[j])
			j +=1
		else:
			l3.append(l1[i])
			i +=1
	
	if i <len(l1):
		l3.extend(l1[i:])
	if j <len(l2):
		l3.extend(l2[j:])
			
	return l3		

def main():
	input_list1=eval(input("Enter the list1"))
	input_list2=eval(input("Enter the list2"))
	output_list=SortingTwoString(input_list1,input_list2)
	print(output_list)
	
	
if __name__=='__main__':
	main()
'''	
'''
Output:
F:\Jay\Python Programs>python Day13.py
Enter the list1[8,6,9,7,3]
Enter the list2[2,3,4,5,3,2]
[2, 2, 3, 3, 3, 4, 5, 6, 7, 8, 9]	
'''
#HW:WAP to accept two list from user and find uinon of them

#HW:WAP to accept two list from user and find intersection of them

#HW:WAP to accept two list from user and find symmetric difference of them

#HW:WAP to accept two list from user and check if l2 is subset of l1

#HW:WAP to accept two list from user and check if l2 is disjoint of l1

#HW:WAP to accept two list from user and check if l2 is superset of l1
