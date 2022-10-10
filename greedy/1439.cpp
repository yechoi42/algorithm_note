#include <iostream>
#include <string>

using namespace std;

int main(void)
{
    string s;
    cin >> s;

    int len = s.length();
    int count_zero = 0;
    int count_one = 0;
    char before = s[0];
    if (before == '0')
        count_zero += 1;
    else
        count_one += 1;


    for (int i = 0; i < len; i++)
    {
        if (before != s[i])
        {
            before = s[i];
            if (s[i] == '0')
                count_zero += 1;
            else
                count_one += 1;
        }
        
    }
    cout << (count_zero > count_one ? count_one : count_zero) << '\n';
    return 0;
}