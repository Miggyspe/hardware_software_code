def is_valid_number(num_str):
    return num_str.isdigit() and all(char in "0123456789" for char in num_str)

def decimal_to_binary(number):
    result = ""
    number = int(number)
    while number > 0:
        remainder = number % 2
        number = number // 2
        result = str(remainder) + result
    return result

def main():
    while True:
        num_str = input("Enter a valid number [0-9]: ")
        if is_valid_number(num_str):
            break
        else:
            print("Invalid input. Please enter a valid number [0-9].")

    num = int(num_str)
    print("Decimal {} to Binary: {}".format(num, decimal_to_binary(num)))

if __name__ == "__main__":
    main()
