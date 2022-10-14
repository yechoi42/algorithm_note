#include <iostream>
#include <vector>
#define MAX 101

using namespace std;

vector<int> computers[MAX];
bool checked[MAX];
int cnt = 0;

void dfs(int start)
{
    checked[start] = true;
    for (int i = 0; i < computers[start].size(); i++)
    {
        int new_pos = computers[start][i];
        if (!checked[new_pos])
        {
            cnt++;
            dfs(new_pos);
        }
    }
}

int main(void)
{
    int n;
    cin >> n;

    int m, tmp1, tmp2;
    cin >> m;
    for (int i = 0; i < m; i++)
    {
        cin >> tmp1 >> tmp2;
        computers[tmp1].push_back(tmp2);
        computers[tmp2].push_back(tmp1);
    }
    dfs(1);
    cout << cnt << '\n';
    return 0;
}