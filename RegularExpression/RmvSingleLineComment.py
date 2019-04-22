  import re
def DeletingCommentFromPyFile(input_file):
	try:
		fd=open(input_file)
		fs=open("FileWithoutComment.txt","w")
		regex_cmnt1=re.compile(r"\A(#)")
		#regex_cmnt2=re.compile("(\A''' '''\Z)|(\A""" """\Z)")
		line=fd.readline()
		while line!='':
			i=regex_verbs.match(line)
			#print(i)
			if i==None:
				fs.write(line)	
			line=fd.readline()
	finally:
		fd.close()
		fs.close()
		

def main():
	input_file=input("Enter file name")
	DeletingCommentFromPyFile(input_file)

if __name__=='__main__':
	main()
