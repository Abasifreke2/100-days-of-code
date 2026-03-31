#The code exceeded the range of index
from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)#it should be 5 not 6
print(dice_images[dice_num])
