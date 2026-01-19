
#   Problem Statemnt    2.8:    write a program which accept one number and display below pattern:
#                               input   :   5   
#                               output  :   1
#                                           1   2   
#                                           1   2   3   
#                                           1   2   3   4
#                                           1   2   3   4   5




def main():
    print("enter the number")
    number=int(input())

    for i in range(1,number+1,1):
        
        for j in range(1,i+1,1):
            print(j,end='')

    print()


if __name__=="__main__":
    main()