import kivy

mylanTransdermalAbArrY = [110, 120, 137.5, 112.5, 110, 105, 97.5, 92.5, 85, 80, 75, 72.5, 70, 67.5, 17.5, 5]
mylanTransdermalAbArrX = [12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144, 156, 168, 180, 192]
mylanTransdermalBtArrY = [120, 155, 147.5, 150, 120, 115, 107.5, 102.5, 95, 90, 85, 82.5, 80, 77.5, 17.5, 5]
mylanTransdermalBtArrX = [12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144, 156, 168, 180, 192]

mylanTAAErrorMax = -10
mylanTAAErrorMin = -2.5
mylanTBAErrorMax = +15
mylanTBAErrorMin = +2.5

def seekRateNow(timeHours, loc):
    if loc == 'ab':
        valTime = mylanTransdermalAbArrX.index(min(mylanTransdermalAbArrX, key=lambda x:abs(x-timeHours)))
        valUpper = mylanTransdermalAbArrY[valTime]
        valLower = mylanTransdermalAbArrY[valTime-1]
    else:
        valTime = mylanTransdermalBtArrX.index(min(mylanTransdermalBtArrX, key=lambda x:abs(x-timeHours)))
        valUpper = mylanTransdermalBtArrY[valTime]
        valLower = mylanTransdermalBtArrY[valTime-1]

    return (valUpper+valLower)/2            




startTimeD = input("How many days ago did you apply your patch: ")
location = input("Location: ")
timeDifferenceHours = int(startTimeD)*24
daysToChange = 3.5-float(startTimeD)

rateDiffOptimal = seekRateNow(timeDifferenceHours, 'ab' if location == 'abdomen' else 'bt')-97.5
print('+'+str(rateDiffOptimal) if rateDiffOptimal > 0 else '-'+str(rateDiffOptimal))
print('Reccomended change in: ' + str(daysToChange))