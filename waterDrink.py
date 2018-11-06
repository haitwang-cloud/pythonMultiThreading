"""
bottle为空瓶数目，gap为瓶盖数据，drink为第一次买到的饮料数目
"""


def drinkWater(bottle, gap, drink):
    if bottle < 4 and gap < 2:
        return drink
    counter = gap//2+bottle//4
    drink += counter
    bottle = counter+bottle % 4
    gap = counter+gap % 2
    return drinkWater(bottle,gap,drink)

print("sum=",drinkWater(10,10,10))
