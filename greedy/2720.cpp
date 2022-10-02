#include <iostream>

using namespace std;

int main(void)
{
    int t;
    double c;
    int quarter;
    int dime;
    int nickel;
    int penny;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        quarter = dime = nickel = penny = 0;
        cin >> c;
        quarter = c / 25;
        c -= quarter * 25;
        dime = c / 10;
        c -= dime * 10;
        nickel = c / 5;
        c -= nickel * 5;
        penny = c / 1;
        cout << quarter << " " << dime << " " << nickel << " " << penny << "\n";
    }
    return 0;
}