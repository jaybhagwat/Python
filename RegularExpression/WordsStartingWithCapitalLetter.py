#Write a program to accept a file name from user and print all the words starting with capital letters
import re
def WordsStartingWithCapital(input_file):
	try:
		fd=open(input_file)
		fs=open("Capital.txt","w")
		regex_verbs=re.compile(r"[A-Z]\w+")
		data=fd.read()
		for i in regex_verbs.finditer(data):
			print(i.group(0))
			fs.write(str(i.group(0))+"\n")
	finally:
		fd.close()
		fs.close()
		

def main():
	input_file=input("Enter file name")
	WordsStartingWithCapital(input_file)

if __name__=='__main__':
	main()
