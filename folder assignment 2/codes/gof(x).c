#include <stdio.h>
float gof(float x)
{
    return 2*x*x*x*x*x*x+1;
}
int main()
{
FILE*ptr=fopen("gof(x).dat","w");
float i;

for(i=-6;i<=6;i+=0.01)
{
    fprintf(ptr,"%f %f\n",i,gof(i));
}
   fclose(ptr);
    return 0;
}
