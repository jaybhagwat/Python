
#WAP to accept a file name from user and number of lines to copy to another file.

import sys

def copyline(input_file,output_file,number):
	source=open(input_file)
	dest=open(output_file,"w")
	
	count=1
	
	line=source.readline()
	
	while line!='':
		if count>number:
			break
		else:	
			dest.write(line)
			line=source.readline()
			count+=1
	else:
		print("complete file copied")
		source.close()
		dest.close()

def main():
	if len(sys.argv)!=4:
		print("please enter the input")
	else:	
		copyline(sys.argv[1],sys.argv[2],int(sys.argv[3]))
	
	

if __name__=='__main__':
	main()
		
	
"""
for running on CMD type:
>python program_file_name source_file Dest_file number_of_line
>python newtemp.py temp.py dest.txt 10	
"""
