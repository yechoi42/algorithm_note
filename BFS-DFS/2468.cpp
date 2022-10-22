#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#define MAX 101
using namespace std;

int arr[MAX][MAX];
int checked[MAX][MAX];
int n;
int height;
int cnt;
vector<int> v;

void dfs(int x, int y)
{
    if (x >= 0 && x < n && y >= 0 && y < n && arr[x][y] > height && !checked[x][y])
    {
        checked[x][y] = 1;
        dfs(x + 1, y);
        dfs(x - 1, y);
        dfs(x, y + 1);
        dfs(x, y - 1);
    }
}

void check_arr(void)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (!checked[i][j] && arr[i][j] > height)
            {
                cnt++;
                dfs(i, j);
            }
        }
    }
}

int main(void)
{
    int tmp;
    int max_num = 0;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cin >> tmp;
            if (max_num < tmp)
                max_num = tmp;
            arr[i][j] = tmp;
        }
    }
    for (int i = 1; i < max_num; i++)
    {
        memset(checked, 0, sizeof(checked));
        cnt = 0;
        height = i;
        check_arr();
        v.push_back(cnt);
    }
    sort(v.begin(), v.end(), greater<int>());
    cout << v[0] << endl;
}