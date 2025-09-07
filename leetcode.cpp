#include <iostream>
#include <vector>
using namespace std;
vector<int> sumZero(int n)
{
    vector<int> result(n);
    int i = n / 2 - 1;
    int j;
    if (n % 2 != 0)
    {
        j = i + 2;
    }
    else
    {
        j = i + 1;
    }
    int startNum = 1;
    while (j < n)
    {
        result[i] = -startNum;
        result[j] = startNum;
        startNum++;
        i--;
        j++;
    }
    return result;
}