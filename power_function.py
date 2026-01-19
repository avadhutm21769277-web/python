

#Problem Statement4.1:  write a program contains one lamda function which accepts one parameter and return power of two
#                       input   :   4           output  :   16
#                       input   :   6           output  :   36





power=lambda number:number**2               #Lambda function for power
    


def main():

    print("enter the number")               #getting input from the user
    num1=int(input())

    answer=power(num1)                      #calling the lambda function
    print("your answer is:",answer)         


if __name__=="__main__":
    main()