

#Problem Statement 3.3: write a program which accept N numbers fron user and stored into the list .Return minimun number from that list.
#
#                       input               :       number of elements :   4
#                       input elemnts       :       13 5 45 7
#                       outpt               :       5



def minimum_number_of_list(user_list):
    empty_list=[]
    for i in user_list:
        empty_list.append(int(i))

    print("here is your integer format list")

    min_no_from_list=min(empty_list)
    return min_no_from_list



def main():

    print("enter the number of elemts")
    no_of_elements=int(input())

    print("you should enter",no_of_elements,"elemnts only")

    print("enter the elemnts into the list")
    elements_list=list(input().split())

    print("your list is",elements_list)

    answer=minimum_number_of_list(elements_list)
    print("mininum number from the list is:",answer)



if __name__=="__main__":
    main()