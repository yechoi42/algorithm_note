#include <iostream>
#include <vector>

using namespace std;

int main(void)
{
    long long n;
    cin >> n;

    int i = 0;
    long long sum = 0;
    while (sum <= n)
    {
        i++;
        sum += i;
    }
    cout << i - 1 << '\n';

    return 0;
}