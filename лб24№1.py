from datetime import datetime, timedelta

def time_to_new_year():
    now = datetime.now()
    next_new_year = datetime(now.year + 1, 1, 1)
    time_left = next_new_year - now
    
    days = time_left.days
    hours, remainder, = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    print(f"До нового року залишилось: {days} днів, {hours} годин, {minutes} хвилин, {seconds} секунд")

time_to_new_year()