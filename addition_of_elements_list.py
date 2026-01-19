

#problem Statement 3.1 : Write a program which accept N numbers from user and store it into List.Return Addition of all elemnts from that list.

#                           input              :       number of elemts :6
#                           input elements     :       13 5  45 7 4 56
#                           output             :       136






def main():

    print("enter the number of elements")                           #Taking number of input from user
    no_of_elements=int(input())

    print("enter the elements in to the list")                      #Getting user inputs in the form of list
    elements_in_list=list(input().split())

    print(elements_in_list)

    print(len(elements_in_list))                                    #length of list

    integer_list=[]                                                 #creating empty list

    for i in elements_in_list:
        integer_list.append(int(i))                                 #adding the elements into empty list in the integer format

    print(integer_list)

    print(sum(integer_list))


if __name__=="__main__":
    main()