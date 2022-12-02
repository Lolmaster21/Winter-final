import pygame as py
from settings import *

class Mouse:
    def __init__(self):
        self.mouse_pos = (0, 0)
        self.click = False
    def handler(self, event: list[py.event.Event]):
        if event.type == py.MOUSEMOTION:
            self.mouse_pos = py.mouse.get_pos()
        if event.type == py.MOUSEBUTTONDOWN:
            self.click = True
        if event.type == py.MOUSEBUTTONUP:
            self.click = False
