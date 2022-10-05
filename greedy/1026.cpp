#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void)
{
    int n;
    int tmp;

    cin >> n;
    vector<int> array_a(n);
    vector<int> array_b(n);
    for (int i = 0; i < n; i++)
    {
        cin >> tmp;
        array_a[i] = tmp;
    }
    for (int i = 0; i < n; i++)
    {
        cin >> tmp;
        array_b[i] = tmp;
    }
    sort(array_a.begin(), array_a.end());
    sort(array_b.begin(), array_b.end(), greater<int>());

    int sum = 0;
    for (int i = 0; i < n; i++)
    {
        sum += array_a[i] * array_b[i];
    }
    cout << sum << '\n';
    return 0;
}