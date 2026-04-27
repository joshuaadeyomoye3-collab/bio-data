def pressure_feed(readings):
    for reading in readings:
        yield reading

        if reading < 1000:
            yield "CRITICAL"
        elif reading < 2500:
            yield "LOW"
        elif reading < 4500:
            yield "NORMAL"
        else:
            yield "OVERPRESSURE"

feed = pressure_feed([3850, 820, 4600, 3200, 650])
for item in feed:
    print(item)
