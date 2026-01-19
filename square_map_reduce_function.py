

# Problrm Statement 4.4:    write a program which contains filter(),map() and reduce(). python application which contains one list of number.list contains
#                           the numbers which are accepted from user.Filter should filter out such numbers which are even. map function will calculate its square.
#                           reduce will return addition of all that numbers.

#                           input list          =       [5,2,3,4,3,4,1,2,8,10]
#                           List after filte    =       [2,4,4,2,8,10]
#                           List after map      =       [4,16,16,4,64,100]
#                           Output              =       204




def filter_data(fdata):
    result=0
    result_filtered=[]
    for i in fdata:
        if (i%2==0):
            result_filtered.append(i)
    return result_filtered
    

def mapped_data(evendata):
    result=1
    result_mapped=[]
    for i in evendata:
       
       result_mapped.append(i**2)
    return result_mapped

def reduced_data(squaredata):
    add=0
    for i in squaredata:
        add+=i
    return add

        




def main():

    print("enter the number of elements that you want to stoared into the list")
    number1=int(input())
    print("you should enter",number1,"elements only")


    input_list=list(input().split())
    print("your input list is:", input_list )

    input_int_list=[]
    for i in input_list:
        input_int_list.append(int(i))
    print("here is your integer format list",input_int_list)

    even_filtered_data=filter_data(input_int_list)
    print("your filtered data is:",even_filtered_data)

    square_mapped_list=mapped_data(even_filtered_data)
    print("your mapped list is:",square_mapped_list)

    addition_reduce_list=reduced_data(square_mapped_list)
    print("your reduced output is:",addition_reduce_list)

    





if __name__=="__main__":
    main()