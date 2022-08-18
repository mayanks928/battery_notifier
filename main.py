# %%
import psutil,time,plyer
from plyer import notification

# %%
def cnvrtseconds(secs):
    mins,secs=secs//60,secs%60
    hrs,mins=mins//60,mins%60
    s="Hrs:{hrs} Mins:{mins} Seconds:{secs}".format(hrs=hrs,mins=mins,secs=secs)
    return s

# %%
while(True):
    batteryinfo=psutil.sensors_battery()
    percent=batteryinfo.percent
    mssg="Battery Percent:{}\n".format(percent)
    if (batteryinfo.power_plugged):
        mssg=mssg+"Battery is Charging"
    else:
        mssg=mssg+cnvrtseconds(batteryinfo.secsleft)
    notification.notify(title="Battery Notifier",message=mssg,app_icon = None,  timeout = 2,  toast =False  )
    time.sleep(60)
