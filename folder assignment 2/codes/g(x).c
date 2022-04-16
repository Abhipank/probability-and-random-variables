#include <stdio.h>
float g(float x)
{
    return 2*x*x+1;
}
int main()
{
FILE*ptr=fopen("g(x).dat","w");
float i;

for(i=-6;i<=6;i+=0.01)
{
    fprintf(ptr,"%f %f\n",i,g(i));
}
   fclose(ptr);
    return 0;
}
