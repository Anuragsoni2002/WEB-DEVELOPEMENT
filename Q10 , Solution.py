"""
Write a python script to display the current date and time. First create variables to
store date and time, then display date and time in proper format (like: 13-8-2022 and
9:00 PM
"""
from datetime import datetime
dt=datetime.today()
print(dt)

d1=dt.strftime("%d-%m-%Y")
print(d1)

d2=dt.strftime("%d/%B/%Y")
print(d2)

d3=dt.strftime("%I:%M %p")
print(d3)

d4=dt.strftime("%H:%M:%S")
print(d4)

d5=dt.strftime("%d/%b/%y")
print(d5)

d6=dt.strftime("%I:%M:%S %p")
print(d6)