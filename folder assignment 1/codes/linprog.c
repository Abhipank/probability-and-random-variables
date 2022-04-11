/*here A is line 1 :11x-4=y ,B is line 2:15x-y=4 and C is line 3:13x-y=14*/
#include <stdio.h>

struct matrix{
    float x;
    float y;
};

struct matrix feedmatrix(float a,float b )
{
    struct matrix temp;
    temp.x=a;
    temp.y=b;
    return temp;
}

struct matrix solve(struct matrix m,struct matrix n,int c1,int c2)
{
    struct matrix temp;
    
    
    temp.x=((m.y)*c2 -(n.y)*c1)/((m.x)*(n.y)-(n.x)*(m.y));
    
    temp.y=((m.x)*c2 -(n.x)*c1)/((m.x)*(n.y)-(n.x)*(m.y));

return temp;
}

int main()
{
struct matrix A=feedmatrix(11,-1);


struct matrix B=feedmatrix(15,-1);


struct matrix C=feedmatrix(13,-1);


struct matrix intersec1,intersec2;

intersec1=solve(A,B,-4,4);


intersec2=solve(B,C,4,14);

printf("intersection1 is intersection of lines 1 and 2 : (%f,%f)",intersec1.x,intersec1.y);
printf("\n");

printf("intersection2 is intersection of lines 2 and 3  : (%f,%f)",intersec2.x,intersec2.y);


    return 0;
}
