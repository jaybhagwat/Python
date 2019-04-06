	"""
HW:implement a bank accoun class which should support deposit and widraw method should be supported 
can autogenerate account number by taking an class attribute
"""
class BankAccount:
	auto_acc_number=1
	
	def __init__(self,name,bal=0):
		self.__name=name
		self.__bal=bal
		self.acc_number=BankAccount.auto_acc_number
		BankAccount.auto_acc_number=BankAccount.auto_acc_number+1
	
	def widraw(self,amount):
		if self.__bal < amount:
			print("Insufficient Amount")
			return -1
		else:
			self.__bal=self.__bal-amount
			print( " Amount is deducted",amount)
			print("Current Balance is:",self.__bal)
		
	def deposit(self,amount):
		self.__bal=self.__bal+amount
		print("Amount Deposition Successfull")
		print("Current Balance is:",self.__bal)
	
	
			
def main():
	
	c1=BankAccount("jay",10000)
	c2=BankAccount("Veer",100000)
	c1.widraw(1000)
	c2.deposit(40000)
	
	

if __name__=='__main__':
	main()

