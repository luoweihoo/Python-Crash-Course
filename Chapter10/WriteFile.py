# @File    :   WriteFile.py
# @Time    :   2019/08/24 15:49:07
# @Author  :   Wei Luo 
# @Version :   1.0
# @Contact :   luoweihoo@yahoo.com
# @Desc    :   None

filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write('I love programming. \n')
    file_object.write('I love creating new games.\n')

    