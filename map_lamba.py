










from functools import reduce


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

    filtered=list(filter(lambda i : i>=70 and i<=90, interger_list))
    print("your filtered data is",filtered)

    mapped=list((lambda j: j+10, filtered))
    print("your mapped data is:",mapped)

    
    reduced=reduce(lambda k,y:k*y, mapped)
    print("your reduced output is:",reduced)



    



if __name__=="__main__":
    main()