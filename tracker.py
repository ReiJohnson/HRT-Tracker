"""
HRT Patch aopplication Tracking Software
Coded in Python
Abide by Standard MIT License
Free for all use cases
"""
import os

# Arrays for X and Y Graph Coordinates
mylanTransdermalAbArrY = [110, 120, 137.5,
                          112.5, 110, 105,
                          97.5, 92.5, 85,
                          80, 75, 72.5,
                          70, 67.5, 17.5,
                          5]
mylanTransdermalAbArrX = [12, 24, 36,
                          48, 60, 72,
                          84, 96, 108,
                          120, 132, 144,
                          156, 168, 180,
                          192]
mylanTransdermalBtArrY = [120, 155, 147.5,
                          150, 120, 115,
                          107.5, 102.5,
                          95, 90, 85,
                          82.5, 80, 77.5,
                          17.5, 5]
mylanTransdermalBtArrX = [12, 24, 36,
                          48, 60, 72,
                          84, 96, 108,
                          120, 132, 144,
                          156, 168, 180,
                          192]

# Error Rates for Each Method
MYLANTAAERRORMAX = -10
MYLANTAAERRORMIN = -2.5
MYLANTBAERRORMAX = +15
MYLANTBAERRORMIN = +2.5


def seek_rate_now(time_hours, loc):
    """
    Create an approximation of:
    - Current application rate

    To be used for:
    - Approximating error
    """
    if loc == 'ab': # Location is abdomen
        # Get time delta
        val_time = mylanTransdermalAbArrX.index(min(mylanTransdermalAbArrX,
                                                   key=lambda x:abs(x-time_hours)))
        # Get delta min/max values for patch rate
        val_upper = mylanTransdermalAbArrY[val_time] # Max
        val_lower = mylanTransdermalAbArrY[val_time-1] # Min
    else:
        # Get time delta
        val_time = mylanTransdermalBtArrX.index(min(mylanTransdermalBtArrX,
                                                   key=lambda x:abs(x-time_hours)))
        # Get delta min/max values for patch rate
        val_upper = mylanTransdermalBtArrY[val_time] # Max
        val_lower = mylanTransdermalBtArrY[val_time-1] # Min

    return (val_upper+val_lower)/2 # Give back rate


os.system('clear' if os.name == "posix" else 'cls') # Clean terminal
startTimeD = input("How many days ago did you apply your patch: ") # Delta time help
location = input("Location: ") # Location Input
timeDifferenceHours = float(startTimeD)*24 # Real delta as a float
daysToChange = 3.5-float(startTimeD) # Change date

# Get optimal rate difference/delta
rateDiffOptimal = seek_rate_now(timeDifferenceHours, 'ab' if location in ['abdomen',
                                                                          'ab',
                                                                          'abs'] else 'bt')-97.5

os.system('clear' if os.name == "posix" else 'cls') # Clean input questions
print('+'+str(rateDiffOptimal) if rateDiffOptimal > 0 else '-'+str(rateDiffOptimal)) # Rate
print('Reccomended change in: ' + str(daysToChange)) # Recommended change
