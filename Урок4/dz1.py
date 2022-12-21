# Вычислить число Пи c заданной точностью d

# *Пример:* 
# - при d = 0.001, π = 3.141
# - при d = 0.0001, π = 3.1415 

from math import pi

def format(num: float, accuracy: float) -> float:
    accuracy = str (accuracy)
    accuracy = len (accuracy[accuracy.find('.')+1::])
    print(accuracy)
    return float(f'{pi:0.{accuracy}f}')

d=input('Введите точность в формате "0.001": ')
print(format(pi, d)) 