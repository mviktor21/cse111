import math

from datetime import datetime

print("This program will calculate the width, the ratio and the diameter of a tire")

pi=3.14285714286
width = float(input("Enter the width of the tire in mm (ex 205): "))
ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

current_date_and_time = datetime.now()
print(f"{current_date_and_time:%Y-%m-%d}")

volume = math.pi*ratio*ratio*width
print("The approximate volume is = "+str(volume)+" liters")

with open("volumes.txt", "at") as volumes:
    print(volumes, file=volumes)
    print(f"{current_date_and_time}, {volume}", file=volumes)

    # Not sure how to convert or reduce the floating number.