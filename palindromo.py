import random

def palindrome(word):
    reversed_letter = "".join(reversed(word))

    if word == reversed_letter:
        return True

    return False

if __name__ == "__main__":
    inputWord = str(input("Put your word: "))
    response = palindrome(inputWord)

    if response is True:
        print("{} is a palindrome".format(inputWord))
    else:
        print("{} is not a palindrome".format(inputWord))