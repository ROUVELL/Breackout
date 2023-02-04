import pygame as pg


class Group:
    def __init__(self, *items):
        self._items = [*items]

    def __len__(self):
        return len(self._items)

    @property
    def is_empty(self): return not len(self._items)

    @property
    def last(self):
        if not self.is_empty: return self._items[-1]

    def clear(self):
        self._items.clear()

    def copy(self):
        return self._items[:]

    def add(self, *items):
        [self._items.append(item) for item in items]

    def remove(self, item):
        self._items.remove(item)

    def update(self, *args, **kwargs):
        [item.update(*args, **kwargs) for item in self._items]

    def draw(self, sc: pg.Surface):
        [item.draw(sc) for item in self._items]