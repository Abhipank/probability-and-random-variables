#include<stdio.h>
#include<stdlib.h>
#include<math.h>

#include"coeffs.h"




int main()
{ double x;
x=mean("gau.dat");
   printf("mean=%lf\n",x);
printf("variance=%lf\n",variance("gau.dat"));

}
