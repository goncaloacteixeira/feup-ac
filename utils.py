def parse_date(date):
    year = int(str(date)[0:2])
    month = int(str(date)[2:4])
    day = int(str(date)[4:6])
    return year, month, day
