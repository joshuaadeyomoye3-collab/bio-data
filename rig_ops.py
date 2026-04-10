# rig_ops.py
# NDI Phase 2 — Rig Operations Data System
# Author: [Your Name]

# ── STARTER DATA ─────────────────────────────────────

# List of well dictionaries
wells = [
    {"name": "Bonga-01",   "pressure": 3850, "temp": 185, "active": True,  "engineer": "Emeka Eze"},
    {"name": "Bonga-03",   "pressure": 820,  "temp": 310, "active": True,  "engineer": "Chidi Obi"},
    {"name": "Erha-02",    "pressure": 4600, "temp": 200, "active": True,  "engineer": "Fatima Bello"},
    {"name": "Bonga-07",   "pressure": 2100, "temp": 175, "active": False, "engineer": "N/A"},
    {"name": "Erha-05",    "pressure": 3200, "temp": 290, "active": True,  "engineer": "Tunde Adeyemi"},
    {"name": "Agbami-02",  "pressure": 650,  "temp": 165, "active": True,  "engineer": "Ngozi Okafor"},
]

# Tuple of rig coordinates (NEVER changes)
rig_location = ["Bonga Field", 3.7800, 5.6200]

# Set of known alert types (starts empty)
active_alerts = set()

# ── YOUR CODE GOES BELOW THIS LINE ───────────────────



# TASK1 list
# Loop through the wells list and print each well name
print('All wells:')
for well in wells:
    print(well['name'])
# Slicing pulls out only the first 3 items from the list
print('\nFirst 3 wells:')
# for well in wells[:3]:
#     print(well['name'])
print(wells[0:3])
# len helps us to count how many items are currently in the list
print(f'\nTotal wells: {len(wells)}')
# append() helps to add a new well dictionary to the end of the list
wells.append({
    'name': 'Agbami-05',
    'pressure': 3100,
    'temp': 195,
    'active': True,
    'engineer': 'Yemi Coker'
})
print('Agbami-05 added to the list.')

# We loop through so we can find Bonga-07 before removing it
for well in wells:
    if well['name'] == 'Bonga-07':
        wells.remove(well)
        print('Bonga-07 removed.')

print(f'Updated list length: {len(wells)}')
#task2
# Tuples store ordered data that should never be changed
print('\nFull rig location tuple:')
print(rig_location)
print(rig_location[0])
print(f'Latitude: {rig_location[1]}')
print(f'Longitude: {rig_location[2]}')
#rig_location[1] = 4.0
#Replace tuple with list
#task3
#alert_log = [
   # "pressure_high", "valve_leak", "pressure_high",
   # "temp_spike", "valve_leak", "pump_failure", "pressure_high"
#]
unique_alerts = {"pressure_high", "valve_leak", "pressure_high",
   "temp_spike", "valve_leak", "pump_failure", "pressure_high"}
print(unique_alerts)
unique_alerts.add("gas_leak")
print(unique_alerts)
unique_alerts.discard("temp_spike")
print(unique_alerts)
if "valve_leak" in unique_alerts:
    print("ALERT ACTIVE")
#task4
well_profile = {
    "name":         "Bonga-01",
    "pressure":     3850,
    "temp":         185,
    "status":       "Active",
    "engineer":     "Emeka Eze",
    "last_checked": "2026-04-01"
}
print(well_profile)
for x,y in well_profile.items():
    print(x,y)
well_profile.update({"Pressure": 4100})
print(well_profile)
well_profile.update({"next_service": "2026-05-01"})
print(well_profile)
del well_profile ["temp"]
print(well_profile)
if "status" in well_profile:
    print("Status key exists.")
print(list(well_profile.keys()))
print(list(well_profile.values()))
#task5
active_count = 0
critical_count = 0
print("\nActive well status:")
for well in wells:
    if not well["active"]:
        continue
    pressure = well["pressure"]
    temp = well["temp"]
    if pressure < 1000:
        status = "CRITICAL"
    elif pressure < 2500:
        status = "LOW PRESSURE"
    elif temp > 280:
        status = "HIGH TEMP"
    else:
        status = "NORMAL"
    if status in ("CRITICAL", "HIGH TEMP"):
        active_alerts.add(status)
    if status == "CRITICAL":
        critical_count += 1
    active_count += 1
    print(well["name"], "|", pressure, "psi", "|", status, "| Engineer:", well["engineer"])
print("Total active wells:", active_count)
print("Active alerts:", active_alerts)
print("Critical wells:", critical_count)
#task6
print("\n" + "─" * 45)
print("   NIGERIA OIL FIELD — DAILY OPERATIONS REPORT")
print("─" * 45)
print(f"  Total wells in system : {len(wells)}")
print(f"  Total active wells    : {active_count}")
print(f"  Critical wells        : {critical_count}")

print("\n  [ ACTIVE WELL STATUS ]")
for well in wells:
    if well["active"]:
        continue
    pressure = well["pressure"]
    temp = well["temp"]
    if pressure < 1000:
        status = "CRITICAL"
    elif pressure < 2500:
        status = "LOW PRESSURE"
    elif temp > 280:
        status = "HIGH TEMP"
    else:
        status = "NORMAL"
    print(f"{well['name']}  |  {pressure} psi  |  {status}  |  {well['engineer']}")

print("\n  [ CRITICAL / HIGH TEMP WELLS ]")
for well in wells:
    if not well["active"]:
        continue
    pressure = well["pressure"]
    temp = well["temp"]
    if pressure < 1000:
        print(f"{well['name']} — CRITICAL")
    elif temp > 280:
        print(f"{well['name']} — HIGH TEMP")

print(f"\n  [ ACTIVE ALERTS ]\n    {active_alerts}")
print("\n" + "─" * 45)
print("   END OF REPORT")
print("─" * 45)
