#write a program to accept a file name from user and delete comments from it
import re
def DeletingCommentFromPyFile(input_file):
	try:
		fd=open(input_file)
		data=fd.read()
		x=re.sub(r"'''(.|\s|\n)*?'''","",data)
		file=open("NewFile.txt","w+")
		file.write(x)	
		file.close()
		
		f1=open("NewFile.txt","r")
		f2=open("OutputFile.txt","w")
		line=f1.readline()
		
		while line!='':
			
			i=re.match(r"\A(#)",line)
			if i==None:
				f2.write(line)
			else:
				pass
			line=f1.readline()	
	finally:
		pass
		

def main():
	input_file=input("Enter file name")
	DeletingCommentFromPyFile(input_file)

if __name__=='__main__':
	main()
	
#final output is in OutputFile.txt	
