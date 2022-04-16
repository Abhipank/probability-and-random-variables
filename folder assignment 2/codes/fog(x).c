#include <stdio.h>
float fog(float x)
{
    return 8*x*x*x*x*x*x+12*x*x*x*x+6*x*x+1;
}
int main()
{
FILE*ptr=fopen("fog(x).dat","w");
float i;

for(i=-6;i<=6;i+=0.01)
{
    fprintf(ptr,"%f %f\n",i,fog(i));
}
   fclose(ptr);
    return 0;
}
