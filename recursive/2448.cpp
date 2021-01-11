#include <iostream>
#include <math.h>
using namespace std;

int n;
char    **paper;
char    triangle[][6] = {"  *  "," * * ","*****"};

void drawing(int x, int y, int n)
{
	if (n == 3)
	{
		for (int i = 0 ; i < 3 ; i++)
		{
			for (int j = 0 ; j < 5 ; j++)
			{
                paper[y][x] = '*';
                paper[y + 1][x - 1] = '*';
                paper[y + 1][x + 1] = '*';
                paper[y + 2][x - 2] = '*';
                paper[y + 2][x - 1] = '*';
                paper[y + 2][x] = '*';
                paper[y + 2][x + 1] = '*';
                paper[y + 2][x + 2] = '*';
                return;
			}
		}
		return ;
	}
    drawing(x, y, n / 2);
    drawing(x - (n / 2), y + (n / 2), n / 2);
    drawing(x + (n / 2), y + (n / 2), n / 2);
}

void init(void)
{
	paper = (char **)malloc(sizeof(char *) * n);
	for (int i = 0 ; i < n ; i++)
	{
		paper[i] = (char *)malloc(sizeof(char) * (n * 2 + 1));
		memset(paper[i], ' ', (n * 2));
	}
}

int main(void)
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cin >> n;
	init();
	drawing(n - 1, 0, n);
    for (int i = 0; i < n; i++)
    {
        paper[i][2 * n] = '\0';
        cout << paper[i] << '\n';
    }
	return (EXIT_SUCCESS);
}