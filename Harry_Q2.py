import time
t = time.strftime('%H:%M:%S')
print(t)
hour = int(time.strftime('%H'))
print(hour)
min = int(time.strftime('%M'))
print(min)
sec = int(time.strftime('%S'))
print(sec)
if (hour >= 6 and hour < 12):
     print("Good Morning")
elif (hour >= 12 and hour < 17):
     print("Good Afternoon")
elif (hour >= 17 and hour < 0):
     print("Good Evening")
elif (hour >= 0 and hour < 6):
     print("Good Night")