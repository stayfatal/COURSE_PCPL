import random

def gen_random(amount:int,l:int,r:int):
    result = []
    for i in range(amount):
        result.append(random.randint(l,r))

    return result