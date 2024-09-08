
import math
import sys


def main():
    args = sys.argv
    equation=Equation()
    if len(args)==4:
        try:
            equation.a = int(sys.argv[1])
            equation.b = int(sys.argv[2])
            equation.c = int(sys.argv[3])
        except:
            print("incorrect input")
            sys.exit(1)
    else:
        while True:
            try:
                equation.a,equation.b,equation.c=map(int,input("Enter nums: ").split())
                break
            except:
                print("incorrect input")
    
    equation.calculateAndPrint()
            
class Equation:
    a:int
    b:int
    c:int
    
    def calculateAndPrint(self):
        d=int(math.pow(self.b,2))-4*self.a*self.c
        if d>0:
            print("Ans 1",(-float(self.b)-math.sqrt(d))/(2.0*float(self.a)))
            print("Ans 2",(-float(self.b)+math.sqrt(d))/(2*float(self.a)))
        elif d==0:
            print("Ans 1",float(self.b)/(2*float(self.a)))
        else:
            print("Discriminant < 0")

main()