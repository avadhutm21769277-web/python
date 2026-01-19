

# problem Statement 5.2: vowel or consonant check




def main():

    print("enter a character")
    ch=(input())

    ch=ch.lower()                       #handle lowecase

    if ch in ['a','e','i','o','u']:

    
        print("it is vowel")

    else:
        print("it is consonant")


if __name__=="__main__":
    main()