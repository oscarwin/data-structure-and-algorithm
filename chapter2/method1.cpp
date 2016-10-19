//method 1
#include <iostream>
#include <stdlib.h>
int main()
{
	int iarray[] = {10, 12, -5, 6, -1, -7, 18, 1, -9, 8};
	int icount = sizeof(iarray)/sizeof(iarray[0]);
	int imax = 0;
	int temp = 0;
	for(int i = 0; i < icount; i++)
	{
		temp = 0;
		for(int j = i; j < icount; j++)
		{
			temp += iarray[j];
			if(temp > imax)
			{
				imax = temp;
			}
		}
	}
	std::cout << imax << std::endl;
	system("pause");
	return 0;
}

//时间复杂度O(N2)