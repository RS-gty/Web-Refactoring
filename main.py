import numpy as np

from server import *

if __name__ == '__main__':
    H1 = Host(np.array([0, 0, 1]), 1000, 10)
    print(H1)
