"""Дополнительный модуль: искусственный интеллект."""

# импорт из стандартной библиотеки
from random import choice

# импорт дополнительных модулей
import data


def easy_mode() -> int:
    """Возвращает номер случайной свободной клетки игрового поля."""
    # Определяем, каким токеном играет бот. Имя бота легкого уровня: '#1'. Если имя бота стоит первым в списке игроков data.PLAYERS, значит он ходит "крестиками".
    bot_token_index = data.PLAYERS.index('#1')
    # Проверяем, является ли ячейка свободной.
    for i in range(len(data.BOARD)):
        if data.BOARD[i] == ' ':
            data.BOARD[i] == bot_token_index
            # Бот легкого уровня делает ход случайным образом.
            bot_step = choice(data.BOARD[i])
            # Возвращаем номер случайной свободной клетки (i + 1), обновляем список TURNS
            cell_number = data.TURNS.append(bot_step+1)
            return cell_number
            # возвращает None вместо int, что делаю не так?


def hard_mode() -> int:
    """Вычисляет наиболее выигрышный ход и возвращает номер клетки для этого хода."""


# тесты
if __name__ == '__main__':

    data.PLAYERS = ['#1', 'Natalia']
    data.BOARD = ['']*data.DIM**2
    data.TURNS = [5, 8, 3]
    print(f'{easy_mode() = }')