

#   Problem Statement 4.3   :Write a program which contains filter(),map(),reduce() in it.python application which contaons one list of numbers.List contains the number
#                            which are accepted from user.Filter should filter out all such numbers which greater or equal to 70 and less than or equal to 90 .Map function
#                            will increae each number by 10. Reduce will return product of all that number

#                           input list          :   [4,34,36,76,68,24,89,23,86,90,45,70]
#                           list after filter   :   [76,89,86,90,70]
#                           list after map      :   [86,99,96,100,80]
#                           output of reduce    :   6538752000






def filter_function(list_data):

    
    filterdata=[]
    for i in list_data:
        if i>=70 and i<=90:
            print(filterdata.append(i))

    return filterdata


def map_function(list_filter):


    mapdata=[]
    for i in list_filter:
        i+=10
        print(mapdata.append(i))

    return mapdata

    



def reduce_function(mdata):
    result=1
    for i in mdata:
        result *= i

    return result
    










    













def main():

    print("enter the number of elements that you want to add into the list")

    number1=int(input())

    print("you should enter the",number1,"elements only")

    print("enter the"  ,number1, "elements into the list")

    input_list=list(input().split())

    print("here is your list",input_list)

    interger_list=[]
    for i in input_list:
        interger_list.append(int(i))
    print("integer format list :",interger_list)

    fdata=filter_function(interger_list)
    print("your filter data is:",fdata)

    mdata=map_function(fdata)
    print("your mapdata is",mdata)

    rdata=reduce_function(mdata)
    print("your reduce data is:",rdata)







if __name__=="__main__":
    main()