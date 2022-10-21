#include <iostream>
#include <vector>
#include <algorithm>
#define MAX 25
using namespace std;

int house[MAX][MAX];
int checked[MAX][MAX];
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, -1, 1};
vector<int> q;

int n;
int cnt;

void dfs(int x, int y)
{
    if (x >= 0 && x < n && y >= 0 && y < n
    && !checked[x][y] && house[x][y])
    {
        checked[x][y] = 1;
        cnt++;
        for (int i = 0; i < 4; i++)
        {
            dfs(x + dx[i], y + dy[i]);
        }
    }
}

int main(void)
{
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        string s;
        cin >> s;
        for (int j = 0; j < n; j++)
        {
            house[i][j] = s[j] -'0';
        }
    }
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (house[i][j] && !checked[i][j])
            {
                cnt = 0;
                dfs(i, j);
                q.push_back(cnt);
            }
        }
    }
    sort(q.begin(), q.end());
    cout << q.size() << '\n';
    for (int i = 0; i < q.size() ; i++)
    {
        cout << q[i] << '\n';
    }
    return 0;
}