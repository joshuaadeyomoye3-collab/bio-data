# #task 1
# def greet_engineer(name):
#     print("Good morning " + name ,"" + "Ready to monitor the rig?")
# greet_engineer("emeka")
# greet_engineer("joshua")
#
# def rig_status(well_name ,is_active  ):
#     if is_active:
#         print(well_name + "is Online")
#     else:
#         print(well_name + "is Offline— maintenance required ")
#
# rig_status("zlatan-02 ", True)
# rig_status("Konga-09 ", False)
# rig_status("Ogbafia-06 ", True)
#
# def calculate_daily_output(flow_rate, hours_active):
#     return flow_rate * hours_active
# print(f"daily_output:{ calculate_daily_output(50, 24)}")
#
# print(calculate_daily_output(80, 18))
# print(calculate_daily_output(120, 12))
# print(calculate_daily_output(120, 12))
#
# #taskb
# def classify_pressure(pressure):
#     if pressure < 1000:
#         return "CRITICAL"
#     elif pressure < 2500:
#         return "LOW"
#     elif pressure < 4500:
#         return "NORMAL"
#     elif pressure >= 4500:
#         return "OVERPRESSURE"
#     else:
#         return "invalid"
#
# print(classify_pressure(650))
# print(classify_pressure(1500))
# print(classify_pressure(3850))
# print(classify_pressure(4600))
#
# def maintenance_due(days_since_service):
#     if days_since_service > 90:
#         return "Overdue"
#     elif days_since_service > 60:
#         return "Due soon"
#     else:
#         return "OK"
# print(maintenance_due(30))
# print(maintenance_due(50))
# print(maintenance_due(80))
#
# def access_level(role):
#     match role:
#         case "supervisor":
#             return "Full access"
#         case "engineer":
#             return "Operational access"
#         case "contractor":
#             return "Limited access"
#         case _:
#             return "No access"
# print(access_level("supervisor"))
# print(access_level("engineer"))
# print(access_level("contractor"))
# print(access_level("jimoh"))
#
# #taskc
# wells = [
#     {"name": "Bonga-01",  "pressure": 3850},
#     {"name": "Bonga-03",  "pressure": 820},
#     {"name": "Erha-02",   "pressure": 4600},
#     {"name": "Erha-05",   "pressure": 3200},
#     {"name": "Agbami-02", "pressure": 650},
# ]
# def check_all_wells(wells):
#     for well in wells:
#         status = classify_pressure(well["pressure"])
#         print(well["name"], "|", well["pressure"], "psi", "|", status)
#
# check_all_wells(wells)
#
# def count_critical(wells):
#     count = 0
#     for well in wells:
#         if classify_pressure(well["pressure"]) == "CRITICAL":
#             count += 1
#     return count
#
# critical_total = count_critical(wells)
# print(critical_total, "well(s) are in CRITICAL condition")
#
# def pressure_monitor():
#     while True:
#         reading = int(input("Enter pressure reading (or 0 to quit): "))
#         if reading == 0:
#             break
#         status = classify_pressure(reading)
#         print("Status:", status)
#
# pressure_monitor()
#
# #taskd
# def run_daily_check(wells):
#     total_checked = 0
#     critical_count = 0
#     maintenance_count = 0
#
#     for well in wells:
#         if well["pressure"] == 0:
#             continue
#
#         status = classify_pressure(well["pressure"])
#
#         maintenance = maintenance_due(45)
#
#         if status == "CRITICAL":
#             critical_count += 1
#
#         if maintenance != "OK":
#             maintenance_count += 1
#
#         total_checked += 1
#
#         print(well["name"], "|", status, "| Maintenance:", maintenance)
#
#     print("─" * 45)
#     print("Total wells checked:", total_checked)
#     print("Critical wells:", critical_count)
#     print("Wells needing maintenance:", maintenance_count)
#     print("─" * 45)
#
# run_daily_check(wells)


# def add_greetings(func):
#     def inner(name):
#         return "good morning," + func(name)
#     return inner
#
# @add_greetings
# def greetings(name):
#     return name
#
# print(greetings("BALO"))
#
# 1
def add10(a):
    return a + 10
print(add10(5))
# 2
def sub5(a):
    return a - 5
print(sub5(20))
# 3
def mul3(a):
    return a * 3
print(mul3(4))
# 4
def dvd(a):
    return a / 2
print(dvd(10))
# 5
def sqr(a):
    return a ** 2
print(sqr(6))
# 6
def cube(a):
    return a ** 3
print(cube(3))
#7
def doubler(a):
    return a * 2
print(doubler(7))

# 8
def remainder(a):
    return a % 4
print(remainder(17))

# 9
def add_one_hundred(number):
    return number + 100
print(add_one_hundred(50))

# 10
def negative(number):
    return number * -1
print(negative(9))

# 11
def add_numbers(a, b):
    return a + b
print(add_numbers(3, 7))

# 12
def sub_numbers(a, b):
    return a - b
print(sub_numbers(15, 4))

# 13
def multiply(a, b):
    return a * b
print(multiply(6, 5))

# 14
def divide(a, b):
    return a / b
print(divide(20, 4))

# 15
def get_largest_number(num1, num2):
    if num1 > num2:
        return num1
    else: num1 < num2
    return num2
print(get_largest_number(8,12))

# 16
def get_smallest_number(num1, num2):
    if num1 < num2:
        return num1
    else: num1 > num2
    return num2
print(get_smallest_number(8, 12))

# 17
def get_average(num1, num2):
    return (num1 + num2) / 2
print(get_average(10, 20))

# 18
def raiser(num1, num2):
    return (num1**num2)
print(raiser(2, 8))

# 19
def sum_squares(num1, num2):
    return (num1**2 + num2**2)
print(sum_squares(3, 4))

# 20
def correct(num1, num2):
    if num1 > num2:
        return True
print(correct(10,5))

# 21
def add_numbers(a, b, c):
    return a + b + c
print(add_numbers(5, 6, 2))

# 22
def multiply(a, b, c):
    return a * b * c
print(multiply(2, 3, 4))

# 23
def get_largest_number(num1, num2, num3):
    if num2 > num1 and num3:
        return num2
print(get_largest_number(10, 25, 18))

# 24
def get_average(num1, num2, num3):
    return (num1 + num2 + num3) / 3
print(get_average(10, 20, 30))

# 25
def all_equals(num1, num2, num3):
    if num1 == num2 and num2 == num3:
        return True

print(all_equals(5, 5, 5))

