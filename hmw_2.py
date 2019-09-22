# first task
strings = input()
substring = len(strings)
middle = int(substring/2)
if len(strings) < 7:
    print('Error')
else:
    print(strings[middle-1:middle+2])
