"""Дополнительный модуль: вспомогательные функции."""


# КОММЕНТАРИЙ: вы не должны редактировать мои комментарии: ни содержательно, ни переносы вручную расставлять — для удобства чтения пользуйтесь настройкой "мягкого" переноса строк (soft wrap)


# импорт из стандартной библиотеки
from configparser import ConfigParser

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


def draw_board(align_right: bool = False) -> str:
    """Формирует и возвращает строку, содержащую псевдографическое изображение игрового поля со сделанными ходами."""
    # ОТВЕТИТЬ: чем возврат значения функцией отличается от вывода значения в стандартный поток?
    for i in data.RANGE:
        # ИСПРАВИТЬ: вместо числового литерала 3 используйте глобальную переменную data.DIM — она специально для этого существует
        print(data.BOARD[0+i*3], "|", data.BOARD[1+i*3], "|", data.BOARD[2+i*3])
        # КОММЕНТАРИЙ: упорядочивая код — упорядочиваете мысли; а у вас солянка какая-то: вертикальные разделители выше литералами прописываете, а здесь вычисляете, размерность поля выше тоже литералами, а здесь вспомнили про data.DIM — это признак сумбура и непонимания происходящего
        print(chr(773)*data.DIM*2)
    # ДОБАВИТЬ: основное назначение функции — не пустую сеточку выводить, кому сдалась она пустой — а сделанные ходы


def update_stats(score: data.Score) -> None:
    """Обновляет глобальную переменную статистики в соответствии с результатом завершённой партии."""


# КОММЕНТАРИЙ: сначала мы пишем все объявления всех функций — и только ниже пишем все тесты


# тест
if __name__ == '__main__':
    read_ini()
    print(data.STATS)
    print(data.SAVES)
    # draw_board()
