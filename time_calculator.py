"""Arithmetic Formatter"""


def add_time(start_time: str = "", duration: str = "", day: str = "") -> str:
    """
    :type start_time: str
    :type duration: str
    :type day: str
    :param start_time: False
    :param duration: ""
    :param day: ""
    """
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    tm = start_time[-3:]
    start_time = list(map(int, start_time[:-3].split(':')))
    duration = list(map(int, duration.split(':')))

    minutes = start_time[-1] + duration[-1]
    start_time[0] = start_time[0] + duration[0]

    while minutes > 60:
        hours, minutes = divmod(minutes, 60)
        start_time[0] += hours
    count = 0

    while start_time[0] >= 12:
        start_time[0] -= 12
        if 'PM' in tm:
            count += 1
            tm = tm.replace('PM', 'AM')
        elif 'AM' in tm:
            tm = tm.replace('AM', 'PM')
    hour = start_time[0] + 12 if start_time[0] == 0 else start_time[0]
    if day:
        day_i = days.index(day.lower())
        day = days[(day_i + count) % len(days)] if day_i != -1 else ""
        new_time = "{}:{}{}{}".format(hour, "{0:0=2d}".format(minutes), tm, ", " + day.capitalize())
    else:
        new_time = "{}:{}{}".format(hour, "{0:0=2d}".format(minutes), tm)
    if count == 1:
        new_time += ' (next day)'
    elif count > 1:
        new_time += ' (' + str(count) + ' days later)'
    return new_time
