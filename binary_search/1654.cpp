#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;


int main(void)
{
    ios_base::sync_with_stdio(0); 
    cin.tie(0);
    int n, m;
    cin >> n >> m;

    vector<long long> trees(n);
    long long temp;
    for (int i = 0; i < n ; i++)
    {
        cin >> temp; 
        trees[i] = temp;
    }
    sort(trees.begin(), trees.end());

    long long start, end;
    start = 1;
    end = trees[n - 1];

    while (start <= end)
    {
        long long mid = (start + end) / 2;
        int count = 0;
        for (int i = 0; i < n; ++i)
        {
            count += trees[i] / mid;
        }
        if (count >= m)
            start = mid + 1;
        else
            end = mid - 1;
    }
    cout << end;
    return 0;
}
