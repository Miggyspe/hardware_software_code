def intro_msg():
    print("I can reverse a string")
    print("If you give me 'apple' I will return 'elppa'")
    print("I can even do an entire sentence")
    return input("Type something and see (type 'quit' or 'done' to exit): ")

def reverse_word(characters):
    reverse_string = ''
    index = len(characters) - 1
    while index >= 0:
        reverse_string += characters[index]
        index -= 1
    return reverse_string

def main():
    while True:
        word = intro_msg()
        if word.lower() == 'quit' or word.lower() == 'done':
            break
        word = reverse_word(word)
        print('Below is your string in reverse:\n{}'.format(word))

if __name__ == "__main__":
    main()
