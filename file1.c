#include<stdio.h>
#include <time.h>
#include <stdlib.h>


_Bool nondet_bool();

void main() {
    unsigned int x , y;
    unsigned int c , n;
    _Bool C1,C2;

 // Similar Code Like random :
   C2 = 1;
   srand(time(NULL));
   unsigned int r = rand();
   unsigned int s = rand();

   C2 = C2 && (s >= r);
 
   // What I wanted to get / achieve really
    x  = c + 2;
    y  = n + 2;
    
    C1  = 1;
    C1 = C1 && (x >= y);
  
    __CPROVER_assert(!(C1 && C2), "cond satisfies");
}


