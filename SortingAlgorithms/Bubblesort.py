#HW:Implement BUBBLE sort and INSERTION sort.

def Bubblesort(input_list):
	x=len(input_list)
	while x!=0:
		for i in range(x-1):
			if input_list[i]>input_list[i+1]:
				temp=input_list[i]
				input_list[i]=input_list[i+1]
				input_list[i+1]=temp
		x=x-1		


def main():
	input_list=eval(input("Enter the List you want to sort"))
	Bubblesort(input_list)
	print(input_list)

if __name__=='__main__':
	main()
	
'''
Output:
F:\Jay\Python Programs>python Bubblesort.py
Enter the List you want to sort[7,4,8,3,2,1]
[1, 2, 3, 4, 7, 8]	
'''