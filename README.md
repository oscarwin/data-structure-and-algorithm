# Data-Structure-and-Algorithm
本文的目的：

1. 总结常用的数据结构并进行实现
2. 总结常见的排序的算法
3. 总结常见的搜索算法

采用语言：C/C++
测试平台：Ubuntu16.04 x64

# 排序算法

排序算法稳定性：两个相同的元素排序前后的相对位置关系不会发生改变。

## 复杂度比较
| 算法 | 平均时间复杂度 | 最好情况 | 最坏情况 | 空间复杂度 | 稳定性
| --- | :---: | :---: |:---: | :---: |:---: |
| 冒泡排序 | $O(N^2)$ | $O(N^2)$ | $O(N^2)$ | $O(1)$ |稳定
| 插入排序 | $O(N^2)$ | $O(N)$   | $O(N^2)$ | $O(1)$ |稳定
| 希尔排序 | $O(N^{3/2})$ |      | $O(N^2)$ | $O(1)$ |不稳定
| 堆排序 | $O(NlogN)$ |   $O(NlogN)$   | $O(NlogN)$ | $O(1)$ |不稳定
| 归并排序 | $O(NlogN)$ | $O(NlogN)$ | $O(NlogN)$ | $O(N)$ |稳定
| 快速排序 | $O(NlogN)$ | $O(NlogN)$ | $O(N^2)$ | $O(1)$ |不稳定

## 冒泡排序
#### 排序过程
1. 将第一个元素与第二个元素比较大小，如果第一个元素大于第二个元素则调换他们两的位置；
2. 比较第二个元素和第三个元素的大小，如果第二个元素大于第三个元素则调换他们两的位置；
3. 依次类推，进行两两元素的比较和交换，最终最大的元素排在了最后面；
4. 重复1到3过程，直到所有元素都排序。

#### 图片演示
![这里写图片描述](https://user-gold-cdn.xitu.io/2016/11/30/f427727489dff5fcb0debdd69b478ecf)

#### 复杂度分析

- 平均时间复杂度：$O(N^2)$
- 最坏情况复杂度：$O(N^2)$

#### C语言代码
```
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

int main()
{
	int numbers[15] = {5, 8, 6, 5, 7, 2, 5, 1, 6, 9, 3, 4, 11, 25, 14};
	bubbleSort(numbers, 15);

	for(int i = 0; i < 15; ++i)
	{
		printf("%d ", numbers[i]);
	}

	return 0;
}

```

## 插入排序
#### 排序过程
1. 对于第K个元素，将该元素的值存储在零时变量中，比较第前一个元素与该元素的大小，如果大于该元素就将前一个元素往后移动一步；
2. 比较前面第二个元素与该元素的大小，如果大于该元素就将前第二个元素往后移动一步；
3. 重复上述过程直到找到小于等于原来第K个元素（保存在零时变量中）的位置，并将第K个元素插入到这个元素的后面。或者找不到小于等于第K个元素的位置，就将原来第K个元素插入到数组的首地址。

#### 图片演示
![这里写图片描述](https://user-gold-cdn.xitu.io/2016/11/29/f0e1e3b7f95c3888ab2791b6abbfae41)

#### 复杂度分析

- 平均时间复杂度：$O(N^2)$
- 最坏情况复杂度：$O(N^2)$
- 最好情况复杂度：$O(N)$ (数组本身就是按升序排列)
- 最多需要$	\dfrac{n(n-1)}{2} $次比较
- 最少需要$n - 1$次比较

#### C语言代码
```
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
```

## 希尔排序
希尔排序是在插入排序的基础上进行发展的，通过一个希尔增量先排序一定间隔的数据。
#### 排序过程
1. 插入排序每次与前面一个比较，然后再往前一个，而希尔排序每次往前K个；
2. 当增量为1的时候，希尔排序与插入排序就完全是一样的过程；
3. 所以代码也很好实现，将插入排序中增1的地方改为增K就行。

#### 图片演示
| 初始 | 81 | 94 | 11 | 96 | 12 | 35 | 17 | 95 | 28 | 58 |
| --- | --- | :--- |:--- | :--- |:--- | :---|
| 第一趟5排序后 | 35 | 17 | 11 | 28 | 12 | 81 | 94 | 95 | 96 | 58 |
| 第二趟3排序后 | 28 | 12 | 11 | 35 | 17 | 81 | 58 | 95 | 96 | 94 |
| 第三趟1排序后 | 11 | 12 | 17 | 28 | 35 | 58 | 81 | 94 | 95 | 96 |

#### 复杂度分析
希尔排序的时间复杂度比较复杂，选用不同的希尔增量也会导致复杂度不同，有研究表明选用希尔增量时有如下结果：
- 平均时间复杂度：$O(N^{5/4})$
- 最坏情况复杂度：$O(N^2)$

#### C语言代码

```
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
	//取一半为希尔增量
	for(int increment = length / 2; increment > 0; increment /= 2)
	{
		//与插入排序比较，就是将插入排序代码中的1换成了增量increment，对比一下两个代码
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
```

## 堆排序
#### 排序过程
1. 建立最大堆，建堆的过程是从N/2的位置开始，将父节点与子节点比较，如果子节点大于父节点则交换。为什么是N/2，是因为堆中树叶的个数是N/2。
2. 从堆中删除堆顶元素，对于最大堆而言，堆顶元素也就是最大元素。每删除一个堆顶元素，就将堆顶元素放在数组的后面，因为每删除一个就出现一个空位，所以数组后面是有地方存放的。
3. 进行N-1次的删除以后，整个数组就是排序的状态了。

#### 图片演示
![这里写图片描述](https://user-gold-cdn.xitu.io/2016/11/29/d1ac550a097055f65ed10a50d408f40d)

#### 复杂度分析

- 建堆的平均时间是：$O(N)$
- 建堆的最坏情况是：$O(NlogN)$
- 删除元素的时间是：$O(logN)$
- 整个排序平均时间复杂度：$O(N + NlogN) = O(NlogN)$
- 最坏情况复杂度：$O(NlogN)$

#### C语言代码

```
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
```

## 归并排序
#### 排序过程
1. 将数组Ｎ从中间分成两个数组N1和N2；
2. 用两个指针分别指向数组N1和N2的首地址，比较两个指针所指向值的大小，将值较小的那个插入到一个临时数组中，然后将该指针加一。直到数组N1和N2中有一个成员全部都放入到临时数组中，最后将另一个数组中剩余的数按原来的顺序插入到临时数组的尾部，整个过程就是归并的过程；
3. 其中在分成两个数组的过程，采用递归的方法，一直分割到数组中只有一个元素为止。先分割后归并。

#### 图片演示
![这里写图片描述](https://user-gold-cdn.xitu.io/2016/11/29/33d105e7e7e9c60221c445f5684ccfb6)

#### 复杂度分析

- 平均时间复杂度：$O(NlogN)$
- 最坏情况复杂度：$O(NlogN)$

#### C语言代码

```
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
```

## 快速排序
#### 排序过程
1. 选择一个枢纽元，可以选择首，尾，中三个数的中位数作为枢纽元；
2. 将枢纽元的为止与数组的尾地址进行交换；
3. 定义两个指针，P1指向数组首地址，P2指向数组倒数第二个位置，P1所指元素的值与枢纽元比较，如果小于枢纽元则后移一位，如果大于就停下来。P1所指元素的值与枢纽元比较，如果大于枢纽元则前移一位，如果小于就停下来；
4. 交换P1和P2所指向的元素；
5. 重复３和４直到P1大于P2；
6. 对数组的分割过程同样采用递归的方法。

#### 图片演示

#### 复杂度分析

- 平均时间复杂度：$O(NlogN)$
- 最坏情况复杂度：$O(N^2)$

#### C语言代码
```
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
	return 0;
}
```

[TOC]
