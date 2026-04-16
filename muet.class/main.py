from math_helpers import circle_area, rectangle_area, is_prime

# circle_area
r = 5
print(f"Circle area (r={r}): {circle_area(r):.2f}")

# rectangle_area
w, h = 4, 6
print(f"Rectangle area (w={w}, h={h}): {rectangle_area(w, h)}")

# is_prime
for n in [2, 7, 10, 13, 25]:
    print(f"is_prime({n}): {is_prime(n)}")
