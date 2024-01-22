def into_msg():
    print("I can reverse a string")
    print("If you give me 'apple' I will return 'elppa'")
    print("I can even do an entire sentence and see:")
    return input("Type something and see")

def reverse_word(characters):
    reverse_string = ''
    for character in characters:
        reverse_string = character + reverse_string
    return reverse_string

def main():
    word = into_msg()
    word = reverse_word(word)
    print('Below is your string in reverse: \n{}' .format(word))

if __name__== "__main__":
    main()
