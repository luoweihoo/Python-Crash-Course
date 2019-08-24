# @File    :   alice.py
# @Time    :   2019/08/24 16:25:59
# @Author  :   Wei Luo 
# @Version :   1.0
# @Contact :   luoweihoo@yahoo.com
# @Desc    :   None

filename = 'alice.txt'

try:
    with open(filename, encoding = 'utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    # Count the approximate number of words in the file
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")




