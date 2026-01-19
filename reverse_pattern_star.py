

#problem Statement 2.6 :    write a program which accept on number and display below pattern
#                               input   :   5
#
#                               output  :   *   *   *   *   *
#                                           *   *   *   *
#                                           *   *   *
#                                           *   *
#                                           *





def main():

    print("enter the number")
    number=int(input())

    for i in range(number,0,-1):
        print(i*'*')


if __name__=="__main__":
    main()