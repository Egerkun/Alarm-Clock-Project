from playsound import playsound
import time


def alarm(secs):
    for x in range(secs, -1, -1):
        minutes, seconds = divmod(x, 60)
        print(f"\r{minutes:02d}:{seconds:02d}", end="")
        time.sleep(1)
    print(" Time's Up!")
    playsound("alarm.mp3")



alarm(5)
