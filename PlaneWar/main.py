import pygame as game
import sys
game.init()

screen = game.display.set_mode(size=(420,320))

for event in game.event.get():
    if event.type == game.QUIT:
        sys.exit()



