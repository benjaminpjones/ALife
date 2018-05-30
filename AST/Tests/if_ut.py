# if/orelse

import random
x = random.randint(2,100)

while x != 1:
    if x%2 == 0:
        x /= 2
    elif x%2 == 1:
        x = x*3
    else:
        x = 1
