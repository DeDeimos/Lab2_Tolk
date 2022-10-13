from abc import ABC
from abc import abstractmethod


class Color:
    _color = None

    # def get_color(self):
    #     return self._color
    #
    # def set_color(self, val):
    #     self._color = val

    # color = property(get_color, set_color)

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, val):
        self._color = val
