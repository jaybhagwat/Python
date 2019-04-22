import functools
def square(x):
	return x*x

y=lambda y:y*y
print(y(9))

x=lambda x,y:[y*y,x*x]
print(x(3,4))
	
def generator(x):
	return lambda n:n+x
	
generator_of_5=generator(5)
print(generator_of_5(10))


generator_of_10=generator(10)
print(generator_of_10(10))	
'''
#Python supports multiparadigm.
'''
x= map(square, 	range(1,30,2))
for i in x:
	print(i)
	
y=map(lambda y:y**y,range(5))
for j in y:
	print(j)
	
def Iseavn(n):
	return (n&1==0)
	 
z=map(Iseavn,range(0,10)) #map maps the data
for i in z:
	print(i)

q=filter(Iseavn,range(1,20)) #filter returns the filered out data, first argument of filter shoud return trur/false
for i in q:
	print(i)
	
def multiply(x,y):
	print(x,y)
	return x*y
	
w= functools.reduce(multiply,range(1,10)) #for reduce functools modue should be imported
print(w)



#yield in python

def yielddemo():
	i=0
	for i in range(10):
		yield i
		
x=yielddemo()
print(next(x))		
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
