//method 2 
#include <iostream>
#include <stdlib.h>
int max(int X, int Y, int Z)
{
	int max = 0;
	max = X > Y ? X : Y;
	if(Z > max)
		max = Z;
	return max;
}

int maxsubsum(int array[], int left, int right)
{
	int maxsum = 0;
	int center = (left + right)/2; 
	int leftmax = 0, rightmax = 0,leftbordermax = 0, rightbordermax = 0;
	int tempsum = 0;
	if(left == right)
	{
		maxsum = array[left];
		return maxsum;
	}
	//求左边最大子序列和
	leftmax = maxsubsum(array, left, center);
	//求右边最大子序列和
	rightmax = maxsubsum(array, center + 1, right);
	//求含左边界的最大序列和
	for(int i = center; i >= left; i--)
	{
		tempsum += array[i];
		if(tempsum > leftbordermax)
		{
			leftbordermax = tempsum;
		}
	}
	//求含右边界的最大序列和
	tempsum = 0;
	for(int j = center + 1; j <= right; j++)
	{
		tempsum += array[j];
		if(tempsum > rightbordermax)
		{
			rightbordermax = tempsum;
		}
	}
	return max(leftmax, rightmax, leftbordermax + rightbordermax);
}

int main()
{
	int iarray[] = {10, 12, -5, 6, -1, -7, 18, 1, -9, 8};
	int icount = sizeof(iarray)/sizeof(iarray[0]);
	int imax = maxsubsum(iarray, 0, icount-1);
	std::cout << imax << std::endl;
	system("pause");
	return 0;
}

//时间复杂度O(NlogN)