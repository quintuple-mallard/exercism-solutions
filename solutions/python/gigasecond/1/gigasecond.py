from datetime import datetime, timedelta
def add(moment):
    new_time = moment + timedelta(seconds=1e9)
    return new_time
