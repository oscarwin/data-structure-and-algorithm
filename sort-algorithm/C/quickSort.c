/*
** quick sort
** average time complexity: O(NlogN)
** worst case: O(N2)
*/
#include <stdlib.h>
#include <stdio.h>

void partition(int* array, int begin, int end);

void swap(int * a, int * b)
{
	int temp;
	temp = *a;
	*a = *b;
	*b = temp;
}

void quickSort(int* array, int length)
{
	if(array == NULL || length <= 1)
		return;

	partition(array, 0, length - 1);
}

void partition(int* array, int begin, int end)
{
	if(array == NULL || begin == end)
		return;

	//选取最左边，最右边和中间三个位置数中的中位数作为枢纽元,
	//并将枢纽元调到数组最后面的位置
	int center = (begin + end) / 2;
	if(array[begin] > array[center])
		swap(&array[begin], &array[center]);
	
	if(array[begin] > array[end])
		swap(&array[begin], &array[end]);
	
	if(array[center] > array[end])
		swap(&array[center], &array[end]);
	
	//交换数据
	int left = begin;
	int right = end;
	while(left < right)
	{
		while(array[++left] < array[end]);
		while(array[--right] > array[end]);

		if(left < right)
		{
			swap(&array[left], &array[right]);
		}
	}

	swap(&array[left], &array[end]);

	//递归调用
	partition(array, begin, left - 1);
	partition(array, left, end);
}

int main()
{
	int numbers[15] = {5, 8, 6, 5, 7, 2, 5, 1, 6, 9, 3, 4, 11, 25, 14};
	quickSort(numbers, 15);

	for(int i = 0; i < 15; ++i)
	{
		printf("%d ", numbers[i]);
	}
	return 0;
}
