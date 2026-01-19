

#   Problem Statement :  Write a program which contains one function that accept one number from user and returns true if number is divisible by 5 otherwise return false
#                           input : 8                   output  :  false
#                           input : 25                  output  :  true



def true_false(number):
       is_divisable= (number%5 == 0)
       print(is_divisable)

       

def main():

    print("enter the number")
    value=int(input())

    true_false(value)


if __name__=="__main__":
    main()