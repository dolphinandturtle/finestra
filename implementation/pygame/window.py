import pygame as pg
from abstract import Window


pg.init()

class WindowPygame(Window):

    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.title = title
        self.buffer = pg.display.set_mode(self.size)
        pg.display.set_caption(self.title)
        
    def blit(self, source, position):
        self.buffer.blit(source, position)

    def update(self):
        pg.display.update()
