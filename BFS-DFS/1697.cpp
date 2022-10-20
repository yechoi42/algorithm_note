#include <iostream>
#include <queue>
#define MAX 100001
using namespace std;

int visited[MAX] = {0,};
int n, k;
int cnt = 0;
queue<pair<int,int> > q;

void dfs(int start)
{
    q.push(make_pair(start, 0)); 
    
    int new_pos;
    int new_time;
    while(!q.empty())
    {
        new_pos = q.front().first;
        new_time = q.front().second;
        q.pop();
        if (new_pos == k)
        {
            cout << new_time << '\n';
            break;
        }
        if (visited[new_pos])
            continue;
        else
            visited[new_pos] = 1;
        if ((new_pos * 2 < MAX) && !visited[new_pos * 2])
        {
            q.push(make_pair(new_pos * 2, new_time + 1));
        }
        if ((new_pos + 1 < MAX) && !visited[new_pos + 1])
        {
            q.push(make_pair(new_pos + 1, new_time + 1));
        }
        if ((new_pos - 1 >= 0 ) && !visited[new_pos - 1])
        {
            q.push(make_pair(new_pos - 1, new_time + 1));
        }
    } 
}

int main(void)
{
    cin >> n >> k;
    dfs(n);
    return 0;
}