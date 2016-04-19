import math
from random import randint



def main():

	C1 = True
        z = randint(1,10)
        r = randint(1,10)
        x  = z + 2
        y  = r + 2

        C1 = C1 and (x >= y)
        assert  C1

        print(x)
        print(y)



if __name__ == "__main__":
    main()
