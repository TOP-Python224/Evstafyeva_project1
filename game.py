"""Дополнительный модуль: партия."""

# импорт дополнительных модулей
import data


def human_turn(training: bool = False) -> int:
    """Запрашивает у игрока и возвращает корректную координату ячейки поля для текущего хода."""

    human_step = int(input('Введите координату своего хода от 1 до 9: '))
    human_step = data.BOARD[human_step-1]
    return human_step

# тесты
# if __name__ == '__main__':
#     human_turn()

def bot_turn(token_index: int, training: bool = False) -> int:
    """Вычисляет и возвращает координату ячейки поля для текущего хода бота в зависимости от сложности."""




def check_win() -> bool:
    """Проверяет текущую партию на наличие победной комбинации."""

    winning_combinations = [[0, 1, 2],
                            [3, 4, 5],
                            [6, 7, 8],
                            [0, 3, 6],
                            [1, 4, 7],
                            [2, 5, 8],
                            [0, 4, 8],
                            [2, 4, 6]]
    for i in winning_combinations:
        if (data.BOARD[i[0]] == data.TOKENS[0] and
            data.BOARD[i[1]] == data.TOKENS[0] and
            data.BOARD[i[2]] == data.TOKENS[0]
            or
            data.BOARD[i[0]] == data.TOKENS[1] and
            data.BOARD[i[1]] == data.TOKENS[1] and
            data.BOARD[i[2]] == data.TOKENS[1]
        ):
            return True
        else:
            return False


def game() -> data.Score | None:
    """Управляет игровым процессом для каждой новой или загруженной партии."""


# тесты
if __name__ == '__main__':
    pass