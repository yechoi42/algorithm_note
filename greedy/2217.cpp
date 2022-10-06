#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(void)
{
    int n, tmp;
    cin >> n;

    vector<int> arr(n);
    for (int i = 0; i < n; i++)
    {
        cin >> tmp;
        arr[i] = tmp;
    }
    sort(arr.begin(), arr.end());
    int result = 0;
    int sum;
    for (int i = 0; i < n; i++)
    {
        sum = arr[i] * (n - i);
        if (sum > result)
            result = sum;
    }
    cout << result << '\n';
    return 0;
}