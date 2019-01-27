#Write a program to print following patter
'''	
			*
			* *
			* * *
			* * * *
			print statement takes you directly to new line
'''	

def PrintPattern(no):
	for i in range(no+1):
		for j in range(i):
			print("* ",end="")
		print("")	
			
def main():
	PrintPattern(4)
	
if __name__=='__main__':
	main()