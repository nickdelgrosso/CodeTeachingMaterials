from random import randrange
import pyxel as px
from collections import deque
from time import time
import sys

start_pos = (1, 1)
board_size = (15, 15)


snake = deque([start_pos], maxlen=1)
direction = (1, 0)
last_time = 0
speed = 3


def gen_food(board_size, snake):
    random_food = lambda:  tuple(randrange(coord) for coord in board_size)
    food = random_food()
    while food in snake:
        food = random_food()
    return food

food = gen_food(board_size, snake)



def update():
    # Get keyboard input to steer snake
    global direction
    if px.btn(px.KEY_UP):
        direction = (0, 1)
    elif px.btn(px.KEY_DOWN):
        direction = (0, -1)
    elif px.btn(px.KEY_RIGHT):
        direction = (1, 0)
    elif px.btn(px.KEY_LEFT):
        direction = (-1, 0)

    global snake
    global speed
    current_time = time()
    global last_time
    if current_time - last_time > 1 / speed:
        snake.appendleft(tuple(x + dx for x, dx in zip(snake[0], direction)))  # Move snake
        last_time = current_time
        speed += 0.1

    global food

    if snake[0] == food:
        snake = deque(snake, maxlen=snake.maxlen + 1)
        food = gen_food(board_size, snake)

    x, y = snake[0]
    if not (0 <= x < board_size[0]) or not (0 <= y < board_size[1]):
        px.quit()

    if len(set(snake)) != len(snake):
        px.quit()

def draw():
    px.cls(0)
    for x, y in snake:
        px.pix(x=x, y=board_size[1] - y - 1, col=3)
    px.pix(x=food[0], y=board_size[1] - food[1] - 1, col=4)


px.init(*board_size)
px.run(update=update, draw=draw)

