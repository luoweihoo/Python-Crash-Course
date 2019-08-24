# AUTHOR: Wei Luo
# FILE: C:\Users\Luo Wei\OneDrive\Python\Python-Crash-Course\ReadPi.py
# Contact: luoweihoo@yahoo.com
# DATE: 2019/08/24 Sat
# TIME: 14:45:44

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

