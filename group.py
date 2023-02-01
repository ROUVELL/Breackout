import pygame as pg


class Group:
    def __init__(self, *items):
        self.items = [*items]

    def __len__(self):
        return len(self.items)

    def copy(self):
        return self.items[:]

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        self.items.remove(item)

    def update(self, *args, **kwargs):
        [item.update(*args, **kwargs) for item in self.items]

    def draw(self, sc: pg.Surface):
        [item.draw(sc) for item in self.items]