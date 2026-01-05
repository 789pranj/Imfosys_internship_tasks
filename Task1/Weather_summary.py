def hottest_day(weather):
    max_temp = weather[0]["temp"]
    day = weather[0]["day"]

    for data in weather:
        if data["temp"] > max_temp:
            max_temp = data["temp"]
            day = data["day"]

    return day


def average_temperature(weather):
    total = 0
    count = 0

    for data in weather:
        total = total + data["temp"]
        count = count + 1

    return total / count


def count_rainy_days(weather):
    count = 0

    for data in weather:
        if data["rain"] == True:
            count = count + 1

    return count


def Analyse(weather):
    summary = {}

    summary["hottest_day"] = hottest_day(weather)
    summary["average_temperature"] = average_temperature(weather)
    summary["rainy_days"] = count_rainy_days(weather)

    return summary

weather = [
    {"day": "Mon", "temp": 32, "rain": False},
    {"day": "Tue", "temp": 35, "rain": True},
    {"day": "Wed", "temp": 30, "rain": False}
]

result = Analyse(weather)
print(result)
