

# Problem Statement 2.1 :   Write a program which accpet one number from user and display below pattern

#                       Input : 5               Output :        *   *   *   *   *
#                                                               *   *   *   *   *
#                                                               *   *   *   *   *
#                                                               *   *   *   *   *
#                                                               *   *   *   *   *






def Display(num):

    for i in range(num):
        for j in range(num):
            print("*",end=" ")
        print()



def main():
    print("enter the number")
    number=int(input())
    Display(number)



if __name__=="__main__":
    main()