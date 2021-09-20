import datetime as dt
from plyer import notification as nt
from playsound import playsound


## date=dt.datetime.now()
## print(date.year,date.month,date.day)             ## Accessing to each attribute of datetime module
## print(date.hour,date.minute,date.second)


print('Please the required data below..')
date2=int(input('Enter the date : '))
month=int(input('Enter the month (in ten digit) : '))
year=int(input('Enter the year : '))
hour=int(input('Enter the hour(24 hr format) : '))
mint=int(input('Enter the minute : '))
msg=input('Enter the message/reminder : ')
date_fin=str(year)+str('-')+str(month)+str('-')+str(date2)
time_fin=str(hour)+str(' : ')+str(mint)+str(' : ')+str('00')
print('Reminder has been set for ~ ','   date :',date_fin,'  /\  time ~',time_fin)

while True:
    date=dt.datetime.now()
    date1=date.day
    month1=date.month
    year1=date.year
    hour1=date.hour
    mint1=date.minute
    sec1=date.second

    if year1==year and month1==month and date1==date2 and hour1==hour and mint1==mint:
        nt.notify(title=' REMINDER..',message=msg,timeout=10)
        playsound('/home/ashutosh/Downloads/notsound.mp3')
        break