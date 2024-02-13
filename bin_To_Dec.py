def binToDec(bin_value):

    # converting binary to decimal
    decimal_value = 0
    count = 0

    while(bin_value != 0):
        digit = bin_value % 10
        decimal_value = decimal_value + digit * pow(2, count)
        bin_value = bin_value//10
        count += 1

    # returning the result
    return decimal_value

def main():
    binary = int(input("Enter a binary value: "))
    print("decimal of binary ", binary, " is: ", binToDec(binary))

    binary = int(input("Enter another binary value: "))
    print("decimal of binary ", binary, " is: ", binToDec(binary))

    binary = int(input("Enter another binary value: "))
    print("decimal of binary ", binary, " is: ", binToDec(binary))

# main code
if __name__ == '__main__':
    main()

    
