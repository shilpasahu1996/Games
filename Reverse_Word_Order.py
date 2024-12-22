def main():
    line = input('Enter sentence: ')
    reverse_str(line)


def reverse_str(line):
    length = len(line)

    print(length)
    for i in line:
        print(line[length-1], end ='')
        length= length-1







if __name__ == '__main__':
    main()
