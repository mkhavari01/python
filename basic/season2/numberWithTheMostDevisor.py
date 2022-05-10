numbers = []
devisorNumebrsCountList = []
number = int(input("please enter a number: "))

while number != -1:
    devisorCount = 0
    numbers.append(number)
    devisonLoopTimes = int(number/2)
    while devisonLoopTimes != 0:
        if number % devisonLoopTimes == 0:
            devisorCount += 1
        devisonLoopTimes -= 1
    devisorNumebrsCountList.append(devisorCount+1)
    number = int(input("please enter another number: "))

print("the most devisoner has ",max(devisorNumebrsCountList),"number and its value is",numbers[devisorNumebrsCountList.index(max(devisorNumebrsCountList))])

print(numbers)
print(devisorNumebrsCountList)
