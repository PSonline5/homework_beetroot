# first task


def insert_whitespace(string):
    for word in string:
        if word.isupper():
            string = string.replace(word, f"{' '}{word}").strip(" ")
            string = string.replace('  ', ' ')
    return string


print(insert_whitespace("SheWalksToTheBeach"))
# second task


def calculator(num1, num2, operation):
    while operation == "+":
        return num1 + num2
    while operation == "/":
        return num1 / num2


print(calculator(5, 10, '/'))
# third task


def wrap(string, width):
    new_string = ''
    for word in string:
        if string.index(word) == width+1:
            new_string = new_string + '\n' + string[0:width]
            string = string.replace(string[0:width], '')

    return new_string + '\n' + string


print(wrap('ABCDEFGHIJKLIMNOQRSTUVWXYZ', 4))
