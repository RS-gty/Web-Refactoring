import numpy as np
from numpy import fft

from data import universe


class Server(object):
    def __init__(self, position: np.ndarray):
        self.position = position
        self.__tps = universe.get_tps()
        self._frame = 0
        self._receiving = False
        self._info_density = []
        self._info_max = 5000

        self._frequency = []

    def update(self, frame: int):
        self._frame = frame

    def turn(self):
        self._receiving = not self._receiving

    def resolve(self):
        amp = fft.fft(self._info_density)
        A = (amp.real ** 2 + amp.imag ** 2) ** 0.5 * 2
        self._frequency = A

    def peak(self, avr):
        self.resolve()
        temp = []
        pot = []
        res = []
        k = np.fft.fftfreq(self._info_max, 1 / self.__tps)
        for i in range(self._info_max - 2):
            if self._frequency[i] <= self._frequency[i + 1] >= self._frequency[i + 2] and self._frequency[i + 1] > 1:
                temp.append(i + 1)
        for j in range(len(temp)):
            pot.append(self._frequency[temp[j]])
        for t in temp:
            if self._frequency[t] > avr:
                res.append(k[t])
        return res
