def get_smallest(smallest, value):
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    return smallest

def main():
    mallest = None
    while True:
        num = input("Enter a number: ") .lower()
        if num == "done":
            break
        smallest = get_smallest(smallest, num)
        print("smallest number is:", smallest)

if __name__ == ""__main__":
    main()
