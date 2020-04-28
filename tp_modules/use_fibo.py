# from fibo import *
import sys
import lepackage.modulefibo
from lepackage import modulefibo
from lepackage.modulefibo import fib2

if __name__ == "__main__":
    
    if len(sys.argv) ==2:       
        value = int(sys.argv[-1])
        # result = lepackage.modulefibo.fib2(value)
        # result = modulefibo.fib2(value)
        result = fib2(value)
        print(f"result : {result}")

        a=2
        print(f"a : {a}")

    else:
        print("Merci de donner une valeur")
