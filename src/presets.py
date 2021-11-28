from abc import ABCMeta, abstractmethod

import color
from animation import Animation


class Preset:
    __metaclass__ = ABCMeta
    HOLD_MAX = (1 << 16) - 1
    @abstractmethod
    def get_animation(self):
        pass


class SolidColorPreset(Preset):
    def __init__(self, color=color.WHITE):
        self.color = color
    def get_animation(self):
        return Animation([{ i : self.color for i in range(50) }], Preset.HOLD_MAX)


class SolidTwoColorPreset(Preset):
    def __init__(self, color1=color.WHITE, color2=color.BLACK):
        self.color1 = color1
        self.color2 = color2
    def get_animation(self):
        return Animation([{i : self.color1 if i % 2 == 0 else self.color2 for i in range(50)}],
                Preset.HOLD_MAX)

class TwoColorAlternatingPreset(Preset):
    def __init__(self, color1=color.WHITE, color2=color.BLACK, hold_ms=0):
        self.color1 = color1
        self.color2 = color2
        self.hold_ms = hold_ms
    def get_animation(self):
        return Animation([ { i : self.color1 if i % 2 == j else self.color2 for i in range(50) }
                for j in range(2) ],
                self.hold_ms)

                