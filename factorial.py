
#       Problem Statement 2.3  : Write a program which accept one number from user and return its factorial
#                               input   :   5               Output  :   120






def factorial(number):
    result=1
    for i in range(1,number+1):
        result *= i
    return result






def main():
    print("enter the number")
    num=int(input())
    if num >=1:

        answer=factorial(num)
        print("Factorial is:",answer)

    else:

        print("its invalid to get factorial woth number 0")



if __name__=="__main__":
    main()