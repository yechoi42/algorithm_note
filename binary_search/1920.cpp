#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int binary_search(vector<int> &array, int target, int start, int end)
{
    if (start > end)
        return 0;
    int mid; 
    mid = (start + end) / 2;
    if (array[mid] == target)
        return 1;
    else if (array[mid] > target)
        return binary_search(array, target, start, mid - 1);
    else
        return binary_search(array, target, mid + 1, end);
}

int main(void)
{
    ios_base::sync_with_stdio(0); 
    cin.tie(0);
    int n;
    cin >> n;

    vector<int> numbers(n);
    int temp;
    for (int i = 0; i < n ; i++)
    {
        cin >> temp; 
        numbers[i] = temp;
    }
    sort(numbers.begin(), numbers.end());

    int m;
    cin >> m;
    vector<int> targets(m);
    for (int j = 0; j < m ; j++)
    {
        cin >> temp; 
        cout << binary_search(numbers, temp, 0, n - 1) << '\n';
    }
    return 0;
}