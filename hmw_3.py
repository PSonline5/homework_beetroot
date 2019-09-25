# first task
string = "test1, test2, test3, test4, test5"
string = string.split(',')
number = string[int(input('Enter the number = '))-1]
string.remove(number)
string = ','.join(string)
print(string)

# first task with replace
string1 = "test1, test2, test3, test4, test5"
string1 = string1.split(',')
number = string1[int(input('Enter the number = '))-1]
string1 = ','.join(string1)
print(string1.replace(f"{number}{','}", ""))

# second task
# url = input()
url = 'https://realpython.com/courses/python-thonny/'
print(url.split('/')[2])
