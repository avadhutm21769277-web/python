

#Problem Statement 3.4:  Write a program which accepts N numbers from user and stored into a list.Accept One another number from user 
#                        and return frequency of that number from list.

#                           input           :       number of elements :11
#                           input elements  :       13  5   45  7   4   56  5   34  2   5   65
#                           Elemet to search:       5
#                           output          :       3



def main():

    print("Enter the num of elements ")
    number=int(input())

    print("you should enter ",number,"elements only")

    element_list=list(input().split())

    print("your element list is:",element_list)

    empty_list=[]
    for i in element_list:
        empty_list.append(i)

    print("integer format list")
    print(element_list)

    print("enter another number for search into the list")
    number2=str(input())

    print("your searching is in progress please wait for countong of ...",number2)

    result=empty_list.count(number2)
    print("the frequncy of your number is:",result)


if __name__=="__main__":
    main()