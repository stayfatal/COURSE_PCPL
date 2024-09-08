import sys
import math

def main():
    args = sys.argv
    a:int
    b:int
    c:int
    if len(args)==4:
        try:
            a = int(sys.argv[1])
            b = int(sys.argv[2])
            c = int(sys.argv[3])
        except:
            print("incorrect input")
            sys.exit(1)
    else:
        while True:
            try:
                a,b,c=map(int,input("Enter nums: ").split())
                break
            except:
                print("incorrect input")
        
            
    calculateAndPrintEquation(a,b,c)
    
def calculateAndPrintEquation(a:int,b:int,c:int):
    d=int(math.pow(b,2))-4*a*c
    if d>0:
        print("Ans 1",(-float(b)-math.sqrt(d))/(2.0*float(a)))
        print("Ans 2",(-float(b)+math.sqrt(d))/(2*float(a)))
    elif d==0:
        print("Ans 1",float(b)/(2*float(a)))
    else:
        print("Discriminant < 0")

main()