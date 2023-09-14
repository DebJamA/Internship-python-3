import numpy as np


class Clock:

    def __init__(self, numballs=None):  # constructor method to create instance of class Clock
        self.line_1 = []  # minute track, 1 ball represents 1 minute, up to 4 minutes
        self.line_5 = []  # increment track, 1 ball represents 5 minutes, up to 55 minutes
        self.line_60 = []  # hour track, 1 ball represents 60 minutes or 1 hour, up to 12 hours
        self.balls = np.arange(numballs).tolist()
        # create instance of NumPy with evenly spaced values
        # starting from 0 and ending at [numballs - 1]
        # then tolist() converts the NumPy array to a list
        self.fullCycles = 0

    def tick(self):  # clock simulation
        self.line_1.append(self.balls.pop(0))  # removes and returns first list item, 1st ball in queue to line_1
        if len(self.line_1) == 5:  # 5th ball is 5 minutes, must move to line_5, other balls reset to queue
            self.line_5.append(self.line_1.pop(-1))  # removes and returns last list item, line_1 5th ball to line_5
            for i in range(4):  # index 0, 1, 2, 3 represents balls or minutes 1, 2, 3, 4
                self.balls.append(self.line_1.pop(-1))  # appends line_1 up to 4 balls
            if len(self.line_5) == 12:  # 12th ball is 60 minutes, must move to line_60, other balls reset to queue
                self.line_60.append(self.line_5.pop(-1))  # removes and returns last ball, line_5 12th ball to line_60
                for i in range(11):  # index 0 to 11 represents balls or minutes 5 to 55
                    self.balls.append(self.line_5.pop(-1))  # appends line_5 up to 11 balls
                if len(self.line_60) == 12:  # 12th ball is 12 hours, last ball before reset of line_60 and clock
                    lastball = self.line_60.pop(-1)  # last ball of clock cycle
                    for i in range(11):  # index 0 to 10 represents 1 to 11 hours
                        self.balls.append(self.line_60.pop(-1))  # appends line_60 up to 12 balls
                    self.balls.append(lastball)  # the next ball becomes hour 1, clock resets, 12 balls reset to queue
                    self.fullCycles += 1  # 1 is added to number or count of full cycles
                    return True  # full cycle completed at 12:00, add 1 to fullCycles variable
        return False  # full cycle not complete, do not add to fullCycles variable

    def check_balls_sequence(self):  # checking the sequence of balls in the clock
        for i in range(len(self.balls)):
            if self.balls[i] != i:
                return False
        return True

    def cycles_to_time(cycles):  # elapsed time since clock was initialized and set into motion
        days = int(cycles / 2)  # a day is 24 hours but cycle is only 12 hours so divide number of cycles by 2
        # is_half_day is False
        # is_half_day is True if cycles % 2 != 0
        is_half_day = cycles % 2 != 0
        return str(days) + " days " + ("and 12 hours" if is_half_day else "")
        # if is_half_day is True return "number days and 12 hours"
        # if is_half_day is False only return "number days"

    def simulate(self):
        inprogress = True
        while inprogress:
            if self.tick():
                if self.check_balls_sequence():
                    inprogress = False
        return self.fullCycles
