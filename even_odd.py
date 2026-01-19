
#problem statement 1.2:  write a program which contains one function named as ChkNum() which accept one parameter as number . If number is even it should display 
#                        "Even number" otherwise display "odd number" on console
#                         
#                        input : 11                             output :   odd number
#                        input : 8                              output :   even number






def ChkNum(number):
    

    if number%2 == 0 :
        print("Even number")

    else:
        print("Odd number")


def main():
    print("enter the number")
    num=int(input())

    ChkNum(num)
    
    



if __name__=="__main__":
    main()