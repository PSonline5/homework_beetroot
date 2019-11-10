# Write a function is_palindrome which takes a string and returns boolean
# whether the string is a palindrome or not


def is_palindrome(word: str) -> bool:
    return word == '' or word[0] == word[-1] and is_palindrome(word[1:-1])


print(is_palindrome('test'))
print(is_palindrome('abcba'))

# Eti tri varianta nashel v google
# def is_palindrome(word):
#     if not word:
#         return True
#     else:
#         return word[0] == word[-1] and is_palindrome(word[1:-1])

# def is_palindrome(word):
#     return word[:len(word) // 2] == word[:(len(word) - 1) // 2:-1]


# def ispalindrome(word):
#     if len(word) < 2: return True
#     if word[0] != word[-1]: return False
#     return ispalindrome(word[1:-1])


# Write a function copy_string which takes a string and recursively, character
# by character creates a copy of it.


def copy_string(string: str) -> str:
    if len(string) == 0:
        open('file123.txt', 'r')
        return string
    else:
        with open('file123.txt', 'a+') as file:
            file.write(string[0])
        return copy_string(string[1:])


print(copy_string('test'))


# Write a function first_letter which takes a string and returns first
# uppercase letter in it


def first_letter(string: str) -> str:
    if string[0].isupper():
        return string[0]
    else:
        return first_letter(string[1:])


print(first_letter('hello World'))
