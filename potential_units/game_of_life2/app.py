from typing import *
from itertools import product
from random import random
import pyxel as px


Cell = NewType("Cell", Tuple[int, int])
Board = NewType("Board", Dict[Cell, bool])

def get_neighbors(cell: Cell) -> Iterable[Cell]:
    x, y = cell
    for cell in product([x-1, x, x+1], [y-1, y, y+1]):
        if cell != (x, y):
            yield cell


def should_live(cell: Cell, board: Board) -> bool:
    n_live_neighbors = 0
    for n in get_neighbors(cell):
        try:
            is_alive = board[n]
        except KeyError:
            is_alive = random() <= 0.3
        n_live_neighbors += is_alive
    if board[cell]:
        return True if 1 < n_live_neighbors < 4 else False
    else:
        return True if n_live_neighbors == 3 else False


def init_board(p_alive: float = 0.3, width: int = 100, height: int = 100) -> Board:
    board: Board = {}
    for cell in product(list(range(width)), list(range(height))):
        cell: Cell = cell
        board[cell] = random() <= p_alive
    return board


def step_game(board: Board) -> Board:
    return {cell: should_live(cell=cell, board=board) for cell in board}


BoardView = NewType("BoardView", List[List[bool]])
def view_board(board: Board) -> BoardView:
    width, height = max(board)
    return [[board[(x, y)] for x in range(width)] for y in range(height)]



class Game:
    def __init__(self, width=50, height=50, p_alive=0.3):
        self.width = width
        self.height = height
        self.board = init_board(p_alive=p_alive, width=width, height=height)
        px.init(width=width, height=height, caption="Conway's Game of Life")

    def update(self):
        self.board = step_game(board=self.board)

    def draw(self):
        px.cls(0)
        board_view = view_board(board=self.board)
        for x, row in enumerate(board_view):
            for y, is_alive in enumerate(row):
                px.pix(x=x, y=y, col=7 if is_alive else 0)

    def run(self):
        px.run(update=self.update, draw=self.draw)

game = Game(width=100, height=100)
game.run()