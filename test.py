from datetime import datetime, timedelta

def sleep_time():
    now = datetime.now()
    seconds_till_midnight = (timedelta(hours=24) - (now - now.replace(hour=0, minute=0, second=0, microsecond=0))).total_seconds() % (24 * 3600)
    print(seconds_till_midnight)

sleep_time()