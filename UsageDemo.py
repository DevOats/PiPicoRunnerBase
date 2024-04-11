################################################################################################
# Copyright (c) 2024 DevOats
# The MIT License
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
################################################################################################

from PiPicoRunnerBase import piPicoRunnerBase
import machine

#
# Simple reference example on how to use the piPicoRunnerBase
#
class UsageDemo(piPicoRunnerBase):


    # Constructor
    def __init__(self):
        super().__init__()                       # Mandatory base class constructor call to get the base class to work
        # Put your own constructor stuff here


    # Overrides the base class method to do initializations
    def beforeRun(self):
        print("Runnning")
        self.runSlowTickOnSecondCore = False     # Keeps the slow timer running on the first CPU core. This prevents issues with communication with Thonny
        self.slowTickFrequency = 1               # Sets the Slow tick timer frequency
        self.fastTickFrequency = 8               # Sets the Fast tick timer frequency


    # Gets called by the base class to run on the fast tick frequency intervals.
    # e.g. run communication or button press logic
    def fastTick(self):
        print("Fast!!")  


    # Gets called by the base class to run on the slow tick frequency intervals
    # e.g. run display logic
    def slowTick(self):
        print("Sloooooooooooow")


# Application runs from here
if __name__ == '__main__':
    runner = UsageDemo()
    runner.run()             # Note that the call to run() does not return, thus the script does not end.
