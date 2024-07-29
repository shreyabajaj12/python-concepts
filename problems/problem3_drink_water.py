#write a python program which eminds you of drinking water every hour or two. that sends either a beeep or a notification of it.
from win10toast import ToastNotifier
import time
notification=ToastNotifier()
time.sleep(4)
notification.show_toast(
    "Reminder",
    "Drink Water! Time to hydrate",
    duration=2,
    icon_path=r"C:\Users\C..VISION\Pictures\Screenshots\csesce\Screenshot 2023-11-25 165456.png",
    threaded=True
)