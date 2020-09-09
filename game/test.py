import pygame as game


class Plane(game.sprite.Sprite): # the base class of all the planes, include ourplane and the oppsite plane,it's means there're have to two subclass--Ourplane and Enemyplane
    img_list = []
    burndown_music = []
    active = []



    def __init__(self,screen,init_pos):
        super.__init__()
        self.screen = screen




class Our_plane(Plane):
    pass


class Enemy_plane(Plane):
    pass

class PlaneWar(game.sprite.Sprite):
    game.init()


class start_game(game.sprite.Sprite):
    pass






def main():
    PlaneWar() # load all the parts of game needs,include the begin image of bg, bg_sound, image of ourplane,and init the War as object.
    smallenemyplane() # load the parts of enemyplane, ogranize the enemypalne by group
    start_game() # real logic of the game
