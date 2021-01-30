import datetime as dt


if dt.datetime.now().strftime("%H:%M") == dt.time(hour=2, minute=16).strftime("%H:%M"):  # 24 hour format
    print('It is time')
else:
    print('There is time to wait')