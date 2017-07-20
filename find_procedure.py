import glob
import os.path
from pprint import pprint

migrations = 'Migrations'
files = glob.glob(os.path.join(migrations, "*.sql"))

def search():

    while True:
        filter_list = list()
        user_input = input('Введите запрос\n')
        for file in files:
            with open(file) as f:
                line = f.read()
                if user_input in line:
                    filter_list.append(file)

        pprint(filter_list)
        print('Всего найдено', len(filter_list), 'файлов')

search()