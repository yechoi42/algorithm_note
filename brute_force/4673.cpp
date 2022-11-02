#include <iostream>

using namespace std;

int nums[10001] = {0, };

int d(int n)
{
    int cnt = n;
    while (n >= 1)
    {
        cnt += n % 10;
        n /= 10;
    }
    return cnt;
}

int main(void)
{
    int i;
    int next;
    int post_next;
    for (i = 1; i <= 10000; i++)
    {
        if (nums[i] == 1)
            continue;
        else 
        {
            next = d(i);
            while (next <= 10000) 
            {
                nums[next] = 1;
                next = d(next);
            }
        }
    }
    for (int j = 1; j <= 10000; j++)
    {
        if (!nums[j])
            cout << j << '\n';
    }
}