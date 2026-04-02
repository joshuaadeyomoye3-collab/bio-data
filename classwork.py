#task 1
print("Welcome to the Oil Field Data Processing System")
well_name = input("well name:")
report = input("Enter well report (e.g. WellA-1500, WellB-2000, WellC-1750): ")
well_iD = input("Well iD: ")
well_location = input("Well location:")
barrels = input("Barrels:")
date = input ('date:')

#task 2
cleaned = report.lower().replace ("-" ":")
print(f"Cleaned report: {cleaned}")
#task 3
wells = cleaned.split(",")
print(f"Individual wells: {wells}")

