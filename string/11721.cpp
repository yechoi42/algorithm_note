#include <iostream>
#include <string.h>
using namespace std;
int main(void)
{
    char str[101];
    memset(str, 0, 101);
    cin >> str;
    int len = strlen(str);
    for (int i = 0; i < len; i++)
    {
        cout << str[i];
        if (i > 1 && (i + 1) % 10 == 0)
            cout << endl;
    }
    return 0;
}