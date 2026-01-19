
# Problem Statement 1.4 :    write a program which display 5 times Marvellous on screen

#     Output                      Marvellous  
#                                 Marvellous  
#                                 Marvellous  
#                                 Marvellous  
#                                 Marvellous              




def show(user_input):
    result=(5*user_input)
    return result




def main():
    print("enter the input to get result of 5 times of it")
    userinput=str(input())
    answer=show(userinput)
    
    print("your 5 times result is :",answer)






if __name__=="__main__":
    main()