#include "binarySearchTree.h"
#include <malloc.h>

binarySearchTree insert(int element, binarySearchTree T)
{
	if(T == NULL)
	{
		T = (binarySearchTree)malloc(sizeof(struct TreeNode));
		if(T == NULL)
		{
			fprintf(stderr, "out of space!\n");
		}
		else
		{
			T->value = element;
			T->pLeft = NULL;
			T->pRight = NULL;
		}
	}
	else if(element < T->value)
			T->pLeft = insert(element, T->pLeft);

	else if(element > T->value)
			T->pRight = insert(element, T->pRight);
	
	return T;
}

/*递归实现*/
bool find(int element, binarySearchTree T)
{
	if(T == NULL)
		return false;

	if(T->value == element)
	{
		return true;
	}
	else if(element < T->value)
	{
		return find(element, T->pLeft);
	}
	else if(element > T->value)
	{
		return find(element, T->pRight);
	}
}

/*非递归实现*/
bool findUnRecur(int element, binarySearchTree T)
{
	binarySearchTree current = T;
	while(T != NULL)
	{
		if(T->value == element)
		{
			return true;
		}
		else if(element < T->value)
		{
			current = T->pLeft;
		}
		else if(element > T->value)
		{
			current = T->pRight;
		}
	}

	return false;
} 
