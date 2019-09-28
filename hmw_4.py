# first task
string = input()
symbol = input()
for i in string:
    if i == symbol:
        string = string.replace(symbol, '')
print(string)

# second task
names = ['John',  'Kate',  'Dave',  'Den', 'Adele']
string1 = input()
if string1 not in names:
    print('not found')
else:
    if names.index(string1) % 2 == 0:
        print("it's all good")
    else:
        string1 = names.index(string1)
        del names[string1]
        print(names)

# third task
nums = [75, 81, 96, 213, 94, 15, 38, 11]
while sum(nums) > 200:
    nums.pop()
print(nums)

# fourth task
number = int(input())


def coll_seq(n):
    print(n)
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            print(n)
        else:
            n = n * 3 + 1
            print(n)
    return n


print(coll_seq(number))
