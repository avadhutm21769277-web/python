

#problem statement 2.10 : write a program which accept number from user and return addition of digits in that number
#                           input : 5187934             output=37








def Addition_of_digits(number):
    count=0
    if number==0:
        count=1

    else:
        while number!=0:
            number=number//10
            count+=1
    print(count)
    result=0
    for i in count:
        result+=i
        print(result)





def main():
    print("enter the number")
    num=int(input())
    answer=Addition_of_digits(num)
    print("Addition of digit is:")



if __name__=="__main__":
    main()