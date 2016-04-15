/* Basic Constraint solving for the cost allocation puyput
*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define C 2   // Total cabs  
#define N 7  // Numbr of cutomers
#define n1 4  // Numberof sutomers in ith Cab
#define n2 3  // Number of cutimers in jth cab

_Bool nondet_bool();
unsigned int nondet_uint();

//typedef unsigned __CPROVER_bitvector[M] bitvector; 

unsigned int  nondet (){  
  unsigned int num = nondet_uint();
  __CPROVER_assume( num>= 0 && num  <= 1);
   return num;
};


struct EdgeBag
 {
   unsigned int num ;
    int x;
    int  y;
   unsigned int costshare;
};

struct Start 
{
    int x;
    int y;
};


int  main()

 {    

     _Bool C1,C2;
    unsigned int  i , j , k, l , mi , alpha ;
    double totald1[n1] , totald2[n2] = {} , irDist1[n1] = {}, irDist2[n2] = {}, costd1[n1]  = {} , costd2[n2] = {};
    double totalCost1[n1] , totalCost2[n2];
    int source1, source2, dest1 , dest2;
    unsigned int edgeCount = 0;
    double distance , totaldistance1 = 0, totaldistance2 = 0 , finalDistance = 0 , de1 = 0 , de2 = 0, del[n1] = {}, de2l[n2] = {};
    
    struct EdgeBag cab1[n1]; // pass the argument to this as the total number of customers there
    struct EdgeBag cab2[n2];  // same 
    
    struct Start s;  // create a starting point pair 
    struct Start d;  // create a destination pair

    /* Long Input */

    cab1[0].x = 2;
    cab1[1].x = 1;
    cab1[2].x = 1;
    cab1[3].x = 1;
    
    cab1[0].y = 2;
    cab1[1].y = 1;
    cab1[2].y = 0;
    cab1[3].y = -1;

    cab2[0].x = 3;
    cab2[0].x = 3;
    cab2[0].x = 3;
  

    cab2[0].y = 1;
    cab2[1].y = 0;
    cab2[2].y = -1;

    d.x = 0;
    d.y = 0;

    /* Optimal Cost
     *
 *-----------------------------------------
 *
 * */

// For the cab 1 

   for ( i = 0; i < n1 ; i++) {
     
       if (i != n1 ) {
           distance = sqrt((cab1[i].x - cab1[i+1].x) * (cab1[i].x - cab1[i+1].x) + (cab1[i].y - cab1[i].y) *(cab1[i].y - cab1[i + 1].y));
           totald1[i] = distance / (i + 1);
        }

       else {
           distance = sqrt((cab1[i].x - d.x) * (cab1[i].x - d.x) + (cab1[i].y - d.y) * (cab1[i].y - d.y));
           totald1[i] = distance / (i + 1);
       }

   }

    for ( i = 0; i < n1 ; i++) {
            costd1[i] +=  totald1[i];
        for ( j = i + 1; j < n1 ; j++) { 
            costd1[i] +=  totald1[j];
        }

        costd1[i] *=  alpha;
    }

  
// For the cab 2
    for ( i = 0; i < n2 ; i++) {
      

       if (i != (n2 - 1)) {
           distance = sqrt((cab2[i].x - cab2[i+1].x) * (cab2[i].x - cab2[i+1].x) + (cab2[i].y - cab2[i].y) *(cab2[i].y - cab2[i + 1].y));
           totald2[i] = distance / (i + 1);
        }

       else {
           distance = sqrt((cab2[i].x - d.x) * (cab2[i].x - d.x) + (cab2[i].y - d.y) * (cab2[i].y - d.y));
           totald2[i] = distance / (i + 1);
       }

   }
  


 for ( i = 0; i < n1 ; i++) {
            costd2[i] +=  totald2[i];
        for ( j = i + 1; j < n1 ; j++) { 
            costd2[i] +=  totald2[j];
        }

        costd2[i] *=  alpha;
    }

 /* Optimal Cost Ends */

   irDist1[0] = 0;
   irDist2[0] = 0;
   
for ( i = 0; i < (n1 - 1); i++) {
         de1 = sqrt((cab1[i].x - cab1[i+1].x) * (cab1[i].x - cab1[i+1].x) + (cab1[i].y - cab1[i].y) *(cab1[i].y - cab1[i + 1].y));
           de2 = sqrt((cab1[i + 1].x - d.x) * (cab1[i + 1].x - d.x) + (cab1[i + 1].y - d.y) * (cab1[i + 1].y - d.y));
           del[i] = sqrt((cab1[i].x - d.x) * (cab1[i].x - d.x) + (cab1[i].y - d.y) * (cab1[i].y - d.y));
           irDist1[i + 1] = alpha * (de1 + de2 - del[i]); 


   }

   for ( i = 0; i < (n2 - 1); i++) {
      
           de1 = sqrt((cab2[i].x - cab2[i+1].x) * (cab2[i].x - cab2[i+1].x) + (cab2[i].y - cab2[i].y) *(cab2[i].y - cab2[i + 1].y));
           de2 = sqrt((cab2[i + 1].x - d.x) * (cab2[i + 1].x - d.x) + (cab2[i + 1].y - d.y) * (cab2[i + 1].y - d.y));
           de2l[i] = sqrt((cab2[i].x - d.x) * (cab2[i].x - d.x) + (cab2[i].y - d.y) * (cab2[i].y - d.y));
           irDist2[i] = alpha * (de1 + de2 - de2l[i]); 
          
      }

/* IR completes  */

for (i = 0; i < n1; i++) {
    if (i == 0) {
        totalCost1[i] = costd1[i];
    }
    else {
        totalCost1[i] = costd1[i] + ( (i) * irDist1[i]);
    }
}

for (i = 0; i < n2 ; i++) {
    if (i == 0) {
        totalCost2[i] = costd2[i];
    }
    else {
        totalCost2[i] = costd2[i] + ( (i) * irDist2[i]);
    }
}

C1 = 1;

// Sir Constrints 
for ( i=0;i<n1;i++) {
        C1 = (C1 && (del[i] >= costd1[i]));
}

for ( i=0;i<n1;i++) {
    C2 = (C2 && (de2l[i] >= costd2[i])) ;
 }

__CPROVER_assert(!(C1 && C2) , "Cost distribution exists for the current path");  
 
}

