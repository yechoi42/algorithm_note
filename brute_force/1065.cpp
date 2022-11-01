#include <iostream>

using namespace std;

int main(void)
{
    int n = 0;
    int cnt;
    cin >> n;

    if (n < 100)
        cnt = n;
    else 
    {
        cnt = 99;
        for (int i = 100; i <= n; i++)
        {
            int hundred = i / 100;
            int ten = (i / 10) % 10;
            int one = i % 10;
            if ((hundred - ten ) == (ten - one))
            {
                cnt++;
            }
        }
    }
    cout << cnt << endl;
    return 0;
}