#WAP to accept a list  of integer from user and check if its palindrome or not.


def List_Palindrome(input_list):
   i=0
   j=-1
   while i<len(input_list):
       if input_list[i]==input_list[j]:
           i=i+1
           j=j-1
       else:
           break
    
   if i==len(input_list):
       return True
   else:
       return False

def main():
    input_list=eval(input("Enter the list"))
    ret=List_Palindrome(input_list)

    if ret==True:
        print("List is Palindrome")
    else:
        print("List is not Palindrome")

if __name__=='__main__':
    main()