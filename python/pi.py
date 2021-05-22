import random


def inside(x, y):
    return x**2 + y**2 < 1

def estimate(iterations):
    counter = 0
    #n = 1000000
    #for i in range(n):
    for _ in range(iterations):
        a = random.random()
        b = random.random()
        if inside(a,b):
            counter = counter + 1
    
    #print(f"Counter is {counter}")
    return (counter/iterations)*4

print(estimate(100000))


