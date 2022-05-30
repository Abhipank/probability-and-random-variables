#include <stdio.h>
#include<math.h>
float f(float z)
{
    if(z<1)
    return 2*z-2-2*log(z);
    else return 0;
    
}


int main()
{   float i;
   FILE*ptr=fopen("pdef.log","w");
   
   for(i=0.1;i<=6;i+=0.01)
   {
       fprintf(ptr,"%f %f\n",i,f(i));
   }
   fclose(ptr);
    return 0;
}
