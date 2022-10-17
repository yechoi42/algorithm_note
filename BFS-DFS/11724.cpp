#include <iostream>
#include <vector>
#define MAX 1001

using namespace std;

int n, m, tmp1, tmp2;
vector<int> points[MAX];
bool checked[MAX];
int cnt = 0;

void dfs(int start)
{
    checked[start] = true;
    for (int i = 0; i < points[start].size(); i++)
    {
        int new_pos = points[start][i];
        if (!checked[new_pos])
        {
            dfs(new_pos);
        }
    }
}


int main(void)
{
    cin >> n >> m;
    for (int i = 0; i < m; i++)
    {
        cin >> tmp1 >> tmp2;
        points[tmp1].push_back(tmp2);
        points[tmp2].push_back(tmp1); 
    }
    for (int i = 1; i <= n; i++)
    {
        if (!checked[i])
        {
            cnt++;
            dfs(i);
        }
    }
    cout << cnt << '\n';
}