import Multiplication
import Division
import Addition
import Remainder

def menu():
    a=int(input("Enter the first number"))
    b=int(input("Enter the second Number"))
    x=int(input("Enter : 1 for Addition , 2 for multiplication , 3 for division and 4 for modulus"))
    if(x==1):
    	Addition.fun(a,b)
    elif(x==2):
    	Multiplication.multi(a,b)
    elif(x==3):
    	Division.division(a,b)
    elif(x==4):
    	Remainder.Remainder(a,b)
    else:
    	print("please enter the correct choice")
		

menu()



 

	


	

	





