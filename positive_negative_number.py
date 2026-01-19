
#Problem Statement 1.6 : write a program which accept number from the user and check whethere the number is positive or negative or zero
#                               input :  11                              output  :  positive number
#                               input  : -8                              output  :  negative number
#                               input :  0                               output  :  zero





def positive_negative_or_zero(number):

    if number>0:
        print("positive number")
    if number<0:
        print("negative number")
    else:
        print("zero")


def main():
    print("enter the number")
    num=int(input())
    positive_negative_or_zero(num)


if __name__=="__main__":
    main()