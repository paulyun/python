#In class Activity for 3/10/2016

totalTime = int(input ("Enter a time in seconds"))

resultMinutes = int(totalTime / 60) #this function divides the users totaltime by 60 to get the minute value
resultSeconds = totalTime % 60 #this function gets the remainder value of the totaltime divided by 60 to get the remaining seconds value

print (resultMinutes,"Minutes", resultSeconds,"Seconds")
