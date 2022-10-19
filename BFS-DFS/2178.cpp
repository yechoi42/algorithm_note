#include <iostream>
#include <queue>
#define MAX 101
using namespace std;

int n, m, tmp;
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};
int maze[MAX][MAX];
int checked[MAX][MAX];
int distances[MAX][MAX];
queue<pair<int,int> > q;

void dfs(int start_x, int start_y)
{
    int x;
    int y;
    checked[start_x][start_y] = 1;
    distances[start_x][start_y]++;
    q.push(make_pair(start_x, start_y));

    while (!q.empty())
    {
        x = q.front().first;
        y = q.front().second;
        q.pop();
        for (int i = 0; i < 4; i++)
        {
            int x_new = x + dx[i];
            int y_new = y + dy[i];
            if (!checked[x_new][y_new] && maze[x_new][y_new] && (x_new >= 0 && x_new < n)&& (y_new >= 0 && y_new < m))
            {
                checked[x_new][y_new] = 1;
                distances[x_new][y_new] = distances[x][y] + 1;
                q.push(make_pair(x_new, y_new));                
            }
        }
    }

}

int main(void)
{
    cin >> n >> m;
    for (int i = 0; i < n; i++)
    {
        string s;
        cin >> s;
        for(int j = 0; j < m; j++)
        {
            maze[i][j] = s[j] - '0';
        }
    }
    dfs(0, 0);
    cout << distances[n-1][m-1] << '\n';
    return 0;
}