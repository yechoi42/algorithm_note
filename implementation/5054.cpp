#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(void)
{
    int t;
    cin >> t;
    for (int i = 0; i < t ; i++)
    {
        int n;
        cin >> n;
        vector<int> shops;
        int temp;
        for (int j = 0; j < n ; j++)
        {
            cin >> temp;
            shops.push_back(temp);
        }
        sort(shops.begin(), shops.end());
        cout << (shops[n - 1] - shops[0]) * 2 << endl;
    }
}