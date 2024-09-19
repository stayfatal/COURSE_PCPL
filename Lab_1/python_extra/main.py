import math
import sys

def main():
    args = sys.argv
    equation = Equation()
    if len(args) == 4:
        try:
            equation.a = int(sys.argv[1])
            equation.b = int(sys.argv[2])
            equation.c = int(sys.argv[3])
        except ValueError:
            print("Incorrect input")
            sys.exit(1)
    else:
        while True:
            try:
                equation.a, equation.b, equation.c = map(int, input("Enter coefficients a, b, c: ").split())
                break
            except ValueError:
                print("Incorrect input")
    
    equation.calculate_and_print()
            
class Equation:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0
    
    def calculate_and_print(self):
        discriminant = self.b**2 - 4 * self.a * self.c
        
        if discriminant > 0:
            t1 = (-self.b - math.sqrt(discriminant)) / (2 * self.a)
            t2 = (-self.b + math.sqrt(discriminant)) / (2 * self.a)
            
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
            t = -self.b / (2 * self.a)
            
            if t >= 0:
                print("Roots:", math.sqrt(t), -math.sqrt(t))
            else:
                print("No real roots")
        
        else:
            print("Discriminant < 0, no real roots")

main()
