# Напишите код, который запускается из командной строки и получает на вход путь до директории 
# на ПК. Соберите информацию о содержимом в виде объектов namedtuple. Каждый объект хранит:
# имя файла без расширения или название каталога,
# расширение, если это файл, флаг каталога, название родительского каталога.
# добавить логирование и argparse


import pathlib 
from collections import namedtuple
from logger import log_dec
from pars import pars_dec

DIRSUBJECT = namedtuple('DIRSUBJECT',['file_name', 'ext', 'flag', 'parent'])

@log_dec

def dir_info(path):
    path = pathlib.Path(path)
    new_list = []
    for file in path.iterdir():
        new_list.append(DIRSUBJECT(file.name, file.suffix, file.is_dir(), file.parent))

    return new_list



print(pars_dec())

print(dir_info('D:\GB\Python Auto HW\Home_work_15\python'))