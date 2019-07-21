#include <stdlib.h>
#include <stdio.h>

void swap(int* a, int* b)
{
	int temp;
	temp = *a;
	*a = *b;
	*b = temp;
}

void shellSort(int* array, int length)
{
	if(array == NULL || length <= 1)
		return;
	
	int i, j;
	for(int increment = length / 2; increment > 0; increment /= 2)
	{
		for(i = increment; i < length; ++i)
		{
			int temp = array[i];

			for(j = i - increment; j >= 0; j -= increment)
			{
				if(array[j] > temp)
				{
					array[j + increment] = array[j];
				}
				else
				{
					break;
				}
			}
			array[j + increment] = temp;
		}
	}
}

int main()
{
	int numbers[15] = {5, 8, 6, 5, 7, 2, 5, 1, 6, 9, 3, 4, 11, 25, 14};
	shellSort(numbers, 15);

	for(int i = 0; i < 15; ++i)
	{
		printf("%d ", numbers[i]);
	}
	printf("\n");

	return 0;
}
