from datetime import datetime

def convert_date(date_string):
    year = int(date_string[:4])
    month = int(date_string[5:7])
    day = int(date_string[-2:])
    return datetime(year, month, day)