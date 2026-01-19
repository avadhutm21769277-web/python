
#   Problem Statement 4.2   :   write a program which contains one lambda function which accepts two parameters and return its multiplication:
#                               Input   :   4   3           Output  :   12
#                               Input   :   6   3           Output  :   18







multiplication=lambda value1 , value2: value1*value2                #  lambda function for multiplication
    
def main():

    print("enter the first number")                                 #   Accepting two number from the user
    num1=int(input())
    print("enter the second number")
    num2=int(input())

    answer=multiplication(num1,num2)                                #     calling the lambda function
    print("your answer is:",answer)


if __name__=="__main__":
    main()