import numpy as np

from environment import *


class Universe(Environment):
    def __init__(self):
        super().__init__(1000, np.array([0, 0, 0]), 0)
        self.__environments: list[Environment] = []
        self.__signals = []
        self.__frame = 0

    def update(self):
        self.__frame += 1

    def receive_signal(self, signal):
        self.__signals.append(signal)

    def get_signals(self):
        return self.__signals

    def get_density(self, position: np.ndarray):
        temp = 0
        for i in self.__signals:
            temp += i.get_density(position, self.__frame)
        return temp
