"""Дополнительный модуль: настройка партии."""
import data

# импорт дополнительных модулей
import data
import bot

def game_mode() -> None:
    """Запрашивает режим для новой партии, при необходимости выполняет запросы уровня сложности или имени второго игрока, выполняет запрос очерёдности ходов."""
    print("Введите имя первого игрока:")
    player1_name = input(data.PROMPT)
    data.PLAYERS.append(player1_name)
    print("С кем будете играть?\n Если с человеком, введите 'ч'. Если с ботом введите 'б'")
    opponent_name = input(data.PROMPT)
    if opponent_name == 'ч':
        print("Введите имя второго игрока:")
        player2_name = input(data.PROMPT)
        data.PLAYERS.append(player2_name)
        # print(f"{player1_name}, введите свой токен: 'X' или '0':\n")
        # player1_token = input(data.PROMPT)
        # if player1_token == 'X':
        #     data.PLAYERS[0] == data.TOKENS[0]
        # else:
        #     data.PLAYERS[1] == data.TOKENS[0]
    elif opponent_name == 'б':
        return get_bot_level()
    else:
        print("Некорректный ввод")


def get_bot_level() -> None:
    """Запрашивает уровень сложности для режима игры с ботом, добавляет имя бота в глобальную переменную текущих игроков."""
    print("Введите уровень сложности бота:\n #1 - легкий, #2 - сложный")
    bot_level = input(data.PROMPT)
    data.PLAYERS.append(bot_level)
    if bot_level == '#1':
        return bot.easy_mode()
    elif bot_level == '#2':
        return bot.hard_mode()
    else:
        print("Некорректный ввод")


def get_turn_order() -> None:
    """Запрашивает текущего активного игрока о его выборе токена для партии, при необходимости меняет порядок имён в глобальной переменной текущих игроков."""
    print(f"{data.PLAYERS[0]}, выберите свой токен: 'X' или '0':\n")
    player1_token = input(data.PROMPT)
    if player1_token == 'X':
        data.PLAYERS[0] == data.TOKENS[0]
    else:
        data.PLAYERS[0] == data.TOKENS[1]

def check_training() -> bool:
    """Проверяет является ли данная партия первой для любого из игроков."""

    # отсутствие сохранённых данных в data.SAVES означает, что партия является первой для игроков
    if data.SAVES:
        return False
    else:
        return True

# тест
if __name__ == '__main__':
    game_mode()
    get_bot_level()
    get_turn_order()
    check_training()