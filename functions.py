"""Дополнительный модуль: вспомогательные функции."""

import configparser


# вариант решения 2
def read_ini(file_name) -> dict:
    """Читает ini-файл и возвращает его содержимое в формате вложенного словаря."""
    config = configparser.ConfigParser()
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
