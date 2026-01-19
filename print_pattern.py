

# Problem Statement 2.7 :   write a program which accept one number and display below pattern:
#                           Input   :   5
#
#                           output  :   1   2   3   4   5
#                                       1   2   3   4   5
#                                       1   2   3   4   5
#                                       1   2   3   4   5
#                                       1   2   3   4   5



def main():

    print("enter the number")

    number=int(input())

    for i in range(number):
        for j in range(1,number+1):
            print(j,end=' ')
    print()


if __name__=="__main__":
    main()