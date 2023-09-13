import numpy as np

class Clock(object):

    def __init__(self, numballs=None):
        self.line_1 = []  # track 1, 1 ball represents 1 minute, up to 4 minutes
        self.line_5 = []  # track 2, 1 ball represents 5 minutes, up to 55 minutes
        self.line_60 = []  # track 3, 1 ball represents 60 minutes, up to 12 hours
        self.balls = np.arange(numballs).tolist()
        # create instance of NumPy with evenly spaced values
        # starting from 0 and ending at numballs - 1
        # then tolist() converts the NumPy array to a list
        self.fullCycles = 0
