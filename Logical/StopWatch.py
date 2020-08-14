"""
Program for measuring the time that elapses between
the start and end clicks
"""
from time import time
class StopWatch:
    startTimer=0
    stopTimer=0
    elapsed=0

    def start(self):
        """
        function to calculating start time in milliseconds
        """
        self.startTimer=int(time() * 1000)
        print("Start Time ", self.startTimer)

    def stop(self):
        """
        function for calculating stop time in milliseconds
        """
        self.stopTimer=int(time() * 1000)
        print("Stop Time ", self.stopTimer)

    def getElapsed(self):
        """
        function to get elapsed time
        :return: returns the elapsed time
        """
        self.elapsed= self.stopTimer - self.startTimer
        return self.elapsed

class ValueNotEqualError(Exception):
    """Raised when the input value is too small"""
    pass

watch=StopWatch()
value=1
while value==1:
    try:
        userInput=(int(input("Press  1 to start Time"))) # press 1 to start time
        if userInput != 1:
            raise ValueNotEqualError
        watch.start() #function call to start times
        print()

        userInput = (int(input("Press  2 to stop Time"))) #press 2 to stop time
        if userInput != 2:
            raise ValueNotEqualError
        watch.stop() #function call to stop timer
        print()

        elapsed=watch.getElapsed() #function call to get elapsed time after stoping the timer
        print("Total time Elapsed(in secondes) is ",int(elapsed/1000)) #prints elasped time in seconds
        break
    except ValueNotEqualError:
        print("Enter 1 to start timer and 2 to stop timer")
