class DictStack:
    def __init__(self, maxsize=10):
        self.__dicts = {}
        self.maxsize = maxsize

    def __repr__(self):
        return repr(self.__dicts)

    def push(self, item):
        self.__dicts.update(item)

    def pop(self):
        self.__dicts.popitem()

    def reverse(self):
        new_dicts = {}
        for i in sorted(self.__dicts, reverse=True):
            new_dicts[i] = self.__dicts[i]
        return new_dicts

    def reverse_in_place(self):
        self.__dicts = self.reverse()

    def index(self, item):
        for index, value in self.__dicts.items():
            if value == item:
                return index

    def last_index(self, item):
        new_item = []
        for index, value in self.__dicts.items():
            if value == item:
                new_item.append({index: value})
        return new_item[-1]

    def join(self, joiner):
        new_string = ''
        for index, value in enumerate(self.__dicts):
            if index != 0:
                new_string += f'{joiner} {value}: {self.__dicts[value]}'
            else:
                new_string += f'{value}: {self.__dicts[value]}'
        return new_string

    def sum(self):
        result = 0
        for item in self.__dicts.values():
            if not isinstance(item, int):
                raise TypeError("It is not int")
            result += item
        return result

    def enqueue(self, item):
        if self.is_full:
            self.__dicts.popitem()
            self.__dicts.update(item)
        else:
            self.__dicts.update(item)

    def dequeue(self, item):
        del self.__dicts[item]

    def size(self):
        return len(self.__dicts)

    def is_full(self):
        return len(self.__dicts) == self.maxsize

    @property
    def is_empty(self):
        return not bool(len(self.__dicts))
