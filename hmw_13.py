from functools import wraps
# Write a class TypeDecorators which has several methods for converting
# results of functions to a specified type (if it's possible):
# methods:
#   - to_int
#   - to_str
#   - to_bool
#   - to_float
#
# Don't forget to use @wraps


class TypeDecorators:
    @staticmethod
    def to_int(func):
        @wraps(func)
        def wrapper(*args):
            return int(func(*args))
        return wrapper

    @staticmethod
    def to_str(func):
        @wraps(func)
        def wrapper(*args):
            return str(func(*args))
        return wrapper

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def wrapper(*args):
            return bool(func(*args))
        return wrapper

    @staticmethod
    def to_float(func):
        @wraps(func)
        def wrapper(*args):
            return float(func(*args))
        return wrapper


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


assert do_nothing('25') == 25
assert do_something('True') is True


# Implement 2 classes, the first one is Boss and the second one is Worker
# Worker has a property 'boss' which value must be an instance of Boss
# You can reassign this value, but you should check whether the new value
# is Boss. Each Boss has a list of his own workers. You should implement
# a method which allows you to add workers to a Boss. You're not allowed
# to add instances of Boss class to workers list!
# You can refactor the existing code.
#
# id_ - is just a random unique integer


class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = set()

    def add_worker(self, worker):
        if isinstance(worker, Worker):
            self.workers.add(worker)
        else:
            print("You can't add it to workers list")

    def remove_worker(self, worker):
        self.workers.remove(worker)


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id_ = id_
        self.name = name
        self.company = company
        self._boss = boss
        boss.add_worker(self)

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, value):
        if not isinstance(value, Worker):
            self._boss.remove_worker(self)
            value.add_worker(self)
        else:
            print('He is not a Boss')
