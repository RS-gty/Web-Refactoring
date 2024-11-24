import numpy as np

from data.data import universe


class Signal(object):
    def __init__(self, center: np.ndarray, strength, frequency, duration, tps,
                 direction=None, concentrate=np.pi):
        self.__center = center
        self.__strength = strength
        self.__frequency = frequency
        self.__duration_tick = duration
        self.__dir = direction
        self.__concentrate = 0

        self.__origin_tick = 0
        self.__tps = tps

        if self.__dir is not None:
            self.__concentrate = concentrate
        else:
            if concentrate == np.pi:
                self.__concentrate = concentrate
            else:
                raise ValueError("'value:concentrate' must be set after the direction is defined")

        universe.receive_signal(self)

    def set_origin_tick(self, origin: int):
        self.__origin_tick = origin

    def get_distance(self, target: np.ndarray):
        return np.linalg.norm(self.__center - target)

    def is_accessible(self, target: np.ndarray, c_tick) -> bool:
        target_vector = target - self.__center
        if (np.linalg.norm(target_vector) >= (c_tick - self.__origin_tick) / self.__tps or
                np.linalg.norm(target_vector) <= (c_tick - self.__origin_tick - self.__duration_tick) / self.__tps):
            return False
        else:
            if self.__dir is None:
                return True
            else:
                if np.arccos(np.dot(target_vector, self.__dir) / (
                        np.linalg.norm(target_vector) * np.linalg.norm(self.__dir))) <= self.__concentrate:
                    return True
                else:
                    return False

    def get_density(self, target: np.ndarray, c_tick) -> float:
        distance = self.get_distance(target)
        if self.is_accessible(target, c_tick):
            bias = 2 * np.pi * (self.__frequency * (((c_tick - self.__origin_tick) % (self.__tps/self.__frequency)) / self.__tps))
            amp = self.__strength / (2 * np.pi * (1 - np.cos(self.__concentrate)) * distance ** 2)
            n = np.sin(2 * np.pi * distance / (1 / self.__frequency) + bias)
            return n * amp
        else:
            return 0.0
