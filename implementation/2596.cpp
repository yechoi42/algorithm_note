#include <iostream>
#include <string>
using namespace std; 

string alpha_list[] = {"000000", "001111", "010011", "011100", "100110", "101001", "110101", "111010"};

int check_alpha(string s)
{
    for (int i = 0; i < 8; i++)
    {
        string alpha = alpha_list[i];
        int count = 0;
        for (int j = 0; j < 6; j++)
        {
            if (alpha[j] != s[j])
            {
                count += 1;
                if (count > 1)
                    break;
            }
        }
        if (count <= 1)
            return i;
    }
    return -1;
}

int main(void) 
{
    int n;
    cin >> n;

    string s;
    cin >> s;
    char result[n + 1];
    result[n] = 0;

    for (int i = 0; i < n ; i++)
    {
        string t = s.substr(i * 6, 6);
        int alpha = check_alpha(t);
        if (alpha == -1)
        {
            cout << i + 1 << endl;
            return 0;
        }
        result[i] = 'A' + alpha;
    }
    cout << result << endl;
    return 0;
}