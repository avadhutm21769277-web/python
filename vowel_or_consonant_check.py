

#   Problem Statement 5.4   : Find Largest Among Three Numbers




def main():

    print("enter three numbers by using spaces")

    numbers=list(input().split())

    print("you have entered these numbers",numbers)

    print("Largest number is",max(numbers))



if __name__=="__main__":
    main()