import numpy as np
import uuid

from server import Server


class SubServer(Server):
    def __init__(self, position: np.ndarray):
        super().__init__(position)
        self.__server_name = str(uuid.uuid4())[24:]
        self.ids: list[str] = []

    def get(self):
        return self.__server_name
