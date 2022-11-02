#include <iostream>

using namespace std;

int main(void)
{
    int n;
    cin >> n;

    int share = n / 3;
    int remainder = n % 3;

    if ((share + remainder) / 2)
        cout << "SK" << endl;
    else
        cout << "CY" << endl;
    return 0;
}