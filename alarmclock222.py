import datetime
from playsound import playsound

alarmHour = int(input("What hour do you want the alarm to ring? "))
alarmMinute = int(input("What minute do you want the alarm to ring? "))
amorPm = str(input("am or pm? "))
print("Waiting for alarm", alarmHour, alarmMinute, amorPm)

if (amorPm == "pm"):
    alarmHour = alarmHour + 12

while (1 == 1):
    if (alarmHour == datetime.datetime.now().hour and
            alarmMinute == datetime.datetime.now().minute):
        print("Time to wake up")
        playsound("alarm.mp3")
        break
