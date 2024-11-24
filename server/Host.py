import numpy as np
import uuid

from server import Server
from environment import *


class Host(Server):
    def __init__(self, position: np.ndarray, tps: int, radius: int):
        super().__init__(position)
        self.__host_name = str(uuid.uuid4())[13: 18]
        self.__server_ids: list[str] = []
        self.__environment: Environment = Environment(tps=tps, center=position, radius=radius)
        self.__env_id = self.__environment.get_id()

    def isAccessible(self, target: np.ndarray) -> bool:
        return self.__environment.isAccessible(target)

    def get_subserver_id(self):
        sub_id = self.__env_id + self.__host_name
        return sub_id

    def get_tps(self):
        return self.__tps

    def message_handler(self, message):
        pass
