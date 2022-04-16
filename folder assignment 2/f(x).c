#include <stdio.h>
float f(float x)
{
    return x*x*x;
}
int main()
{
FILE*ptr=fopen("f(x).dat","w");
float i;

for(i=-6;i<=6;i+=0.01)
{
    fprintf(ptr,"(%f,%f)\n",i,f(i));
}
   fclose(ptr);
    return 0;
}
