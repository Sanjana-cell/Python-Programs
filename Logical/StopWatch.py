from time import time
class StopWatch:
    startTimer=0
    stopTimer=0
    elapsed=0

    def start(self):
        self.startTimer=int(time() * 1000)
        print("Start Time ", self.startTimer)

    def stop(self):
        self.stopTimer=int(time() * 1000)
        print("Stop Time ", self.stopTimer)

    def getElapsed(self):
        self.elapsed= self.stopTimer - self.startTimer
        return self.elapsed

class ValueNotEqualError(Exception):
    """Raised when the input value is too small"""
    pass

watch=StopWatch()
value=1
while value==1:
    try:
        userInput=(int(input("Press  1 to start Time")))
        if userInput != 1:
            raise ValueNotEqualError
        watch.start()
        print()

        userInput = (int(input("Press  2 to stop Time")))
        if userInput != 2:
            raise ValueNotEqualError
        watch.stop()
        print()

        elapsed=watch.getElapsed()
        print("Total time Elapsed(in secondes) is ",int(elapsed/1000))
        break
    except ValueNotEqualError:
        print("Enter 1 to start timer and 2 to stop timer")
