import math
from random import randint

def distance(x1,y1,x2,y2):
	return math.hypot(x2 - x1, y2 - y1)


#--------------------------------------------------------------------
#     Main starts
# --------------------------------------------------------------------

def main():
    x = distance(2,2, 1,1)
    print(x)




#---------------------------------------------------------------------
 # Main Ends
#----------

if __name__ == "__main__":
    main()
