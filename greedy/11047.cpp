#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void)
{
    int n, k;
    cin >> n >> k;

    vector<int> coins(n);
    int temp;
    for (int i = 0; i < n; i++)
    {
        cin >> temp;
        coins[i] = temp;
    }
    sort(coins.begin(), coins.end());

    int count = 0;
    for (int i = n - 1; i >= 0; i--)
    {
        temp = k / coins[i];
        count += temp;
        k -= temp * coins[i];
    }
    cout << count << '\n';
    return 0;
}