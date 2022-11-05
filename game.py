"""Дополнительный модуль: партия."""

# импорт дополнительных модулей
import data
import bot


def human_turn(training: bool = False) -> int:
    """Запрашивает у игрока и возвращает корректную координату ячейки поля для текущего хода."""
    # ИСПРАВИТЬ: если пользователь введёт не цифровые символы, то на этом игра прервётся — вы должны предусмотреть такую ситуацию или хотя бы слушать преподавателя, когда он об этом говорит
    human_step = int(input('Введите координату своего хода от 1 до 9: '))
    # ОТВЕТИТЬ: какой вами ожидается результат данного действия?
    human_step = data.BOARD[human_step-1]
    return human_step


def bot_turn(token_index: int, training: bool = False) -> int:
    """Вычисляет и возвращает координату ячейки поля для текущего хода бота в зависимости от сложности."""
    # предположим, что в текущий момент функция не знает, который игрок является ботом
    for player in data.PLAYERS:
        if player == '#1':
            return bot.easy_mode()
        elif player == '#2':
            return bot.hard_mode()


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
    # ИСПОЛЬЗОВАТЬ: вы перебираете не индексы — а имя i используется для индексов
    for combination in winning_combinations:
        # ИСПОЛЬЗОВАТЬ: распаковку и алгебру логики
        # i, j, k = combination
        # if data.BOARD[i] == data.BOARD[j] == data.BOARD[k] != '':
        #     ...
        if (data.BOARD[combination[0]] == data.TOKENS[0] and
            data.BOARD[combination[1]] == data.TOKENS[0] and
            data.BOARD[combination[2]] == data.TOKENS[0]
            or
            data.BOARD[combination[0]] == data.TOKENS[1] and
            data.BOARD[combination[1]] == data.TOKENS[1] and
            data.BOARD[combination[2]] == data.TOKENS[1]
        ):
            return True
        else:
            return False


def game() -> data.Score | None:
    """Управляет игровым процессом для каждой новой или загруженной партии."""


# тесты
if __name__ == '__main__':
    pass