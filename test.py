from pokemon import *
from battle import *
p = Pokemon()

p.isConfused = True
p.isParalysed = True
p.confuseCount = 2
print(checkCondition(p))