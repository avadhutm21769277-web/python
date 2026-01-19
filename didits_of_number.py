

# Problem Statement 2.5:    Write a program which accept one number from user and check whether it is prime not.
#                           input   :   5                   output  :   It is a prime number




def Checkprimenumber(number):

    if number<1==0:
        print("prime number is always greater than 1")

    else:
        for i in range(2,number):
             if number%i==0:
                print("not prime")
                break
        else:
            print("prime number")



def main():
    print("enter the number")
    num=int(input())
    Checkprimenumber(num)


if __name__=="__main__":
    main()