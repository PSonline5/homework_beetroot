import time
# Write a context manager Logger that provides an object for logging data and
# writing it to a file.
# Logger must have log method that takes any value and writes it into a file
# A filename must be specified when calling context manager.
# You must provide a timestamp (just use time.time()) for every new line
# in file.


class Logger:
    def __init__(self, file_name):
        self.file_name = file_name

    def __enter__(self):
        print("Operation Started")
        return self

    def __repr__(self):
        return self.file_name

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.log_method(self)

    def log_method(self, value):
        with open(self.file_name, 'a+') as log:
            log.write(f"[{time.time()}]{value}\n")


with Logger('files/log3.txt') as logger:
    logger.log_method(12 + 14)
    logger.log_method('Hello World')
    logger.log_method(True)

# example:
# with Logger('log1.txt') as logger:
#     logger.write(12 + 14)
#     logger.write('Hello World')
#     logger.write(True)

# this code must create log1.txt file with the following structure:
# [timestamp] 26
# [timestamp] Hello World
# [timestamp] True
#
# where timestamp is the result of time.time() call
