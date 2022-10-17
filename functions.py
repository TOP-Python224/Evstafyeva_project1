"""Дополнительный модуль: вспомогательные функции."""

# ИСПОЛЬЗОВАТЬ: из стандартной библиотеки лучше импортировать только необходимые объекты, чем модули целиком — последни могут быть весьма объёмными
from configparser import ConfigParser


# ИСПОЛЬЗОВАТЬ: в этот модуль вы импортируете модуль с глобальными переменными и далее обращаетесь к ним
import data


# вариант решения 2
def read_ini(file_name) -> dict:
    """Читает ini-файл и возвращает его содержимое в формате вложенного словаря."""
    config = ConfigParser()
    config.read(file_name)
    dictionary = {}
    for section in config.sections():
        dictionary[section] = {}
        for option in config.options(section):
            dictionary[section][option] = config.get(section, option)
    return dictionary


# СДЕЛАТЬ: изучите структуру файлов и данных в референсе, делайте по аналогии


file_name = 'players.ini'
res = read_ini(file_name)
print(f'{res}')
