import pyxel as px
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import NamedTuple, Tuple
from itertools import product

class Direction(Enum):
    LEFT = auto()
    RIGHT = auto()



class Ship(NamedTuple):
    x: float
    y: float

    def move(self, direction: Direction, distance: float):
        x = self.x
        if direction == direction.RIGHT:
            x += distance
        elif direction == direction.LEFT:
            x -= distance
        return Ship(x=x, y=self.y)


class Player(Ship):
    pass


class Invader(Ship):
    pass



@dataclass
class Game:
    player: Player = field(default_factory=lambda: Ship(x=0.1, y=0.1))
    invaders: Tuple[Invader] = field(default_factory=lambda: tuple(Invader(x=x, y=y) for x, y in product(list(x / 11. + 0.02 for x in range(11)), [0.6, 0.7, 0.8, 0.9])))
    invader_direction: Direction = field(default=Direction.RIGHT)

    def move_player(self, direction: str, distance: float):
        directions = {'right': Direction.RIGHT, 'left': Direction.LEFT}
        player = self.player.move(direction=directions[direction.lower()], distance=distance)
        if 0 <= player.x <= 1.:
            self.player = player

    @property
    def player_pos(self):
        return self.player.x, self.player.y

    @property
    def invader_pos(self):
        return tuple((ship.x, ship.y) for ship in self.invaders)

    def move_army(self):
        distance = 0.01
        invaders = tuple(ship.move(direction=self.invader_direction, distance=distance) for ship in self.invaders)
        print(min(ship.x for ship in invaders))
        if not all(0. <= ship.x <= 1. for ship in invaders):
            self._step_army_closer()
            self._reverse_army_direction()
        else:
            self.invaders = invaders

    def _step_army_closer(self):
        distance = 0.05
        invaders = tuple(Invader(x=ship.x, y=ship.y - distance) for ship in self.invaders)
        self.invaders = invaders

    def _reverse_army_direction(self):
        self.invader_direction = Direction.LEFT if self.invader_direction == Direction.RIGHT else Direction.RIGHT

    def shoot(self):
        passj


class App:

    def __init__(self, game: Game, width=50, height=70):
        self.game = game
        self.width = width
        self.height = height

        px.init(width=width, height=height, fps=10)

    def _draw(self):
        px.cls(0)
        x, y = self.game.player_pos
        px.pix(x=int(x * self.width), y=self.height - int(y * self.height), col=1)
        for x, y in self.game.invader_pos:
            px.pix(x=int(x * self.width), y=self.height - int(y * self.height), col=2)


    def _update(self):
        if px.btn(px.KEY_RIGHT):
            self.game.move_player(direction='right', distance=.01)

        if px.btn(px.KEY_LEFT):
            self.game.move_player(direction='left', distance=.01)

        self.game.move_army()

    def run(self):
        px.run(draw=self._draw, update=self._update)



if __name__ == '__main__':
    game = Game()
    app = App(game=game)
    app.run()