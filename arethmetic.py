

# Problem Statement 5.1:    Arethmetic operations on two numbers
#                           write a program to accept two integers from user and display their:
#                           1.sum       2.difference    3.product   4.division




def addition(value1,value2):
    sum=value1+value2
    return sum

def difference(value1,value2):
    diff=value1-value2
    return diff

def multiplication(value1,value2):
    multi=value1*value2
    return multi

def division(value1,value2):
    divis=value1/value2
    return divis



def main():

    print("enter the first number")
    number1=float(input())

    print("enter the second number")
    number2=float(input())

    add=addition(number1,number2)
    print("addition is:",add)

    dif=difference(number1,number2)
    print("difference is:",dif)

    mul=multiplication(number1,number2)
    print("multiplication is:",mul)

    div=division(number1,number2)
    print("division is:",div)



if __name__=="__main__":
    main()