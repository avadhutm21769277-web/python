
# Problem Statement 4.5 :   Write a program which contaons filter(),map(),reduce() in it.Pyrhon application which contains one list of numbers,
#                           List contains numbers accepeted by users > filter should filter out all prime numbers > Map function will multiply each 
#                           number by two. Reduce will retuen maximum number from that list.


#                           input       :       [2,70,11,10,17,23,31,77]
#                  list afater filter   :       [2,11,17,23,31]
#                  list after map       :       []4,22,34,46,62]
#                  output of reduce     :       62






def filter_function(numbers):
    prime_list=[]

    for num in numbers:
        if num>1:
            for i in range(2,num):
                if num%i==0:
                    break
        else:
            prime_list.append(num)

     return prime_list
            









def main():

    print("Enter number of elements that you want to store into list")
    number_of_element=int(input())
    print("user list:",number_of_element)


    print("Enter the elements that you want store into a list by using space")
    user_list=list(input().split())
    print("your list is:",user_list)

    #converting user_list into integaer_user_list

    interger_user_list=[]
    for i in user_list:
        interger_user_list.append(int(i))
    print("Integer list is:",interger_user_list)

    fdata=filter_function(interger_user_list)
    print("filter data is:",fdata)




if __name__=="__main__":
    main()