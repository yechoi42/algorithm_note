#include <iostream>
#include <vector>
#include <numeric>
using namespace std;

int main(void)
{
    int count = 1;
    int l, p, v;
    int sum;
    while (1)
    {
        cin >> l >> p >> v;
        if (l == 0 && p == 0 && v == 0)
            break;
        sum = (v / p) * l;
        if (v % p >= l)
            sum += l;
        else
            sum += v % p;
        cout << "Case " << count << ": " << sum << "\n";
        count += 1;
    }
    return 0;
}