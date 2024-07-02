def main():
    """
    ########################################
    Code Your Program here
    ########################################
    """
    total = 0
    i = 0
    while (i < 5):
        number = int(input('Enter a number '))
        total += number
        i += 1
    print(total)

    ########################################
    # Do not delete the return statement
    ########################################
    return total


if __name__ == '__main__':
    main()
