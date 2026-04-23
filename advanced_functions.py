import time
from unittest import result


def well_report(well_name, pressure, status="active", location="offshore"):
    print("Well:", well_name, "Pressure:", pressure, "Status:", status, "Location:", location)

# Call 1 — positional only (use all defaults)
well_report('Bonga-01', 3850)

# Call 2 — override status with keyword argument
well_report('Erha-02', 4600, status='Under Review')

# Call 3 — override both defaults
well_report('Agbami-05', 2100, status='Inactive', location='Onshore')

# Call 4 — all keyword arguments, no positional order
well_report(pressure=820, well_name='Bonga-03', location='Deep Water')

#task2
def log_pressures(*readings):
    for reading in readings:
        print("Reading:", reading,"psi")
    print("Highest Reading:", max(readings))

log_pressures(3850,820,2100)
log_pressures(3850,820,2100,3200,650,2100)

#2b
def create_well_profile(**details):
    for key, value in details.items():
        print(key, ":", value)

print(create_well_profile(name = "Bonga-01", pressure= 3850,status="Under Review"))
print(create_well_profile(name = "Erha-02", pressure= 820, status="Inactive", location="Onshore", field= "Bonga", depth="3500"))

#2c
def rig_summary(rig_name,*wells,**stats):
    print("Rig:", rig_name)
    print("Wells:", wells)
    print("Stats:", stats)

rig_summary(
    'Bonga Field',
    'Bonga-01', 'Bonga-03', 'Bonga-07',
    total_output=12400, uptime_pct=94.2, crew_count=47
)


#task3
rig_status = "operational"

def show_status():
    print(rig_status)

def update_status(new_status):
    global rig_status
    rig_status=new_status

show_status()
update_status("Shutdown")
show_status()

#3b
def pressure_tracker():
    current_max = 0
    def update_max(reading):
        nonlocal current_max
        if reading > current_max:
            current_max = reading

    update_max(3200)
    update_max(4800)
    update_max(1500)
    print(f'Peak pressure recorded: {current_max} psi')


pressure_tracker()


#task4
def log_call(func):
    def wrapper(*args, **kwargs):
        print("Function Started")
        result = func(*args, **kwargs)
        print("Function Complete")
        return result
    return wrapper

@log_call
def check_well(well_name):
    print(f"Checking: {well_name}")

check_well("Bonga-01")

#4b
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Time taken:", round(end - start, 2), "seconds")
        return result
    return wrapper

@timer
def run_pressure_scan():
    for i in range(1_000_000):
        pass
    print("pressure scan complete")

run_pressure_scan()

#task5
psi_to_bar = lambda psi: psi * 0.0689476
print("3850 psi in bar:", psi_to_bar(3850))

format_well = lambda name, status: name + "-" + status
print(format_well("Bonga-01", "ACTIVE"))

wells = [
    {'name': 'Bonga-01',  'pressure': 3850},
    {'name': 'Agbami-02', 'pressure': 650},
    {'name': 'Erha-02',   'pressure': 4600},
    {'name': 'Bonga-03',  'pressure': 820},
    {'name': 'Erha-05',   'pressure': 3200},
]

sorted_wells = sorted(wells, key=lambda w: w['pressure'], reverse=True)
print("Sorted by pressure:")
for w in sorted_wells:
    print(" ",w["name"], w["pressure"])


high_pressure = list(filter(lambda w: w["pressure"] > 3850, wells))
print("Wells above 3000 psi:")
for w in high_pressure:
    print(" ",w["name"])


high_pressure = list(filter(lambda w: w["pressure"] > 3000, wells))
print("Wells above 3000 psi:")
for w in high_pressure:
    print(" ",w["name"])

uppercase_names = list(map(lambda w: w["name"].upper(), wells))
print(uppercase_names)

#task6
def countdown(n):
    if n < 0:
        return
    print(n)
    countdown(n-1)

print(countdown(10))

#6b
def sum_readings(readings):
    if len(readings) == 0:
        return 0
    return readings[0] + sum_readings(readings[1:])

print(sum_readings([3850, 820, 4600, 3200, 650]))

#6c
def find_deepest(wells, current_max=0):
    if len(wells) == 0:
        return current_max
    first_pressure = wells[0]["pressure"]
    if first_pressure>current_max:
        current_max = first_pressure
    return find_deepest(wells[1:], current_max)

wells = [
    {'name': 'Bonga-01',  'pressure': 3850},
    {'name': 'Erha-02',   'pressure': 4600},
    {'name': 'Agbami-02', 'pressure': 650},
    {'name': 'Bonga-03',  'pressure': 820},
]

print(find_deepest(wells))

#7a
for i in range(1, 11):
    print("Well-" + str(i).zfill(2))

for i in range(2, 11, 2):
    print("Well-" + str(i).zfill(2))

for i in range(10, 0, -1):
    print(i)
print("Rig shutdown complete")

#7b
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

#7c
def well_id_generator(prefix='Well'):
    n = 1
    while True:
        yield f'{prefix}-{n:03d}'
        n += 1

gen = well_id_generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))



