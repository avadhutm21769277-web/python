

#   Problem Statement 5.7   : Area And Perimeter of Rectangel
#                             Accept teh length and width of a rectangle .Calculate Area and Perimeter of rectangle

#                               Input   :  length   :   5     Width    :   3
#                               Output  :  Area : 15           Perimeter   :   16







def main():

    print("enter the length")
    length=float(input())

    
    print("enter the width")
    width=float(input())


    area=length*width
    print("Area of Rectangle is : ",area)

    perimeter=(2*length)+(2*width)
    print("perimeter is:",perimeter)


if __name__=="__main__":
    main()