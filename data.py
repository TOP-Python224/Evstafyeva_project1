"""Дополнительный модуль: глобальные переменные и константы."""

# импорт из стандартной библиотеки
from numbers import Real
from typing import Sequence
from pathlib import Path
from sys import path


# глобальные переменные данных
STATS = {}
SAVES = {}

PLAYERS = []
TOKENS = ('X', 'O')
WEIGHT_OWN = 1.5
WEIGHT_FOE = 1

DIM = 3
CELLS = DIM**2
RANGE = range(DIM)
ALL_TURNS = range(CELLS)

TURNS = []
BOARD = ['']*CELLS

TRAINING = False


# глобальные переменные типов для аннотаций
Series = Sequence[Real | str]
Matrix = Sequence[Series]
Score = tuple[dict, dict]


# глобальные константы
APP_TITLE = "КРЕСТИКИ-НОЛИКИ"
PROMPT = ' > '

script_dir = Path(path[0])
players_ini = script_dir / 'players.ini'
saves_ini = script_dir / 'saves.ini'

COMMANDS = {
    'начать новую партию': ('game', 'партия', 'g', 'п'),
    'выйти из игры': ('quit', 'выход', 'q', 'в')
}
