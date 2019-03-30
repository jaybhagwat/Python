"""
In python there are no access specifier.
You can make them sudo private.
In python class is also an object
By making class an object it makes the python most powerful language by means you can create class at runtime.
Every object intenally is a dictionary
#learn object specific attribute
"""

#Write a program to implement the complex number on your own
#add two complex numbers,substract,multiply a complex number by an integer
class Complex:
	def __init__(self,r1=0,i1=0):
		self.__real=r1
		self.__img=i1
		
	def __del__(self):
		print("We are inside Distructor")
		
	def add(self,c2):
		real=self.__real+c2.__real
		img=self.__img+c2.__img
		
		print(real,"+",img,"i")
	
	def sub(self,c2):
		real=self.__real-c2.__real
		img=self.__img-c2.__img
		
		print(real,"-",img,"i")
		
	def mul(self,num):
		real=self.__real*num
		img=self.__img*num
		print(real,"*",img,"i")
			
		
def main():
	c1=Complex(10,20)
	c2=Complex(20,30)
	c1.add(c2) 	
	c2.sub(c1)
	c1.mul(19)

if __name__=='__main__':
	main()
