#Write a program to accept a file name from user and print all the words starting with small or capital t and ending in small or capital e

import re

def Regular(input_file):
	parser=re.compile(r"T\b(\w+)\bE",re.IGNORECASE)
	line=input_file.readline()
	while line!='':
		output=parser.finditer(line)
		for i in output:
			i.group(0)
		line=input_file.readline()
	input_file.close()	
		

def main():
	input_file=open(input(),"r")
	Regular(input_file)

if __name__=='__main__':
	main()
