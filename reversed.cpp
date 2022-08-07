#include <iostream>
using namespace std;

int main(int argc, char){
    //Given a random non-negative number,
    // you have to return the digits of this number within an array in reverse order.
    // Example(Input => Output):
    //348597 => [7,9,5,8,4,3]
    //0 => [0]

    int number = 348597;
    int size = sizeof(number) / sizeof(number[0]);
    int array[size];
    int i = 0;
    while (number > 0)
    {
        array[i] = number % 10;
        number = number / 10;
        i++;
    }
    cout << "[";
    for (int j = i - 1; j >= 0; j--)
    {
        cout << array[j];
        if (j > 0)
        {
            cout << ",";
        }
    }


}