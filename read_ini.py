import configparser

# вариант решения 1

def read_ini (file_name) -> dict:
    """Читает ini-файл и возвращает его содержимое в формате вложенного словаря."""

    config = configparser.ConfigParser()
    config.read(file_name)
    new_format = config.__dict__['_sections'].copy()
    return new_format

file_name='players.ini'
res = read_ini(file_name)
print(f'{res}')

# вариант решения 2

def read_ini (file_name) -> dict:
    """Читает ini-файл и возвращает его содержимое в формате вложенного словаря."""

    config = configparser.ConfigParser()
    config.read(file_name)
    dictionary = {}
    for section in config.sections():
        dictionary[section] = {}
        for option in config.options(section):
            dictionary[section][option] = config.get(section, option)
    return dictionary

file_name = 'players.ini'
res = read_ini(file_name)
print(f'{res}')

