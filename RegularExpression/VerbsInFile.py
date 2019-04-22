#Homework:Write a program to accept a file name from user and print all verbs in it.
import re
def VerbsInFile(input_file):
	try:
		fd=open(input_file)
		fs=open("verbs.txt","w")
		regex_verbs=re.compile(r"(\w+)(ing\b)|(\w+)(ly\b) ")
		data=fd.read()
		for i in regex_verbs.finditer(data):
			print(i.group(0))
			fs.write(str(i.group(0))+"\n")
	finally:
		fd.close()
		fs.close()
		

def main():
	input_file=input("Enter file name")
	VerbsInFile(input_file)

if __name__=='__main__':
	main()
