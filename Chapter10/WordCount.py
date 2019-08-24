# @File    :   WordCount.py
# @Time    :   2019/08/24 16:45:28
# @Author  :   Wei Luo 
# @Version :   1.0
# @Contact :   luoweihoo@yahoo.com
# @Desc    :   None

def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding = 'utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file{filename} doesn't exist. ")
    else:    
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'liitle_women.txt']
for filename in filenames:
    count_words(filename)

