import numpy as np
import numpy.linalg as linalg
import uuid


class Environment(object):
    def __init__(self, tps: int, center: np.ndarray, radius: float):
        self._tps = tps
        self.__center = center
        self.__radius = radius
        self.__env_id = str(uuid.uuid4())[:8]

    def isAccessible(self, target: np.ndarray) -> bool:
        return linalg.norm(target - self.__center) <= self.__radius or self.__radius == 0

    def get_id(self):
        return self.__env_id
