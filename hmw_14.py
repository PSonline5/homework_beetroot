import csv
from abc import ABC
from pandas import DataFrame
# Extend the existing @logger decorator which writes logs to a file
# called log.txt instead of console


def logger(func):
    def wrapper(*args,**kwargs):
        with open('files/log.txt', 'w') as file:
            file.write(func(*args, **kwargs))
    return wrapper


@logger
def do_nothing(string: str):
    return string


do_nothing('256')

# Write a function called new_lines that takes a file path, opens the file
# and adds a newline character (\n) once in 20 symbols

text = "Hello World to all"
text2 = "Good bye to all"

with open('files/log1.txt', 'w') as file:
    for _ in range(5):
        file.write(text)
        file.write('\n')
        file.write(text2)
        file.write('\n')
print("File made")


def new_lines(path: str):
    with open(path, 'r') as file1:
        file_read = file1.read()
        with open(path, 'w') as file2:
            new_text = ''
            print(file1.read())
            for index, ch in enumerate(file_read, start=1):
                if index % 20 == 0:
                    new_text += '\n'
                else:
                    new_text += ch
            file2.write(new_text)

    return "Operation completed"


print(new_lines('files/log1.txt'))

# Add a new method to our Worker-Boss program to the Boss class.
# This method is called (dump_workers). It must take all workers from
# workers list and output them into a .csv file (just the way we did it)
#
# Extra point for doing it using built-in csv library
# Extra point for doing it using 3rd party library pandas


class Person(ABC):
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company


class Boss(Person):
    def __init__(self, id_: int, name: str, company: str):
        super().__init__(id_, name, company)
        self.workers = []

    def add_worker(self, worker):
        if isinstance(worker, Worker):
            self.workers.append(worker)
        else:
            print("You can't add it to workers list")

    def remove_worker(self, worker):
        self.workers.remove(worker)

    @staticmethod
    def dump_workers():
        with open('files/workers.csv', 'w') as file:
            file.write('id_,name,company,boss_id\n')
            for index, worker in enumerate(workers):
                file.write(f"{workers[index].id},{workers[index].name},"
                           f"{workers[index].company},"
                           f"{workers[index]._boss.id}\n")


    def __repr__(self):
        return f"{self.name} the boss"


class Worker(Person):
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        super().__init__(id_, name, company)
        self._boss = boss
        self._boss.workers.append(self)

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, value):
        if isinstance(value, Worker):
            self._boss.workers.remove(self)
            self._boss.workers.append(self)
        else:
            print('He is not a Boss')

    def __repr__(self):
        return f"{self.name} the worker"


bosses = []
workers = []

with open('files/bosses.csv', 'r') as file:
    for boss in file.readlines()[1:]:
        id_, name, company = boss.split(',')
        bosses.append(Boss(id_, name, company))


with open('files/workers.csv', 'r') as file1:
    for worker in file1.readlines()[1:]:
        id_, name, company, boss_id = worker.split(',')
        workers.append(Worker(id_, name, company, bosses[int(boss_id)]))


bosses[0].dump_workers()

# Version 2

file1 = 'files/workers2.csv'

workers_list = [workers[index].__dict__ for index, dict_ in enumerate(workers)]

with open(file1, 'w', newline='') as file:
    columns = ['id', 'name', 'company', '_boss']
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    writer.writerows(workers_list)

with open(file1, 'r', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['id'], row['name'], row['company'], row['_boss'], sep=',')


# Version 3

file2 = 'files/workers3.csv'

df = DataFrame(workers_list, columns=['id', 'name', 'company', '_boss'])

print(df)


