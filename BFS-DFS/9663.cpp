#include <iostream>
#include <cstring>

int result = 0;
int n;
int board[15];

bool possible(int row)
{
    for (int i = 0; i < row; i++)
    {
        if (board[i] == board[row] || (abs(board[i] - board[row]) == row - i))
            return false;
    }
    return true;
}

void    set_queen(int row)
{
    if (row == n)
    {
        result++;
        return ;
    }
    for (int i = 0; i < n; i++)
    {
        board[row] = i;
        if (possible(row))
            set_queen(row + 1);
    }   
}

int main()
{
    std::cin >> n;
    std::memset(board, 0, sizeof(int) * 15);
    set_queen(0);
    std::cout << result;
    return (0);
}