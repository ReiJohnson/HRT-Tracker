import datetime
import matplotlib.pyplot as plt
import tkinter as tk

mylanTransdermalAbArrY = [110, 120, 137.5, 112.5, 110, 105, 97.5, 92.5, 85, 80, 75, 72.5, 70, 67.5, 17.5, 5]
mylanTransdermalAbArrX = [12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144, 156, 168, 180, 192]
mylanTransdermalBtArrY = [120, 155, 147.5, 150, 120, 115, 107.5, 102.5, 95, 90, 85, 82.5, 80, 77.5, 17.5, 5]
mylanTransdermalBtArrX = [12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144, 156, 168, 180, 192]

mylanTAAErrorMax = -10
mylanTAAErrorMin = -2.5
mylanTBAErrorMax = +15
mylanTBAErrorMin = +2.5
mylanTBAFitLine = None


def modData(x):
    yVals = []

    for i in mylanTransdermalAbArrY:
        erroredVal = lambda a : a+mylanTAAErrorMin if mylanTransdermalAbArrY.index(a) > 10 else a+2.5
        yVals.append(erroredVal(i))

    return plt.plot(x, yVals)


mylanTAAFitLine = modData(mylanTransdermalAbArrX)
mylanTBAFitLine = modData(mylanTransdermalBtArrX)

startTime = input("How many days ago did you apply your patch: ")
timeDifferenceHours = startTime*24