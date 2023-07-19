# bounce.py
#
# Exercise 1.5

height = 100 # (meters)
count = 0

while count < 10:
    height = height * 0.6
    count = count + 1
    print(round(height, ndigits=4))
