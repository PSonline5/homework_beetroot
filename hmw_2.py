# first task
strings = input()
substring = len(strings)
middle = int(substring/2)
if substring < 7:
    print('Error')
else:
    print(strings[middle-1:middle+2])

# second task
sentence = input()
word = input()
print(sentence.count(word))

# third task
number = int(input())
number = str(number)
if number[::-1] == number:
    print(True)
else:
    print(False)

# fourth task
string = input()
number = string[int(input())]
print(string.replace(number, ""))

# fifth task
num1 = int(input())
num2 = int(input())
if num1 == 10 or num2 == 10 or (num1+num2) == 10:
    print(True)
else:
    print(False)
