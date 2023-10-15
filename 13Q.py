# find the roots of the quadratic equation 
import math

def find_quadratic_roots(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (root1, root2)
    elif discriminant == 0:
        root = -b / (2*a)
        return root,
    else:
        # Complex roots (no real solutions)
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
        return (real_part + imaginary_part * 1j, real_part - imaginary_part * 1j)

# Input coefficients
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

roots = find_quadratic_roots(a, b, c)

print("Roots of the quadratic equation:")
for root in roots:
    print(root)
