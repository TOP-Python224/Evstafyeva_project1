"""Дополнительный модуль: вспомогательные функции."""

# импорт из стандартной библиотеки
from configparser import ConfigParser

# импорт дополнительных модулей
import data


def read_ini(file_name: str) -> bool:
    """Читает ini-файл и возвращает его содержимое в формате вложенного словаря."""
    config = ConfigParser()
    config.read(file_name)
    data.STATS = {}
    for player in config.sections():
        data.STATS[player] = {}
        for key, value in config[player].items():
            data.STATS[player][key] = int(value) if value.isdecimal() else value
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


def draw_board(align_right: bool = False) -> str:
    """Формирует и возвращает строку, содержащую псевдографическое изображение игрового поля со сделанными ходами."""
    for i in data.RANGE:
        print(data.BOARD[0+i*3], "|", data.BOARD[1+i*3], "|", data.BOARD[2+i*3])
        print(chr(773)*data.DIM*2)


def update_stats(score: data.Score) -> None:
    """Обновляет глобальную переменную статистики в соответствии с результатом завершённой партии."""


# тест
if __name__ == '__main__':
    file_name = 'players.ini'
    read_ini(file_name)
    print(data.STATS)
