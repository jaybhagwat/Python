#Write a program to accept a filename from user and print all words having 'end' in batewwn	(hint:\B)
import re
def WordsContainingend(input_file):
	try:
		fd=open(input_file)
		fs=open("end.txt","w")
		regex_verbs=re.compile(r"\w+(\Bend)\w+")
		data=fd.read()
		for i in regex_verbs.finditer(data):
			print(i.group(0))
			fs.write(str(i.group(0))+"\n")
	finally:
		fd.close()
		fs.close()
		

def main():
	input_file=input("Enter file name")
	WordsContainingend(input_file)

if __name__=='__main__':
	main()
