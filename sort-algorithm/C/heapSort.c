#include <stdlib.h>
#include <stdio.h>

#define leftChild(i) (2 * (i) + 1)

void swap(int* a, int* b)
{
	int temp;
	temp = *a;
	*a = *b;
	*b = temp;
}

/*
** 功能：下虑函数
** 参数：下虑的堆，堆中元素的个数，下虑的位置
*/
void percDown(int* array, int length, int i)
{
	int tmp;
	int greaterChild;

	for(tmp = array[i]; leftChild(i) < length; i = greaterChild)
	{
		greaterChild = leftChild(i);
		//找出较大的那个儿子
		if(greaterChild + 1 < length && array[greaterChild] < array[greaterChild + 1])
			++greaterChild;
		if(tmp < array[greaterChild])
		{
			array[i] = array[greaterChild];
		}
		else
		{
			break;
		}
	}
	array[i] = tmp;
}

//堆排序
void heapSort(int* array, int length)
{
	//建立堆
	for(int i = length / 2; i >= 0; --i)
		percDown(array, length, i);
	
	for(int i = length - 1; i > 0; --i)
	{
		swap(&array[i], &array[0]);　　//将存放在堆顶的最大元素交换到堆的末尾
		percDown(array, i, 0);
	}
}

int main()
{
	int numbers[15] = {5, 8, 6, 5, 7, 2, 5, 1, 6, 9, 3, 4, 11, 25, 14};
	heapSort(numbers, 15);

	for(int i = 0; i < 15; ++i)
	{
		printf("%d ", numbers[i]);
	}
	printf("\n");

	return 0;
}
