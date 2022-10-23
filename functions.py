"""Дополнительный модуль: вспомогательные функции."""

# ИСПОЛЬЗОВАТЬ: из стандартной библиотеки лучше импортировать
# только необходимые объекты, чем модули целиком — последни могут быть весьма объёмными

from configparser import ConfigParser


# ИСПОЛЬЗОВАТЬ: в этот модуль вы импортируете модуль с глобальными переменными и далее обращаетесь к ним
import data

def read_ini(file_name: str) -> bool:
    """Читает ini-файл и возвращает его содержимое в формате вложенного словаря."""
    config = ConfigParser()
    config.read(file_name)
    # необходимо использовать глобальную переменную из модуля data
    data.STATS = {}
    for player in config.sections():
        # используйте data.STATS
        data.STATS[player] = {}
        for key, value in config[player].items():
            # ИСПОЛЬЗОВАТЬ: когда значениями словаря являются числа, считывать их необходимо как числа
            data.STATS[player][key] = int(value) if value.isdecimal() else value
    # УДАЛИТЬ: поскольку вы изменяете глобальную переменную, то возвращать что-либо не требуется
    # отсутствие сохранённых ранее имён игроков трактуем как первый запуск приложения
    if data.STATS:
        return False
    else:
        return True

def write_ini(file_name: str):
    """Записывает конфигурационные файлы из глобальных переменных статистики и сохранений."""

    players = ConfigParser()
    for player in data.STATS:
        players[player] = data.STATS[player]
    with open(file_name, 'w', encoding='utf-8') as f_out:
        players.write(f_out)

# ИСПОЛЬЗОВАТЬ: все тесты и всю отладку убираем под проверку импорта
if __name__ == '__main__':
    file_name = 'players.ini'
    read_ini(file_name)
    print(data.STATS)



def get_player_name() -> None:
    """Запрашивает имя игрока и проверяет присутствие этого имени в глобальной переменной статистики, добавляет имя в глобальную переменную текущих игроков."""

    Player1 = input('Введите имя первого игрока: ')
    Player2 = input('Введите имя второго игрока:  ')
    for player in data.STATS:
        if Player1 and Player2 in config.sections():
            continue
        else:
            with open(file_name, 'w', encoding='utf-8') as f_out:
                players.write(f_out)

# тест
# if __name__ == '__main__':
#     get_player_name()

def draw_board(align_right: bool = False) -> str:
    """Формирует и возвращает строку, содержащую псевдографическое изображение игрового поля со сделанными ходами."""

    # print(data.BOARD[0], end=' |')
    # print(data.BOARD[1], end=' |')
    # print(data.BOARD[2], end='\n')
    # print(chr (773)*data.DIM*2)
    #
    # print(data.BOARD[3], end=' |')
    # print(data.BOARD[4], end=' |')
    # print(data.BOARD[5], end='\n')
    # print(chr (773)*data.DIM*2)
    #
    # print(data.BOARD[6], end=' |')
    # print(data.BOARD[7], end=' |')
    # print(data.BOARD[8], end='\n')
    # print(chr (773)*data.DIM*2)
    for i in data.RANGE:
        print (data.BOARD[0 + i * 3], "|", data.BOARD[1 + i * 3], "|", data.BOARD[2 + i * 3])
        print(chr (773)*data.DIM*2)

# тест
if __name__ == '__main__':
    draw_board()

def update_stats(score: data.Score) -> None:
    """Обновляет глобальную переменную статистики в соответствии с результатом завершённой партии."""





