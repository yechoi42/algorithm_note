#include <iostream>
#include <vector>
#include <queue>
#define MAX 25

using namespace std;

int house[MAX][MAX];
int visited[MAX][MAX];
int x_dir[4] = {-1, 1, 0, 0};
int y_dir[4] = {0, 0, -1, 1};
vector<int> result;
queue<pair<int, int>> q;
int cnt = 0;

void dfs(int start_x, int start_y)
{
    visited[start_x][start_y] = 1;
    q.push(make_pair(start_x, start_y));
    cnt++;

    while (!q.empty())
    {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        for(int i = 0; i < 4; i++)
        {
            int x_new = x + x_dir[i];
            int y_new = y + y_dir[i];

            if (maze[x_new][y_new] == 1 && !visited[x_new][y_new] &&
            (0 <= x_new && x_new < N) && (0 <= y_new && y_new < M))
            {
                visited[x_new][y_new] = 1;
                q.push(make_pair(x_new, y_new));
                cnt++;
            }
        }
    }
}

int main(void)
{
    int n;
    string s;
    cin >> n;
    for (int i = 0 ; i < n; i++)
    {
        cin >> s;
        for (int j = 0; j < M; j++)
        {
            house[i][j] = s[j] - '0';
        }
    }
    for (int i = 0; i < n; i++) 
    {
        for (int j = 0; j < n; j++) 
        {
            if (arr[i][j]=='1' && visited[i][j] == false) 
            {
                cnt = 0;
                bfs(i,j);
                result.push_back(cnt);
            }
        }
    }
    sort(result.begin(),result.end());
    
    cout << result.size() << "\n";
    for (int i = 0; i < result.size(); i++) 
    {
        cout << result[i] << "\n";
    }
    return 0;
}