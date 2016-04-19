import math
from random import randint

def distance(x1,y1,x2,y2):
	return math.hypot(x2 - x1, y2 - y1)


#--------------------------------------------------------------------
#     Main starts
# --------------------------------------------------------------------

def main():

	cabs = 2
	n1 = 4
	n2 = 3
	C1 = True
	C2 = True

	cab1 = [(2,2), (1,1), (1,0) , (1,-1)]
	cab2 = [(3,1), (3,0), (3,-1)]

	d = (2,0)

	totaldist1 = [0 for x in range(n1)]
	totaldist2 = [0 for x in range(n2)]


	irDist1 = [0 for x in range(n1)]
	irDist2 = [0 for x in range(n2)]


	costd1 = [0 for x in range(n1)]
	costd2 = [0 for x in range(n2)]


	totalCost1 = [0 for x in range(n1)]
	totalCost2 = [0 for x in range(n2)]


	dell = 	[0 for x in range(n1)]
	de2l = 	[0 for x in range(n2)]

        print(dell)
        print(de2l)

	# Define Alpha to be an Unsigned Int
	alpha = randint(1,10)

	## CAB 1 the OPPERATIONAL COST

	for  i in range(n1):
		if (i != (n1 - 1) ):
			dist = distance (cab1[i][0] , cab1[i][1] ,cab1[i+1][0],cab1[i+1][1])
			totaldist1[i] = dist / (i+1)
		else:
			dist = distance (cab1[i][0] ,  cab1[i][1] , d[0] ,d[1])
			totaldist1[i] = dist / (i+1)

	for i in range(n1):
		costd1[i] = costd1[i] + totaldist1[i]
		for j in range(i+1,n1):
			costd1[i] = costd1[i] + totaldist1[j]
		costd1[i] = alpha * costd1[i]

	## CAB 2 the OPERATIONAL COST

	for  i in range(n2):
		if (i != (n2 - 1)):
			dist = distance (cab2[i][0] , cab2[i][1] ,cab2[i+1][0],cab2[i+1][1])
			totaldist2[i] = dist / (i+1)
		else:
			dist = distance (cab2[i][0] ,  cab2[i][1] , d[0], d[1])
			totaldist2[i] = dist / (i+1)

	for i in range(n2):
		costd2[i] = costd2[i] + totaldist2[i]
		for j in range(i+1,n2):
			costd2[i] = costd2[i] + totaldist2[j]
		costd2[i] = alpha * costd2[i]

	# IR Cost for cab 1

	irDist1[0] = 0;

	for i in range(n1 -1):
		de1 = distance( cab1[i][0] ,cab1[i][1], cab1[i+1][0],cab1[i+1][1])
		de2 = distance ( cab1[i + 1][0], cab1[i + 1][1] , d[0] ,d[1])
		dell[i] = distance( cab1[i][0] , cab1[i][1] , d[0] , d[1])
		irDist1[i + 1] = alpha * (de1 + de2 - dell[i])
    
    dell[n1-1] = distance(cab1[n1-1][0] , cab1[n1-1][1] , d[0],d[1])
	# IR Cost for cab 2
	irDist2[0] = 0;

	for i in range(n2 -1):
		de1 = distance( cab2[i][0] ,cab2[i][1], cab2[i+1][0],cab2[i+1][1])
		de2 = distance ( cab2[i + 1][0], cab2[i + 1][1] , d[0] ,d[1])
		de2l[i] = distance( cab2[i][0] , cab2[i][1] , d[0] , d[1])
		irDist2[i + 1] = alpha * (de1 + de2 - de2l[i])
    
    de2l[n2-1] = distance(cab2[n2-1][0] , cab2[n2-1][1] , d[0],d[1])


	for i in range(n1):
		if (i == 0):
			totalCost1[i] = costd1[i]
		else:
			totalCost1[i] = costd1[i] + ( i * irDist1[i])


	for i in range(n2):
		if (i == 0):
			totalCost2[i] = costd2[i]
		else:
			totalCost2[i] = costd2[i] + ( i * irDist2[i])

## ADD THE LP Code here  : # Sir Constrints
	for i in range(n1):
		C1 = C1 and ((alpha * dell[i]) >= totalCost1[i])

	for i in range(n2):
		C2 = C2 and  ((alpha * de2l[i]) >= totalCost2[i])

        assert   C1
        #assert  not C2

        for i in range(n1):
		print("cost of the first taxi person ", i , totalCost1[i])
                print(dell[i])
		print(" Alone have to pay " , (dell[i] * alpha))
		print("")

        for i in range(n2):
		print("cost of the first taxi person ", i , totalCost2[i])
                print(de2l[i])
		print(" Alone have to pay " , (de2l[i] * alpha))
		print("")

	print(alpha)

#---------------------------------------------------------------------
 # Main Ends
#----------

if __name__ == "__main__":
    main()
