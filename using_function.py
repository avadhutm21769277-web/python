
#       Problem Statement  :  write a program which accept number from user and print thet number in '*'
#                               input : 5            outpot : * *   *   *   *



def print_star(number):
    result=0
    result=('*'*number)
    return result



def main():
    print("enter the number")
    num=int(input())
    answer=print_star(num)
    print("here is your output",answer)








if __name__=="__main__":
    main()