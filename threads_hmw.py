import argparse
import os
import shutil
import time
from concurrent.futures import ThreadPoolExecutor

directory = 'C:/Users/Павел/PycharmProjects/testing/'

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--extension', type=str)
arg = parser.parse_args()


def transporting_files(file_name) -> None:
    date_ = time.gmtime(os.path.getmtime(f'{directory}{file_name}'))
    date_ = f'{date_.tm_mday}-{date_.tm_mon}'
    if date_ in os.listdir(directory):
        shutil.move(f'{directory}{file_name}', f'{directory}{date_}')
    else:
        os.mkdir(f'{directory}{date_}')
        shutil.move(f'{directory}{file_name}', f'{directory}{date_}')


while True:
    file_list = os.listdir(directory)
    with ThreadPoolExecutor() as executor:
        for file1 in file_list:
            if os.path.splitext(file1)[1] == arg.extension:
                executor.submit(transporting_files, file1)
