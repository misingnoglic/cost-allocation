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

	cab1 = [(2,2), (1,1), (1,0) , (1,-1)]
	cab2 = [(3,1), (3,0), (3,-1) ]

	s = (2,2)
	d = (0,0)

	totaldist1 = range(n1)
	totaldist2 = range(n2)

	irDist1 = range(n1)
	irDist2 = range(n2)

	costd1 = range(n1)
	costd2 = range(n2)

	totalCost1 = range(n1)
	totalCost2 = range(n2) 

	# Define Alpha to be an Unsigned Int
	aplha = randint(1,10)

	## CAB 1 the OPTIMAL COST

	for  i in range(n1):
		if (i != n1):
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

	## CAB 2 the OPTIMAL COST

	for  i in range(n2):
		if (i != n2):
			dist = distance (cab2[i][0] , cab2[i][1] ,cab2[i+1][0],cab2[i+1][1])
			totaldist1[i] = dist / (i+1)
		else:
			dist = distance (cab2[i][0] ,  cab2[i][1] , d[0] ,d[1])
			totaldist1[i] = dist / (i+1)

	for i in range(n2):
		costd2[i] = costd2[i] + totaldist2[i]
		for j in range(i+1,n1):
			costd2[i] = costd2[i] + totaldist2[j]
			costd2[i] = alpha * costd2[i]

	# IR Cost for cab 1

	irDist1[0] = 0;

	for i in range(n1 -1):
		de1 = sqrt( (cab1[i][0] - cab1[i+1][0])**2 + (cab1[i][1] - cab1[i][1])**2 )
		de2 = sqrt( (cab1[i + 1][0] - d[0])**2  + (cab1[i + 1][1] - d[1])**2 )
		del[i] = sqrt( (cab1[i][0] - d[0])**2 + (cab1[i][1] - d[1])**2 )
		irDist1[i + 1] = alpha * (de1 + de2 - del[i])

	# IR Cost for cab 2
	irDist2[0] = 0;

	for i in range(n2 -1):
		de1 = sqrt((cab2[i].x - cab2[i+1].x) * (cab2[i].x - cab2[i+1].x) + (cab2[i].y - cab2[i].y) *(cab2[i].y - cab2[i + 1].y))
		de2 = sqrt((cab2[i + 1].x - d.x) * (cab2[i + 1].x - d.x) + (cab2[i + 1].y - d.y) * (cab2[i + 1].y - d.y))
		de2l[i] = sqrt((cab2[i].x - d.x) * (cab2[i].x - d.x) + (cab2[i].y - d.y) * (cab2[i].y - d.y))
		irDist2[i] = alpha * (de1 + de2 - de2l[i])


	for i in range(n1):
		if (i == 0):
			totalCost1[i] = costd1[i]
		else: 
			totalCost1[i] = costd1[i] + ( (i) * irDist1[i])
    

	for i in range(n2):
		if (i == 0): 
			totalCost2[i] = costd2[i]
		else:
			totalCost2[i] = costd2[i] + ( (i) * irDist2[i])


## ADD THE LP Code here 
######################################################################



#---------------------------------------------------------------------
 # Main Ends 
#----------

if __name__ == "__main__":
    main()
