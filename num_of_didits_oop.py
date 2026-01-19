

# Problem Statement 2.4:  write a program which accept one number from user and return addition of its factors
#                           input=12           output=16




def factor_addition(value):

    result=0
    for i in range(1,value+1):
        result*=i  
        print(i)






def main():

    print("Enter the number")
    number=int(input())

    factor_addition(number)


if __name__=="__main__":
    main()