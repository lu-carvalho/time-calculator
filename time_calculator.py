def add_time(startingTime, duration, weekDay = ""):
    
  # extract from input the starting hour, minute and period of the day
  startingHour = int(startingTime.split(":")[0])
  startingMinute = int(startingTime.split(":")[1][0:2])
  period = startingTime.split(" ")[1]

  # set variables of hours to add and days to 0 
  hoursToAdd = 0
  days = 0

  # convert PM hours to 24 hour format to make it easier to add the time
  if period == "PM":
    startingHour = startingHour + 12
    
  # sum the duration minutes to the starting time 
  durationMinute = int(duration.split(":")[1])
  newMinute = startingMinute + durationMinute

  # transform minutes in hours if it exceeds 59 minutes and keep remaining minutes
  while newMinute >= 60:
    newMinute = newMinute % 60 
    hoursToAdd += 1 
    
  # format single digit minutes 
  if newMinute < 10:
    newMinute = "0"+ str(newMinute)

  # extract amount of duration hours
  durationHours = int(duration.split(":")[0])

  # transform hours in days if it exceeds 23 hours and keep remaining hours
  while durationHours >= 24:
    days = int(durationHours/24)
    durationHours = durationHours % 24

  # find out the new hour by summing up starting hour, duration hour and hours to add (extracted from the minutes)
  newHour =  startingHour + durationHours + hoursToAdd

  # transform the new hour in days if it exceeds 24 hours
  while newHour >= 24:
    newHour = newHour % 24
    days += 1

  # transform hour back to AM/PM, avoiding some case errors
  if newHour > 13:
    newHour = newHour - 12
    period = "PM"
  elif period == "AM" and newHour == 12 and ((durationHours+hoursToAdd) < 13):
    period = "PM"
  else:
    period = "AM"
    
  # transforming midnight from 0 to 12 AM 
  if period == "AM" and newHour == 0:
    newHour = 12

  # display how many days later, if so
  if days == 1:
    newDay = "(next day)"
    
  elif days > 1:
    newDay = f"({days} days later)"
    
  else:
    newDay = ""
    
  newTime = str.strip(f"{newHour}:{newMinute} {period} {newDay}")
  
  # associate days of the week to a value in a dict to make it easer
  weekDays = {
    "monday": 1,
    "tuesday": 2,
    "wednesday": 3,
    "thursday": 4,
    "friday": 5,
    "saturday": 6,
    "sunday": 7
  }
    
  # extract the keys from the dict
  keyList = list(weekDays.keys())

  # associate day of the week in the key value pair, sum with days to add, divide by 7 and the remaining - 1 will be the value to the key day
  if weekDay == "":
    pass
  else: 
    weekDay = weekDay.lower()
    weekDay = weekDays[weekDay]
    #weekDay = (weekDay + days) % 7
    weekDay = keyList[((weekDay + days) % 7) - 1]

    newTime = newTime = str.strip(f"{newHour}:{newMinute} {period}, {weekDay.capitalize()} {newDay}")

  return newTime