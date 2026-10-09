from datetime import datetime, timedelta

now = datetime.now()
up = datetime.now() + timedelta(hours=8)

def countdown(time_now, time_up, index = 8):
    if index == 0:
        print("good morning!") #return signals the end --> stops the recursion
        return
    return countdown(time_now, time_up, index-1)

countdown(now, up)

    