def gen_secs():
    for second in range(0, 60):
        yield second


def gen_minutes():
    for minute in range(0, 60):
        yield minute


def gen_hours():
    for hour in range(0, 24):
        yield hour


def gen_months():
    for month in range(1, 12):
        yield month


def gen_years(start=2019):
    while True:
        yield start
        start += 1


def gen_days(month, leap_year=True):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        days_in_month = 31
    elif month in [4, 6, 9, 11]:
        days_in_month = 30
    elif month == 2 and leap_year:
        days_in_month = 29
    else:
        days_in_month = 28

    for days in range(1, days_in_month + 1):
        yield days


def gen_time():
    for hours in gen_hours():
        for minutes in gen_minutes():
            for seconds in gen_secs():
                yield "%02d:%02d:%02d" % (hours, minutes, seconds)


def is_leap_year(year):  # return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    # import calendar
    # print(calendar.isleap(1900))
    if year % 4 == 0 and not (year % 100 == 0 or year % 400 == 0):
        return True
    else:
        return False


def gen_date():
    for year in gen_years():
        for month in gen_months():
            for day in gen_days(month, is_leap_year(year)):
                for time in gen_time():
                    yield "%02d/%02d/%02d %s" % (day, month, year, time)


gd = gen_date()
for i in range(1000000):
    next(gd)
print(next(gd))
