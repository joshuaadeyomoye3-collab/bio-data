#task 1
def greet_engineer(name):
    print("Good morning " + name ,"" + "Ready to monitor the rig?")
greet_engineer("emeka")
greet_engineer("joshua")

def rig_status(well_name ,is_active  ):
    if is_active:
        print(well_name + "is Online")
    else:
        print(well_name + "is Offline— maintenance required ")

rig_status("zlatan-02 ", True)
rig_status("Konga-09 ", False)
rig_status("Ogbafia-06 ", True)

def calculate_daily_output(flow_rate, hours_active):
    return flow_rate * hours_active
print(f"daily_output:{ calculate_daily_output(50, 24)}")

print(calculate_daily_output(80, 18))
print(calculate_daily_output(120, 12))
print(calculate_daily_output(120, 12))

#taskb
def classify_pressure(pressure):
    if pressure < 1000:
        return "CRITICAL"
    elif pressure < 2500:
        return "LOW"
    elif pressure < 4500:
        return "NORMAL"
    elif pressure >= 4500:
        return "OVERPRESSURE"
    else:
        return "invalid"

print(classify_pressure(650))
print(classify_pressure(1500))
print(classify_pressure(3850))
print(classify_pressure(4600))

def maintenance_due(days_since_service):
    if days_since_service > 90:
        return "Overdue"
    elif days_since_service > 60:
        return "Due soon"
    else:
        return "OK"
print(maintenance_due(30))
print(maintenance_due(50))
print(maintenance_due(80))

def access_level(role):
    match role:
        case "supervisor":
            return "Full access"
        case "engineer":
            return "Operational access"
        case "contractor":
            return "Limited access"
        case _:
            return "No access"
print(access_level("supervisor"))
print(access_level("engineer"))
print(access_level("contractor"))
print(access_level("jimoh"))

#taskc
wells = [
    {"name": "Bonga-01",  "pressure": 3850},
    {"name": "Bonga-03",  "pressure": 820},
    {"name": "Erha-02",   "pressure": 4600},
    {"name": "Erha-05",   "pressure": 3200},
    {"name": "Agbami-02", "pressure": 650},
]
def check_all_wells(wells):
    for well in wells:
        status = classify_pressure(well["pressure"])
        print(well["name"], "|", well["pressure"], "psi", "|", status)

check_all_wells(wells)

def count_critical(wells):
    count = 0
    for well in wells:
        if classify_pressure(well["pressure"]) == "CRITICAL":
            count += 1
    return count

critical_total = count_critical(wells)
print(critical_total, "well(s) are in CRITICAL condition")

def pressure_monitor():
    while True:
        reading = int(input("Enter pressure reading (or 0 to quit): "))
        if reading == 0:
            break
        status = classify_pressure(reading)
        print("Status:", status)

pressure_monitor()

#taskd
def run_daily_check(wells):
    total_checked = 0
    critical_count = 0
    maintenance_count = 0

    for well in wells:
        if well["pressure"] == 0:
            continue

        status = classify_pressure(well["pressure"])

        maintenance = maintenance_due(45)

        if status == "CRITICAL":
            critical_count += 1

        if maintenance != "OK":
            maintenance_count += 1

        total_checked += 1

        print(well["name"], "|", status, "| Maintenance:", maintenance)

    print("─" * 45)
    print("Total wells checked:", total_checked)
    print("Critical wells:", critical_count)
    print("Wells needing maintenance:", maintenance_count)
    print("─" * 45)

run_daily_check(wells)


