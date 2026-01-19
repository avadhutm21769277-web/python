
# Problem Statement:        create on module named as Arithmetic which contains 4 functions as Add() for addition, sub() for substraction
#                           mul() for multiplication, div for division. All functions accepts two parameters as number and perform the operation .
#                           Write on python program which can call all the functions from Arithmetic modeule by accepting the parameters from user.




from assignment_2_1_arithmeticmodule import *



def main():

    print("Enter the first number")         # Accepting the Input from the User
    value1=float(input())
    print("Enter the second number")
    value2=float(input())

    Add_answer=Add(value1,value2)           #calling the Functions 
    Sub_answer=Sub(value1,value2)
    Mult_answer=Mult(value1,value2)
    Div_answer=Div(value1,value2)

    print("Addition is:",Add_answer)            # printing the output of each function 
    print("Substraction is:",Sub_answer)
    print("Multiplication is:",Mult_answer)
    print("Division is:",Div_answer)
    

if __name__=="__main__":
    main()
