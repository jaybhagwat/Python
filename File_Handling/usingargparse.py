
#WAP to accept a file name from user and number of lines to copy to another file.
import argparse
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
	print(sys.argv)
	parser=argparse.ArgumentParser()
	parser.add_argument("-i",type=str,help="Input/Source File Name",required=True)
	parser.add_argument("-d",type=str,help="Destination File Name",required=True)
	parser.add_argument("-n",help="Number of lines to copy,default 0",default=0,type=int)
	args=parser.parse_args()
	copyline(args.i,args.d,args.n)
		
if __name__=='__main__':
	main()
		
	
	
"""
for running on CMD type:
>python program_file_name -i source_file -d Dest_file -n number_of_line
>python usingargparse.py -i temp.py -d dest1.txt -n 20

Books:
automate the boring stuff using python
headfirst python	
"""	