
def FileHandling():
	fd=open("petrol.txt","r")
	line=fd.readline()
	maharashtra=0
	goa=0
	karnataka=0
	cnt=0
	while(line!=''):
		res=line.split()
		maharashtra+=int(res[2])
		goa+=int(res[3])
		karnataka+=int(res[4])
		cnt+=1
		line=fd.readline()	
	
	fd1=open("petrol_avg_out.txt","w")
	fd1.write(str(maharashtra/cnt)+str(" ")+str(goa/cnt)+str(" ")+str(karnataka/cnt)+str(" "))
	fd1.close()1
	fd.close()
	
	
def main():
	FileHandling()

if __name__=='__main__':
	main()
	
#Homework:WAP to accept a file neme from user and print its statistical information like type of file , sizeof file, permissions.
#hint( use stat , fstat)

#WAP to accept a file name from user and number of lines to copy to another file.	

#WAP to accpet a foldername from user and create a zip file out of it.(hint= import shutil)

# Study:File input, File cmp,Tmep file. 