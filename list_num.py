



# Problem Statement 3.5 :   Write a program which accepts N numbers from user and stored into a list.Return Addition of all prime numbers from that list.
#                           Main python file accepts N numbers from User and pass each number to Chkprime() which is part of our user defined module
#                           named as Marvellousnum. Name of the function from python main python file should be Listprime().

#                           Input                   :               number of elements      :       11
#                           Input Elements          :   13  5   45  7   4    56  10  34  2   5   8
#                           Output                  :       54      (13+5+7+2+5)












def main():



    print("enter the num of elements ")
    number1=int(input())

    print("enter the elements into the list by using <space key>")

    userlist=list(input().split())
    print("here is your list",userlist)

    empty_list=[]
    for i in userlist:
        empty_list.append(int(i))
    print("your integer format List is:",empty_list)
    Chkprime.(empty_list)


if __name__=="__main__":
    main()

