import numpy as np


class Server(object):
    def __init__(self, position: np.ndarray):
        self.position = position
        self.__tps = 0
