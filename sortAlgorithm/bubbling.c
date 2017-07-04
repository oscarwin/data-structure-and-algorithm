/*
** bubbling sort
** average time complexity
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

/* 普通冒泡算法 */
void bubbleSort(int* array, int length)
{
	if(array == NULL || length <= 1)
		return;

	for(int i = 0; i < length - 1; ++i)
	{
		for(int j = 0; j < length - i - 1; ++j)
		{
			if(array[j] > array[j + 1])
			{
				swap(&array[j], &array[j + 1]);
			}
		}
	}
}

/* 改进的冒泡算法 */
void bubbleSort1(int* array, int length)
{
	if(array == NULL || length <= 1)
		return;
	
	int pos;
	int i = length -1;

	while(i > 0)
	{
		pos = 0;
		for(int j = 0; j < i; ++j)
		{
			if(array[j] > array[j + i])
			{
				swap(&array[j], &array[j + 1]);
				pos = j;
			}
		}
		i = pos;
	}
}


int main()
{
	int numbers[15] = {5, 8, 6, 5, 7, 2, 5, 1, 6, 9, 3, 4, 11, 25, 14};
	bubbleSort1(numbers, 15);

	for(int i = 0; i < 15; ++i)
	{
		printf("%d ", numbers[i]);
	}

	return 0;
}
