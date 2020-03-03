import datetime 

def calculate_time_interval_day(final_date: datetime, begin_date: datetime):
    delta: datetime = final_date - begin_date
    return(delta.days)