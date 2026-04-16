import math

# is se circle ka area nikalta.
def circle_area(r):
    return math.pi * r * r  

# multiply krke rectangle ka area nikalta h.
def rectangle_area(w, h):
    return w * h

# loop chalta h agr koi num devide hojae to false warna true.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
