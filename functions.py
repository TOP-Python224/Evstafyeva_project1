"""Дополнительный модуль: вспомогательные функции."""


# КОММЕНТАРИЙ: вы не должны редактировать мои комментарии: ни содержательно, ни переносы вручную расставлять — для удобства чтения пользуйтесь настройкой "мягкого" переноса строк (soft wrap)


# импорт из стандартной библиотеки
from configparser import ConfigParser
from shutil import get_terminal_size

# импорт дополнительных модулей
import data


def read_ini() -> bool:
    """Читает ini-файл и возвращает его содержимое в формате вложенного словаря."""
    config = ConfigParser()
    config.read(data.players_ini)
    for player in config.sections():
        data.STATS[player] = {}
        for key, value in config[player].items():
            data.STATS[player][key] = int(value) if value.isdecimal() else config[player].getboolean(key)
    config = ConfigParser()
    config.read(data.saves_ini)
    for players in config.sections():
        turns = {config[players].getint('dim'): [int(t) for t in config[players]['turns'].split(',')]}
        players = tuple(players.split(';'))
        data.SAVES[players] = turns
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
    # ДОБАВИТЬ: запись сохранений из словаря data.SAVES в файл saves.ini


def get_player_name() -> None:
    """Запрашивает имя игрока и проверяет присутствие этого имени в глобальной переменной статистики, добавляет имя в глобальную переменную текущих игроков."""
    Player1 = input('Введите имя первого игрока: ')
    Player2 = input('Введите имя второго игрока:  ')
    # ДОБАВИТЬ: вы должны проверить ввод пользователя, одним из условий был запрет пользователю вводи имени, начинающегося с символа '#'
    for player in data.STATS:
        # ИСПРАВИТЬ: я вас не учил так формулировать условия... пересматривайте карточки и занятия по логическим операторам
        # ИСПРАВИТЬ: в локальном пространстве имён данной функции у вас нет переменной config
        if Player1 and Player2 in config.sections():
            continue
        else:
            # УДАЛИТЬ: 1) вам нечего записывать в файл, 2) а даже если бы и было, то вы для этого только что функцию написали выше, write_ini() называется
            with open(file_name, 'w', encoding='utf-8') as f_out:
                # УДАЛИТЬ: в локальном пространстве имён данной функции у вас нет переменной players
                players.write(f_out)


def draw_board(board: data.Series, align_right: bool = False) -> str:
    """Формирует и возвращает строку, содержащую псевдографическое изображение игрового поля со сделанными ходами."""
    board = [str(c) for c in board]
    margin = ' '*(1, get_terminal_size()[0]-1)[align_right]
    cell_max_width = max(len(c) for c in board) + 2
    board_graph = ''
    for i in data.RANGE:
        row = board[i*data.DIM:(i+1)*data.DIM]
        board_graph += margin + '|'.join(cell.center(cell_max_width) for cell in row) + '\n'
    horiz_line = margin + '—'*(cell_max_width*data.DIM + data.DIM - 1)
    board_graph = board_graph.rstrip().replace('\n', f'\n{horiz_line}\n')
    return board_graph


def update_stats(score: data.Score) -> None:
    """Обновляет глобальную переменную статистики в соответствии с результатом завершённой партии."""


def change_dimension(new_dimension: int) -> None:
    """Изменяет размер игрового поля, пересчитывая релевантные глобальные переменные."""
    if new_dimension != data.DIM:
        data.DIM = new_dimension
        data.CELLS = new_dimension**2
        data.RANGE = range(new_dimension)
        data.ALL_TURNS = range(data.CELLS)
        data.BOARD = ['']*data.CELLS


# тест
if __name__ == '__main__':
    # read_ini()
    # print(data.STATS)
    # print(data.SAVES)
    change_dimension(11)
    print(draw_board(range(1, 122)))
