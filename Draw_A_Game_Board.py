def main():
    r = int(input('what row size game board they want to draw:'))
    c = int(input('What column size game board they want to draw:'))


    pattern(r,c)

def pattern(r,c):
    box_len = ' ---'
    box_breadth = '|   '
    for i in range(c):
        print(box_len, end='')
    print('\n', end='')

    for k in range(r):

        for j in range(c+1):
            print(box_breadth, end='')
        print('\n', end='')
        for i in range(c):
            print(box_len, end='')
        print('\n',end='')



        # for j in range(r):
        #     print(box_breadth)


if __name__ == '__main__':
    main()


# **
# **
# **