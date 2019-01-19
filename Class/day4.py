s="jay"
print(s)
print(s.capitalize()) 
#this does not changes the actual string but returns a new string because string is immutable
x="babble"
print(x[0]+ x[1:].replace(s[0],'*'))


#write a program to accept a string from user and jumble it in such a way that from the beginnign are considered in first part and second part contains alternate characters starting from the second part
#input:'jeetendra' output:'jeedaetnr'

q='jeetendra'
print(q)
r=q[::2]+q[1::2]
print(r)

#input:'jeetendra' output:'adeejrnte'
t=q[::-2]+q[-2::-2]
print(t)


"""python has inbuilt containers
	they are
	1)string
	2)list=it accepts heteregeneous data,list is mutable(it can be modified)
	3)tuple=it is immutable
	4)set=it contains unique elements,it is assciative container,internally uses hash table.
	5)dictionary=Compete associative array with key value pair.
"""



#--------OPERATORS--------------
"""
Arity=number of operator an operator takes
	-unary,binary
	
Precedence=(priority-BODMAS)

Associativity=when there is same precendence in an expression then associativity comes into picture
				-Right to left=unary,combinational assignments,ternary
				-Left to Right=all other except above operators
				
Unary operators=
	-Python doesnt suppoert increment and decrement operators,It had only not operator
	
Binary operators=*,+,-,%,//,**

Relational operator=<,>,<=,>=,!=,==,<>(2.7ver)(depricated in 3.xver)

Logical operator= and, or, not.

Membership operator=in ,not in
				Ex:	'j' in 'jeetendra'
					 true
					 
Identity operator=is, is not (both of these looks for memory id)(these operators compares id but not value the value

Bitwise Operator=
			&- turn off bit/bits
				ex.
					0110110111
				&	1111111001
				---------------
					0110110001
			
			|- turn on bit/bits
				ex.
					01001000101
				|	00000111000
				----------------
					01001111101
					
			^- Toggle bit/bits
				ex.
					0100101000
					0000111100
				---------------
					0100010100
					
			~- Bit inversion
				ex.
				~  00001010
				------------
				   11110101

			<< - Left Shift (multiplication by 2's power)
				ex.
					00001010<<1    (10)
					------------
					00010100<<1    (20)
					------------
					00101000       (40) 
					
			>> -  Right Shift 
					It is categorized under two subcategory= Arithmatic Right Shift=Appends 1 to Msb(to negative number)
															 Logical Right Shift=Appends 0 to Msb
					
"""

print(-5%3)
print(5%3)
print(-5%-3)

print(5/2)
print(5//2)#explicit operator is there which can support flood division
print(5**3)#** is exponential operator





#Homework
#Go through presentation no 2
#Write a program to accept a string from user and check if it starts with capital 't'
#Write a program to accept two strings from user and check if second string is rotation of first  Input:1.manager 2.germana Output=True
#write a program to accept a string from user and convert it to lowercase, upppercase.
