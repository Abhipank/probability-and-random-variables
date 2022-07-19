
#include <iostream>
using namespace std;
#include<vector>

void solve(char str[],vector<char> output,int index)
{
    int j;
    if(index>=3)
    { cout<<"{";
        for(j=0;j<output.size();j++)
        {
            cout<<output[j]<<" ";
        }
        cout<<"}";
        cout<<endl;
        return;
    }
    
    
    index=index+1;
    solve(str,output,index);
    
    output.push_back(str[index-1]);
    solve(str,output,index);
}



int main() 
{
vector<char> output;
char str[3]={'1','2','3'};

int index=0;

solve(str,output,index);




	return 0;
}
