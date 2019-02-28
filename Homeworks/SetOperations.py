def Set_Operation (input_list1, input_list2):
    Set_intersection (input_list1, input_list2)
    Set_union(input_list1,input_list2)
    Set_SymmetricDifference(input_list1,input_list2)
    
def Set_SymmetricDifference(input_list1,input_list2):
    output_list3=[]
    for x in input_list1:
        if x not in input_list2:
            output_list3.append(x)
    
    for y in input_list2:
        if y not in input_list1:
            output_list3.append(y)
            
    print(output_list3)        
        

def Set_union(input_list1,input_list2):
    output_list = input_list1 
    for i in input_list2:
        if i not in output_list:
            output_list.append(i)
    print (output_list)
           
    
def Set_intersection (input_list1, input_list2):
    output_string1=[]
    for k in input_list1:
        for l in input_list2:
            if (k==l): 
               output_string1.append(k)
    print(output_string1)   
      
def main ():
    input_list1, input_list2 =eval(input("Enter the set")) 
    Set_Operation (input_list1,input_list2) 
    
if __name__== '__main__':
    main ()
