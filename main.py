import numpy as np
from matplotlib import pyplot as plt
from numpy import fft
from tqdm import tqdm

from environment.Universe import Universe
from server import *
from signal import *
from data import *
from environment import *

if __name__ == '__main__':


    H1 = Host(np.array([0, 0, 1]), tps, 10)
    Su1 = SubServer(np.array([0, 0, 2]))
    Su1.turn()

    S1 = Signal(np.array([0, 0, 0]), 100, 5.6, 100000)
    S2 = Signal(np.array([0, 0, 0]), 10, 10.6, 100000)
    S2 = Signal(np.array([0, 0, 0]), 100, 15.6, 100000)
    S2 = Signal(np.array([0, 0, 0]), 100, 20.6, 100000)
    S2 = Signal(np.array([0, 0, 0]), 100, 25.6, 100000)
    S2 = Signal(np.array([0, 0, 0]), 100, 30.6, 100000)

    amp2 = []
    dur = 50000
    for i in range(1000):

        universe.update()
    for i in tqdm(range(dur)):
        universe.update()

    amp2 = Su1.get()
    amp = fft.fft(amp2)
    A = (amp.real ** 2 + amp.imag ** 2) ** 0.5 * 2
    k = np.fft.fftfreq(5000, 1/tps)

    print(universe.get_signals())
    print(Su1.peak(10))

    plt.plot(k, A)
    plt.show()
