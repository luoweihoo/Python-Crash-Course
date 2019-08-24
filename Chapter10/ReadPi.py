# AUTHOR: Wei Luo
# FILE: C:\Users\Luo Wei\OneDrive\Python\Python-Crash-Course\ReadPi.py
# Contact: luoweihoo@yahoo.com
# DATE: 2019/08/24 Sat
# TIME: 14:45:44

# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
#     print(contents.rstrip())

# -----
# filename = 'pi_digits.txt'
# with open(filename) as file_object:
#     for line in file_object:
#         print(line.rstrip())

# -----
# filename = 'pi_million_digits.txt'
# with open(filename) as file_object:
#     lines = file_object.readlines()

# pi_string = ''
# for line in lines:
#     pi_string += line.strip()

# print(f"{pi_string[:52]}...")
# print(len(pi_string))

# -----
filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the format mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of PI!")
else:
    print("Your birthday does not appears in the first million digits of PI.")

