

# Problem Statement 1.3  :  write a program which contains one function named Add() which accepts two numbers from user and return addition of that two numbers:
#                           input : 11   5                        output : 16




def Add(value1,value2):
    result=0
    result=value1+value2
    return result


def main():
    print("enter the first number")
    num1=float(input())

    print("enter the second number")
    num2=float(input())

    answer=Add(num1,num2)
    print("your addition result is : ",answer)



if __name__=="__main__":
    main()


