import sys
import math

def main():
    args = sys.argv
    a: int
    b: int
    c: int
    if len(args) == 4:
        try:
            a = int(sys.argv[1])
            b = int(sys.argv[2])
            c = int(sys.argv[3])
        except ValueError:
            print("Incorrect input")
            sys.exit(1)
    else:
        while True:
            try:
                a, b, c = map(int, input("Enter coefficients a, b, c: ").split())
                break
            except ValueError:
                print("Incorrect input")

    calculate_and_print_roots(a, b, c)

def calculate_and_print_roots(a: int, b: int, c: int):
    discriminant = b**2 - 4 * a * c
    
    if discriminant > 0:
        t1 = (-b - math.sqrt(discriminant)) / (2 * a)
        t2 = (-b + math.sqrt(discriminant)) / (2 * a)
        
        roots = []
        
        if t1 >= 0:
            roots.extend([math.sqrt(t1), -math.sqrt(t1)])
        if t2 >= 0:
            roots.extend([math.sqrt(t2), -math.sqrt(t2)])
        
        if roots:
            print("Roots:", *sorted(set(roots)))
        else:
            print("No real roots")
    
    elif discriminant == 0:
        t = -b / (2 * a)
        
        if t >= 0:
            print("Roots:", math.sqrt(t), -math.sqrt(t))
        else:
            print("No real roots")
    
    else:
        print("Discriminant < 0, no real roots")

main()
