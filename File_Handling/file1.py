#WAP to accept file from user and print it line by line

def ReadLinebyLine(inputfile):
	f=open(inputfile,"r")
	if f!=None:
		line=f.readline()
		while line!='':
			print(line)
			line=f.readline()
			
def main():
	inputfile=input("Enter File path")
	ReadLinebyLine(inputfile)
	fd=open(inputfile,"r")
	print(fd.read())

if __name__=='__main__':
	main()

	
##WAP to accept file name from user and print those lines who have 
#less than equal to 80 characters. Also print line numbers which have 
#more than 80 characters stating that line are having more than standard count of characters

def Lines(inputfile):
	fd=open(inputfile)
	linenumber=[]
	line_no=1
	line=fd.readline()
	while(line!=''):
		if len(line)<80:
			print(line)
		else:
			linenumber.append(line_no)
			
		line_no +=1
		line=fd.readline()
		
	print("Lines number which has more than 80 characters are",linenumber)	
		
	
def main():
	inputfile=input("Enter File path")
	Lines(inputfile)
	
i(f __name__=='__main__':
	main()


#WAP to accept file from user and print smallest and longest line from it	

def Lines1(inputfile):
	fd=open(inputfile)
	
	line=fd.readline()
	maxline=line
	minline=line
	
	while(line!=''):
		line=fd.readline()
		if line=='\n' or line=='':
			continue
		elif len(line) > len(maxline):
			maxline=line
		elif len(line) < len(minline):
			minline=line
	
	return maxline,minline	
		

def main():
	inputfile=input("Enter File path")
	maxline,minline=Lines1(inputfile)
	print("Maxline = {}\nMinline={}".format(maxline,minline))
	
if __name__=='__main__':
	main()

#WAP to accept file from user and print those lines which have THE word more than once.

def Lines2(inputfile):
	fd=open(inputfile)
	line=fd.readline()
	outputline=[]
	cnt=0
	while line!='':
		cnt=line.count("the")
		print(cnt)
		if line=='\n' or line=='':
			continue
		elif cnt>1:
			outputline.append(line)
			
		line=fd.readline()
		
	print(outputline)		

def main():
	inputfile=input("Enter File path")
	Lines2(inputfile)
	
if __name__=='__main__':
	main()

	