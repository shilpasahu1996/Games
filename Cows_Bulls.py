import random

def main():
    sys_num = random.randint(1000,9999)
    new_sys_num = str(sys_num)
    print(new_sys_num)


    user_input(new_sys_num)

def user_input(new_sys_num):
    while True:
        user_num = input('Guess the 4 digit no:')
        if user_num.lower() == "exit":  # Check if the user wants to exit
            print("Exiting the game!")
            exit()
        if user_num.isdigit() and len(user_num)==4:
            print('Your guess is', user_num)
            bulls_cow(user_num, new_sys_num)
            break
        else:
            print('Enter a 4 digit valid no!!!')

# def no_str(sys_num):
#     return list(map(int,str(sys_num)))

def bulls_cow(user_num, new_sys_num):
    bulls=0
    cows=0
    for i in range(4):
        if user_num[i]==new_sys_num[i]:
            bulls=bulls+1
        elif user_num[i] in new_sys_num:
            cows=cows+1
            print('user_num,new_sys,cows:',user_num[i],new_sys_num,cows)
    print(f'Bulls {bulls} Cows {cows}')

    if bulls==4:
        print('You have guessed all digits correctly!')
    else:
        user_input(new_sys_num)






if __name__ == '__main__':
    main()


# a=999
# b=10
# c=a/b
# print(c)

