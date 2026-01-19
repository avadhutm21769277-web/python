

# Problem Statement 2.9 :   write a program which accept number from user and returns number of digit of that number
#                               input: 5187934         output:7



def countdigit(number):

        count=0

        if number==0:
         count=1

        else: 
            while number!=0:
             number =number//10
             count+=1
        print(count)



def main():
    print("enter the number")
    num=int(input())

if __name__=="__main__":
    main()





