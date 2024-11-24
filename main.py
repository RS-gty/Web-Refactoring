import numpy as np
from matplotlib import pyplot as plt
from numpy import fft

from environment.Universe import Universe
from server import *
from signal import *
from data import *
from environment import *

if __name__ == '__main__':

    H1 = Host(np.array([0, 0, 1]), 1000, 10)
    S1 = Signal(np.array([0, 0, 0]), 100, 67, 1000, 1000)

    amp2 = []
    dur = 2000
    for i in range(dur):
        amp2.append(universe.get_density(np.array([0, 0, 1])))
        universe.update()
    amp = fft.fft(amp2)
    A = (amp.real ** 2 + amp.imag ** 2) ** 0.5 * 2 / dur
    k = np.fft.fftfreq(dur, 1/1000)

    print(universe.get_signals())

    plt.plot(k, A)
    plt.show()
