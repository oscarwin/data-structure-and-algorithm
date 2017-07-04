#include <stdio.h>
#include <stdlib.h>


struct TreeNode
{
	int value;
	TreeNode* pLeft;
	TreeNode* pRight;
};

typedef TreeNode* binarySearchTree;

binarySearchTree insert(int element, binarySearchTree T);
bool find(int element, binarySearchTree T);
bool findUnRecur(int element, binarySearchTree T);
