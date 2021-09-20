import time
import datetime as dt
from plyer import notification as nf

while True:
    start_time=dt.datetime.now()
    start_hour=start_time.strftime('%I')
    start_min =start_time.strftime('%M')

    while True:
        cur_time=dt.datetime.now()
        cur_hour=cur_time.strftime('%I')
        cur_min =cur_time.strftime('%M')

        if (int(cur_hour)==int(start_hour)+2)  and  (int(cur_min)-int(start_min)==0):

            nf.notify(title="Caution...!",message="You have been coding for 2 hrs. Please take some rest..",timeout=10)
            print('Notified...')
            break
