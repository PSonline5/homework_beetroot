# Write a decorator that prints a function with arguments passed to it.
# NOTE! It should print the function, not the result of its execution!
# For example:
#   "add called with 4, 5"


def logger(func):
    def wrapper(*args):
        return f"{func} with {args}"
    return wrapper


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

# Write a decorator that takes a list of stop words and replaces in them
# with * inside decorated function


def stop_words(words: list):
    def decorator(func):
        def wrapper(*args, **kwargs):
            x = func(*args, **kwargs)
            for word in words:
                x = x.replace(word, "*")
            return x
        return wrapper
    return decorator


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan("Steve") == "Steve drinks * in his brand new *!"

# Write a decorator arg_rules that validates arguments passed to the function
# A decorator should take 3 arguments:
#   max_length: 15
#   type_: str
#   contains: []  - list of symbols that an argument should contain
#
# If some of the rules' checks returns False, the function should return False
# and print the reason it failed
#
# Otherwise return result


def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        def wrapper(*args):
            if all(type(arg) != type_ for arg in args):
                return False
            else:
                for arg in args:
                    if len(arg) > max_length:
                        return False
                    else:
                        for cont in contains:
                            if cont not in arg:
                                return False
            return func(*args)
        return wrapper
    return decorator


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
