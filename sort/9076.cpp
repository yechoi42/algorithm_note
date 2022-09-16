#include <iostream>
#include <vector>
#include <algorithm>

int main(void) 
{
    int t;
    std::cin >> t;
    std::vector<int> grade(5);

    int *result = new int[t];

    for (int i = 0; i < t; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            std::cin >> grade[j];
        }
        std::sort(grade.begin(), grade.end());
        if (grade[3] - grade[1] >= 4)
		{
			result[i] = -1;
		}
		else
		{
			result[i] = grade[1] + grade[2] + grade[3];
		}
	}

	for (int i = 0; i < t; i++)
	{
		if (result[i] != -1)
        {
            std::cout << result[i];
        }
		else
        {
            std::cout << "KIN";
        }
		std::cout << "\n";
	}
    return 0;
}