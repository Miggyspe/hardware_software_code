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

def main():
    # taking input as decimal
    # and, printing its binary
    decimal = int(input("Input a decimal number: "))
    print("Binary of the decimal ", decimal, "is: ", end ='')
    decToBin(decimal)

# main code
if __name__ == '__main__':
    main()
