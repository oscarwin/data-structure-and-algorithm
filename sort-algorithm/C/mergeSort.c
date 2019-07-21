#include <stdlib.h>
#include <stdio.h>

void merge(int* array, int* tmpArray, int left, int center, int right)
{
	int pos1 = left;
	int pos2 = center + 1;
	int tmpPos = 0;

	while(pos1 <= center && pos2 <= right)
	{
		if(array[pos1] < array[pos2])
		{
			tmpArray[tmpPos++] = array[pos1++];
		}
		else
		{
			tmpArray[tmpPos++] = array[pos2++];
		}
	}

	while(pos1 <= center)
		tmpArray[tmpPos++] = array[pos1++];

	while(pos2 <= right)
		tmpArray[tmpPos++] = array[pos2++];

	int* cur = array + left;
	for(int i = 0; i < tmpPos; ++i)
	{
		*cur++ = *(tmpArray + i);
	}
}

void mSort(int* array, int* tmpArray, int left, int right)
{
	if(left == right)
		return;

	int center = (left + right) / 2;

	mSort(array, tmpArray, left, center);
	mSort(array, tmpArray, center + 1, right);
	merge(array, tmpArray, left, center, right);
}

void mergeSort(int* array, int length)
{
	int* tmpArray = (int*)malloc(sizeof(int) * length);
	if(tmpArray == NULL)
	{
		printf("out of space!!!\n");	
		return;
	}
	mSort(array, tmpArray, 0, length - 1);
}

int main()
{
	int numbers[15] = {5, 8, 6, 5, 7, 2, 5, 1, 6, 9, 3, 4, 11, 25, 14};
	mergeSort(numbers, 15);

	for(int i = 0; i < 15; ++i)
	{
		printf("%d ", numbers[i]);
	}
	printf("\n");

	return 0;
}
