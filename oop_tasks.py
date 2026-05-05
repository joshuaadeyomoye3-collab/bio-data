import json
import re
#task 1a dict to json
well_data = {
    "name": "Bonga-01",
    "pressure": 3850,
    "temp": 185,
    "active": True,
    "engineer": "Emeka Eze"
}
json_string = json.dumps(well_data)
print(json_string)
print(json.dumps(well_data, indent=2))
print(json.dumps(well_data, sort_keys=True, indent=2))

#task1b json to dict
json_str = '''
{
    "name": "Erha-02",
    "pressure": 3850,
    "temp": 185,
    "active": true,
    "engineer": "Fatima Bello"
}
'''

well_dict = json.loads(json_str)
print(well_data)

print(well_dict["engineer"])

well_dict["pressure"] = 4200
print(well_data["pressure"])

update_json = json.dumps(well_dict, indent=2)
print(update_json)

#task 1c Read/Write JSON file
# wells_list = [
#     {"name": "Bonga-01", "pressure": 3850},
#     {"name": "Erha-02",  "pressure": 4600},
#     {"name": "Agbami-02","pressure": 650}
# ]
#
# with open("wells.json", "w") as file:
#     json.dump(wells_list, file, indent=2)
#
# with open("wells.json", "r") as file:
#     loaded_wells = json.load(file)
#
# for well in loaded_wells:
#     print(well["name"], "|", well["pressure"], "psi")
well_1 = {"name": "Bonga-01", "pressure": 3850}
well_2 = {"name": "Erha-02", "pressure": 4200}
well_3 = {"name": "Agbami-02", "pressure": 4200}

wells_jons = (well_1, well_2, well_3)
to_python = json.dumps(wells_jons)
read_back = json.loads(to_python)

for well in read_back:
    print(f"The well name is {well['name']} and pressure is {well['pressure']}")

#task 2a search and match
log_entry = "Pressure alert triggered on Bonga-03 at 04:32 UTC"
match = re.search(r"\w+-\d+", log_entry)
print(match)
print(match.group())

#task 2b find all matches
ops_log = '''
Erha-02 pressure normal. Bonga-01 valve checked.
Agbami-05 flagged for review. Bonga-01 cleared.
Erha-02 output at 94%. Bonga-07 offline.
'''

all_wells = re.findall(r'[A-Za-z]+-\d+', ops_log)
print("all_wells:", all_wells)


unique_wells = set(all_wells)
print("unique_wells:", unique_wells)

match = re.search(r'Agbami-05', ops_log)
if match:
    print("Found:", match.group())
else:
    print("Well not found")

flagged_wells = re.findall(r'[A-Za-z]+-\d+\s+flagged for review', ops_log)
print("flagged_wells:", flagged_wells)

offline_wells = re.findall(r'[A-Za-z]+-\d+\s+offline', ops_log)
print("offline wells:", offline_wells)

#task2c validate input
def validate_well_id(well_id):
    pattern = r'^[A-Za-z]{1,10}-\d{2}$'
    return bool(re.match(pattern, well_id))
print(validate_well_id('Bonga-01'))
print(validate_well_id('bonga1'))
print(validate_well_id('Erha-02'))
print(validate_well_id('well-03'))


#task 3a basic error catching
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Invalid input — numbers only"

print(safe_divide(100, 4))
print(safe_divide(100, 0))
print(safe_divide(100, "x"))

#task 3b Multiple exceptions + finally
def load_well_pressure(data, key):
    try:
        return float(data[key])
    except KeyError:
        print('Key not found in well data')
        return None
    except ValueError:
        print('pressure value cannot be converted to a number')
    finally:
        print("Pressure check complete")



#task 3c raise your own error
def set_pressure(value):
    if value < 0:
        raise ValueError("Pressure value cannot be negative")
    return value

try:
    set_pressure(-500)
except ValueError as e:
    print("Error caught:", {e})


#task 4a String Formatting
well_name = "Bonga-01"
pressure = 3200.5
engineer = "Abdul Joshua"

print("Well: %s | Pressure: %.1f | Engineer: %s" % (well_name, pressure, engineer))

print("Well: {} | Pressure: {:.1f} | Engineer: {}".format(well_name, pressure, engineer))

print(f"Well: {well_name} | Pressure: {pressure} | Engineer: {engineer}")

print("---")

oil_rate = 4521.67
print(f"Oil rate: {oil_rate:.2f} bbl/day")

#task 4b None
engineer = None
if engineer is None:
    print("no engineer assigned")
else:
    print(f"engineer: {engineer}")

print("---")

def get_well_status(well):
    return well.get("status")
well_a = {"name": "Bonga-01", "status": "Active"}
print(get_well_status(well_a))
print("---")

well_b = {"name": "Erha-02"}
print(get_well_status(well_b))
print("---")

#task 4c user input
# 4C User Input
# well_name = input("Enter well name: ")
#
# try:
#     well_pressure = int(input("Enter pressure reading: "))
#     print("Well:", well_name, "| Pressure:", well_pressure, "psi")
# except ValueError:
#     print("Invalid pressure — please enter a number")


#task 5 classes
class Welli:
    def __init__(self, name, pressure, temp, active = True, engineer = None):
        self.name = name
        self.pressure = pressure
        self.temp = temp
        self.active = active
        self.engineer = engineer


    def describe(self):
        print("Well:", self.name, "| Pressure: ", self.pressure,
              "| Temp: ", self.temp, "| Active: ", self.active,
              "| Engineer: ", self.engineer)

    def is_critical(self):
        if self.pressure < 1000 or self.temp > 300:
            return True
        else:
            return False

    def assign_engineer(self, name):
        self.engineer = name
        print("Engineer", name, "assigned to", self.name)


well1 = Welli("Bonga-01", 3850, 185)
well2 = Welli("Erha-02", 820, 310)
well3 = Welli("Agbami-02", 650, 165)

well1.describe()
print("Critical:", well1.is_critical())

well2.describe()
print("Critical:", well2.is_critical())

well3.describe()
print("Critical:", well3.is_critical())

well1.assign_engineer("Emeka Eze")
well1.describe()


#task 6 CLASS PROPERTIES - Getters & Setters

# class Well:
#     well_count = 0
#
#     def __init__(self, name, pressure, temp, active=True, engineer =None):
#         Well.well_count += 1
#         self.name = name
#         self._pressure = pressure
#         self.temp = temp
#         self.active = active
#         self.engineer = engineer
#
#
#     @property
#     def status(self):
#         if self._pressure < 1000:
#             return "Critical"
#         elif self._pressure < 2500:
#             return "low"
#         elif self._pressure < 4500:
#             return "normal"
#         else:
#             return "overpressure"
#
#     @classmethod
#     def get_well_count(cls):
#         return cls.well_count
#
#
# w1 = Well("Bonga-01", 3850, 185)
# w2 = Well("Erha-02", -500, 310)
# w3 = Well("Agbami-02", 650, 165)
# w4 = Well("Bonga-03", 4600, 200)
#
# lst = [w1, w2, w3, w4]
# print("Total wells created:", Well.get_well_count())
#
# try:
#     w1.pressure = -500
# except ValueError as e:
#     print(f"Error caught:, {e}")
#
# for wells in lst:
#     status = wells.status
#     print(f"{wells.name} status is {status}")

class Well:
    well_count = 0

    def __init__(self, name, pressure, temp):
        Well.well_count += 1
        self.name = name
        self._pressure = pressure
        self.temp = temp

    @property
    def pressure(self):
        return self._pressure

    @pressure.setter
    def pressure(self, value):
        if value < 0:
            raise ValueError('Pressure cannot be negative')
        self._pressure = value

    @property
    def status(self):
        if self.pressure < 1000:
            return "CRITICAL"
        elif self.pressure < 2500:
            return "LOW"
        elif self.pressure < 4500:
            return "NORMAL"
        else:
            return "OVERPRESSURE"


    @classmethod
    def get_well_count(cls):
        return cls.well_count



well1 = Well("Bonga-01", -4500, 200)
well2 = Well("Bonga-02", 2500, 250)
well3 = Well("Bonga-03", -100, 300)
well4 = Well("Agbami-01", 5200, 100)

lst = [well1, well2, well3, well4]
print(f"The total number of wells is {Well.get_well_count()}")

try:
    Well.pressure = -100
except ValueError as e:
    print("Error caught:", {e})

for wells in lst:
    status = wells.status
    print(f"{wells.name}: {status}")


#task 7 inheritance
class OffshoreWell(Welli):
    def __init__(self, name, pressure, temp, water_depth, platform_type):
        super().__init__(name, pressure, temp)
        self.water_depth = water_depth
        self.platform_type = platform_type

    def describe(self):
        return f"offshore well: {self.name}, Pressure: {self.pressure}, depth {self.water_depth}, Platform Type: {self.platform_type}, temp: {self.temp}"

    def depth_rating(self):
        if self.water_depth > 1500:
            return "Ultra Deep"

        elif self.water_depth > 500:
            return "Deep"

        else:
            return "Shallow"


class OnshoreWell(Welli):
    def __init__(self, name, pressure, temp, region, site_manager):
        super().__init__(name, pressure, temp)
        self.region = region
        self.site_manager = site_manager

    # def describe(self):
    #      return f"Onshore Well: {self.name},  Pressure: {self.pressure}, Region: {self.region}, Site Manager: {self.site_manager}, temp: {self.temp}"
    def describe(self):
        return f"offshore well: {self.name}, Pressure: {self.pressure}, region {self.region}, site manager: {self.site_manager}, temp: {self.temp}"

    def is_remote(self):
        if "Delta" in self.region or "Basin" in self.region:
            return True
        else:
            return False

ow1 = OffshoreWell("Bonga-01", 3850, 185, 1200, "FPSO")
ow2 = OffshoreWell("Erha-02", 4600, 200, 1800, "Fixed Jacket")

on1 = OnshoreWell("Delta-01", 820, 165, "Niger Delta", "Tunde Adeyemi")
on2 = OnshoreWell("Basin-02", 2100, 175, "Benin Basin", "Ngozi Okafor")

off = [ow1, ow2]
for us in off:
    print(f"This is an offshore platform detail {us.describe()} and also the condition is {us.is_critical()} and the depth is {us.depth_rating()} ")


onn = [on1, on2]
for log in onn:
    print(f"This is an onshore platform detail {log.describe()} and also the condition is {log.is_critical()}  ")

print(f"The total number of wells is {Well.get_well_count()}")


#task 8 polymorphism

# lst1 = Well("Agbami-05", 4700, 200)
#
# mix2= [
#     OffshoreWell("Bonga-03", 3200, 190, 800, "FPSO"),
#     OffshoreWell("Erha-05", 500, 165, 2000, "Fixed Jacket"),
#     OnshoreWell("Delta-03", 2800, 175, "Niger Delta", "Emeka Eze"),
#     OnshoreWell("Basin-04", 900, 310, "Benin Basin", "Fatima Bello"),
#     # lst1
# ]
#
# def run_inspection(wells):
#     print("=" * 50)
#     print("   DAILY RIG INSPECTION REPORT")
#     print("=" * 50)
#     for well in wells:
#         well.describe()
#         if well.is_critical():
#             print(f"  WARNING: {well.name} is in critical condition!")
#         if isinstance(well, OffshoreWell):
#             print(f"  Depth rating: {well.depth_rating()}")
#         print()
#
# run_inspection(mix2)
#
#
# class SubseaWell(OffshoreWell):
#     def __init__(self, name, pressure, temp, water_depth, platform_type, umbilical_length):
#         super().__init__(name, pressure, temp, water_depth, platform_type)
#         self.umbilical_length = umbilical_length
#
#     def describe(self):
#         print("Subsea Well:", self.name, "| Pressure:", self.pressure, "| Depth:", self.water_depth, "m | Umbilical:", self.umbilical_length, "m | Status:", self.status)
#
#
# sub = SubseaWell("Subsea-01", 3500, 185, 1600, "FPSO", 2500)
# mix2.append(sub)
#
#
# # Why didn't we need to change run_inspection() to support SubseaWell
# # Because run_inspection() just calls well.describe() on whatever it gets
# # SubseaWell has its own describe() so Python automatically calls the right one
# # This is polymorphism one function works on ALL types of wells
# # present and future without everchanging the function itself
#
#
# #task9
# task9_wells = [
#     OffshoreWell("Bonga-01", 3850, 185, 1200, "FPSO"),
#     OnshoreWell("Delta-01", 820, 165, "Niger Delta", "Tunde Adeyemi"),
#     SubseaWell("Subsea-01", 3500, 185, 1600, "FPSO", 2500),
#     OnshoreWell("Basin-02", 2100, 175, "Benin Basin", "Ngozi Okafor"),
# ]
#
# wells_as_dicts = []
# for well in task9_wells:
#     wells_as_dicts.append({
#         "name": well.name,
#         "pressure": well.pressure,
#         "temp": well.temp,
#         "status": well.status
#     })