from datetime import datetime

today = datetime.today()


def is_weekday():
    return 0 <= today.weekday() < 5
