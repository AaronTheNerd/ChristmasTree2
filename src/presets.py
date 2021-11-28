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


class SpinningRainbowPreset(Preset):
    def __init__(self, hold_ms=0):
        self.hold_ms = hold_ms
    def get_animation(self):
        anim = Animation()
        strips = [[0, 17],
                  [1, 16],
                  [2, 15, 18, 31],
                  [3, 14, 19, 30],
                  [4, 13, 20, 29, 32, 41],
                  [5, 12, 21, 28, 33, 40],
                  [6, 11, 22, 27, 34, 39, 42, 47],
                  [7, 10, 23, 26, 35, 38, 43, 46],
                  [8, 9, 24, 25, 36, 37, 44, 45, 48, 49]]
        color_index = {color.Color(252, 32, 3): [7, 8, 19],
                       color.Color(252, 136, 3): [5, 6, 17, 18],
                       color.Color(252, 235, 3): [3, 4, 15, 16],
                       color.Color(65, 252, 3): [1, 2, 13, 14],
                       color.Color(3, 90, 252): [0, 11, 12],
                       color.Color(82, 2, 252): [9, 10]}
        for i in range(10):
            anim.frames.append({})
            for color_key, indicies in color_index.items():
                for index in indicies:
                    if index >= 0 and index < 9:
                        for light in strips[index]:
                            anim.frames[-1][light] = color_key
                for j in range(len(indicies)):
                    indicies[j] -= 1
        return anim