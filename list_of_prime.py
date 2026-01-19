

# Problem Statement 3.2 :   write a program whoch accept N numbers from user and store into the list.Return maximun number from that list

#                           Input :  no of elements  :7
#                           input elements :        13 5 45 7 4 56 34
#                           output                  56




def max_number_of_list(input_list):
    empty_list=[]
    for i in input_list:
        empty_list.append(int(i))

    print("here is your list in the integer format",empty_list)

    maximum_number_from_the_list=max(empty_list)
    return maximum_number_from_the_list




def main():

    print("enter the number of elements ")
    number_of_elements=int(input())
    print("you should enter ",number_of_elements,"elemets")
    print("enter the elements into the list")
    user_list=list(input().split())
    print(user_list)
    
    
    result=max_number_of_list(user_list)
    print("the maximum number from the list is:",result)





if __name__=="__main__":
    main()