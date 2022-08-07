#include <iostream>
using namespace std;
#define MAX_LENGTH 20

int main(int argc, char *argv[])
{
    // make an arry of integers and fill it with values
    int array[MAX_LENGTH] = {1, 2, 3, 4, 5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20};
    
    //size of the array
    //int size = sizeof(array) / sizeof(array[0]);

    //cout<<size<<endl;
    cout<<"[";
    for (int i = 0; i < MAX_LENGTH; i++)
    {        
        cout << array[i] ;
        if (i < MAX_LENGTH-1)
        {
            cout << ",";
        }

    }
    cout << "]" ;
    return 0;
}
