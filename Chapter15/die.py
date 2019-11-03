# @File    :   die.py
# @Time    :   2019/11/03 11:47:27
# @Author  :   Wei Luo
# @Version :   1.0
# @Contact :   luoweihoo@yahoo.com
# @Desc    :   None

from random import randint

class Die:
    """A class represting a single die"""

    def __init__(self, num_sides = 6):
        """Assume a six-sided die"""
        self.num_sides = num_sides

    def roll(self):
        """Return a random value between 1 and number of sides"""
        return randint(1, self.num_sides)