/*
** insert sort
*/

#include <stdlib.h>
#include <stdio.h>

void swap(int* a, int* b)
{
	int temp;
	temp = *a;
	*a = *b;
	*b = temp;
}

void insertSort(int* array, int length)
{
	if(array == NULL || length <= 1)
		return;
	
	int i, j;
	for(i = 1; i < length; ++i)
	{
		int temp = array[i];

		for(j = i - 1; j >= 0; --j)
		{
			if(array[j] > temp)
			{
				array[j + 1] = array[j];
			}
			else
			{
				break;
			}
		}
		array[j + 1] = temp;
	}
}

int main()
{
	int numbers[15] = {5, 8, 6, 5, 7, 2, 5, 1, 6, 9, 3, 4, 11, 25, 14};
	insertSort(numbers, 15);

	for(int i = 0; i < 15; ++i)
	{
		printf("%d ", numbers[i]);
	}
	printf("\n");

	return 0;
}
