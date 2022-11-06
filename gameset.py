"""Дополнительный модуль: настройка партии."""

# импорт дополнительных модулей
import data


def game_mode() -> None:
    """Запрашивает режим для новой партии, при необходимости выполняет запросы уровня сложности или имени второго игрока, выполняет запрос очерёдности ходов."""
    print("С кем будете играть?\nЕсли с человеком, введите 'ч'. Если с ботом введите 'б'")
    opponent_name = input(data.PROMPT)
    if opponent_name == 'ч':
        print("Введите имя второго игрока:")
        player2_name = input(data.PROMPT)
        data.PLAYERS.append(player2_name)
    elif opponent_name == 'б':
        get_bot_level()
    else:
        print("Некорректный ввод")


def get_bot_level() -> None:
    """Запрашивает уровень сложности для режима игры с ботом, добавляет имя бота в глобальную переменную текущих игроков."""
    while True:
        print("Введите уровень сложности бота:\n1 - легкий, 2 - сложный")
        bot_level = input(data.PROMPT)
        if bot_level in ('1', '2'):
            bot_level = int(bot_level)
            break
        print("Введите цифру 1 или 2")
    data.PLAYERS.append(f'#{bot_level}')


def get_turn_order() -> None:
    """Запрашивает текущего активного игрока о его выборе токена для партии, при необходимости меняет порядок имён в глобальной переменной текущих игроков."""
    print(f"{data.PLAYERS[0]}, выберите свой токен: {data.TOKENS[0]!r} или {data.TOKENS[1]!r}:")
    player1_token = input(data.PROMPT)
    if player1_token == data.TOKENS[1]:
        data.PLAYERS.reverse()


def check_training() -> bool:
    """Проверяет является ли данная партия первой для любого из игроков."""


# тест
if __name__ == '__main__':
    game_mode()
    get_bot_level()
    get_turn_order()
    check_training()