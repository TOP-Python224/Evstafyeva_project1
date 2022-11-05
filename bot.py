"""Дополнительный модуль: искусственный интеллект."""

# импорт из стандартной библиотеки
from random import choice

# импорт дополнительных модулей
import data


def easy_mode() -> int:
    """Возвращает номер случайной свободной клетки игрового поля."""
    # возвращает индекс из диапазона 0...8
    return choice(tuple(set(data.ALL_TURNS) - set(data.TURNS)))


def hard_mode() -> int:
    """Вычисляет наиболее выигрышный ход и возвращает номер клетки для этого хода."""


# тесты
if __name__ == '__main__':

    data.PLAYERS = ['#1', 'Natalia']
    data.BOARD = ['']*data.DIM**2
    data.TURNS = [5, 8, 3]
    print(f'{easy_mode() = }')