def into_msg():
    print("Hello")
    print("This is a Number conversion program")
    print("this program also converts binary to Decimal and vice versa")
    return input("press Enter to continue")
################################################################################
def mainMenu():
    print("1. Binary to Decimal")
    print("2. Decimal to Binary")
    print("3. quit program")
    while True:
        try:
            selection=int(input("Enter Choice: "))
            if selection==1:
                binToDec_assist()
                break
            elif selection==2:
                decToBin_assist()
                break
            elif selection==3:
                exit_program()
                break
            else:
                print("Invaild choice Enter 1-3")
                mainMenu()
        except ValueError:
            print("Invalid Choice. Enter 1-3")
################################################################################
def binToDec_assist():
    print("#####################################################")
    binary = int(input("Enter a binary value: "))
    print("decimal of binary ", binary, " is: ", binToDec(binary))
    mainMenu_2nd()
################################################################################
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
################################################################################
def mainMenu_2nd():
    print("#####################################################")
    print("1. Binary to Decimal")
    print("2. Decimal to Binary")
    print("3. quit program")
    while True:
        try:
            selection=int(input("Enter Choice: "))
            if selection==1:
                binToDec_assist()
                break
            elif selection==2:
                decToBin_assist()
                break
            elif selection==3:
                exit_program()
                break
            else:
                print("Invaild choice Enter 1-3")
                mainMenu()
        except ValueError:
            print("Invalid Choice. Enter 1-3")
################################################################################
# function definition
# it accepts a decimal value
# and prints the binary value
def decToBin(dec_value):
    # logic to convert decimal to binary
    # using recursion
    bin_value =''
    if dec_value > 1:
        decToBin(dec_value//2)
    print(dec_value % 2,end = '')
################################################################################
def decToBin_assist():
        # taking input as decimal
        # and, printing its binary
        print("#####################################################")
        decimal = int(input("Input a decimal number: "))
        print("Binary of the decimal ", decimal, "is: ", end ='')
        decToBin(decimal)
        mainMenu_dec()
################################################################################
def mainMenu_dec():
    print("                                                     ")
    print("#####################################################")
    print("1. Binary to Decimal")
    print("2. Decimal to Binary")
    print("3. quit program")
    while True:
        try:
            selection=int(input("Enter Choice: "))
            if selection==1:
                binToDec_assist()
                break
            elif selection==2:
                decToBin_assist()
                break
            elif selection==3:
                exit_program()
                break
            else:
                print("Invaild choice Enter 1-3")
                mainMenu()
        except ValueError:
            print("Invalid Choice. Enter 1-3")
################################################################################
def exit_program():
    print ("Good Bye!")
    return False, None
################################################################################
def main():
    into_msg()
    mainMenu()

if __name__ == '__main__':
    main()
