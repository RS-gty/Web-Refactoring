import numpy as np

from environment import *


class Universe(Environment):
    def __init__(self):
        super().__init__(1000, np.array([0, 0, 0]), 0)
        self.__environments: list[Environment] = []
        self.__signals = []
        self.__hosts = []
        self.__subservers = []
        self.__frame = 0

    def update(self):
        self.__frame += 1
        for host in self.__hosts:
            host.update(self.__frame)
        for subserver in self.__subservers:
            subserver.update(self.__frame)

    def receive_signal(self, signal):
        self.__signals.append(signal)

    def receive_host(self, host):
        self.__hosts.append(host)

    def receive_subserver(self, subserver):
        self.__subservers.append(subserver)

    def get_signals(self):
        return self.__signals

    def get_tps(self):
        return self._tps

    def get_density(self, position: np.ndarray):
        temp = 0
        for i in self.__signals:
            temp += i.get_density(position, self.__frame)
        return temp
