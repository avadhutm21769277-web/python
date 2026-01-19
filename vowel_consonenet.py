

#Problem Statement 5.6 :        Celcius to Fahrenheit Convertor
#                               Accepet temperature in celcious and convert it to Fahrenheit using the formula :    f=(c  *  9/5) + 32
#                               input : 25 C            output : 77.0  F



def celcious_to_fahrenheit_convertor(value):

    result=(value *  9/5) + 32
    return result


def main():

    print("enter the temperature in Celcious")
    ctemp=float(input())

    ftemp=celcious_to_fahrenheit_convertor(ctemp)
    print(" Temperature in  Faherenheit is: ",ftemp , "F")

if __name__=="__main__":
    main()