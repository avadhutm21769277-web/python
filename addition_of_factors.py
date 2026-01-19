

# Problem Statement 2.4:  write a program which accept one number from user and return addition of its factors
#                           input=12           output=16





def Facto_addition(num):                                              #creat a function 
    answer=0
    for i in range(1,num):
        
        if num%i==0:                                                 # if reminder become zero then it should be factor
            print("this are the factors:",i)
            answer+=i                                                # addition of all the factors
    print(answer)




def main():

    print("enter the number")               #taking user input in the integer format
    number=int(input())

    Facto_addition(number)                  #calling the user defined function 


if __name__=="__main__":
    main()



