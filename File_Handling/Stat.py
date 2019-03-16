
#Homework:WAP to accept a file neme from user and print its statistical information like type of file , sizeof file, permissions.
#hint( use stat , fstat)
import sys,os

def main():
	input_file=eval(input("Enter the file name"))
	fd=os.stat(input_file)
	print(fd)
	

if __name__=='__main__':
	main()