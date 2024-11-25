from typing import override

import numpy as np
import uuid

from data import universe
from server import Server


class SubServer(Server):
    def __init__(self, position: np.ndarray):
        super().__init__(position)
        self.__server_name = str(uuid.uuid4())[24:]
        self.ids: list[str] = []

        universe.receive_subserver(self)

    def get(self):
        return self._info_density

    @override
    def update(self, frame: int):
        self._frame = frame
        if self._receiving:
            self._info_density.append(universe.get_density(self.position))
            if len(self._info_density) <= self._info_max:
                pass
            else:
                self._info_density = self._info_density[1:]
