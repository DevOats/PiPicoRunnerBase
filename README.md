# PiPicoRunnerBase
### Author: Joost/DevOats

## Description
PiPicoRunnerBase is a simple Base class to easily start with your micropython projects. It provides configurable fast and a slow periodical Ticks. Both Ticks are separately protected against multiple execution and are only called if the previous call has finished executing. </br>
The SlowTick can be configured to run on the second CPU core (see Notes below)

## Usage
1. Make a Python class
2. Inherit from the **piPicoRunnerBase** class
3. Call the super constructor from your constructor
4. Override the following methods:
     - **fastTick(self)**   (optional)
     - **slowTick(self)**   (optional)
     - **beforeRun(self)**  (optional)
5. In the beforeRun override, set the following configuration variables: (optional)
      - **self.runSlowTickOnSecondCore** = True/[False]  -->  Sets whether the Slow tick gets called on the second CPU core
      - **self.slowTickFrequency** = [20]                -->  Sets the Slow tick timer frequency
      - **self.fastTickFrequency** = [1000]              -->  Sets the Fast tick timer frequency
6. Instantiate your class from your **\_\_main\_\_** and call its **run()** method. Note that **run()** does not return. All custom application logic should be put in the beforeRun, fastTick and slowTick methods for the inheriting class.


## Notes:
 - Making the SlowTick run on the second CPU core causes communications with Thonny to sometimes hang. Physically disconnecting and reconnecting the Raspberry Pi Pico solves this problem.
 - I wrote this code for my own convenience. It'll always be a work in progress.

## Github:
https://github.com/DevOats/PiPicoRunnerBase


Happy coding! :)