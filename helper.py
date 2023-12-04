import pandas as pd

def add_days(x, days):
    new_x = list()
    for day in range(days):
        new_x.append(x[len(x)-1] + pd.to_timedelta(day, unit='D')) 
    return new_x
