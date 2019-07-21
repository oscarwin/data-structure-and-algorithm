/* 对二叉树采用递归和非递归方式实现
** 二叉树的前序，中序和后序遍历。

** 二叉树的前序，中序和后序是针对根
** 节点而言的*/

#include <stdlib.h>

typedef Tree* binaryTree;

struct Tree
{
	int value;
	Tree* pLeft;
	Tree* pRight;
}

/* 递归实现先序遍历 */
void preOrderRecur(binaryTree T)
{
	if(T == NULL)
		return;

	printf("%d ",T->value);

	preOrderRecur(T->pLeft);
	
	preOrderRecur(T->pRight);
}

/* 递归实现中序遍历 */
void inOrderRecur(binaryTree T)
{
	if(T == NULL)
		return;

	inOrderRecur(T->pLeft);

	printf("%d ", T->value);

	inOrderRecur(T->pRight);
}

/* 递归实现后续遍历 */
void posOrderRecur(binaryTree T)
{
	if(T == NULL)
		return;

	posOrderRecur(T->pLeft);

	posOrderRecur(T->pRight);

	printf("%d ", T->value);
}

/* 非递归实现先序遍历 */
void preOrderUnRecur(binaryTree T)
{
	if(T == NULL)
		return;

	stack<int> S;   //定义一个栈

	S.push(T); //压入根节点
	
	while(!S.empty())
	{
		//弹出栈顶元素
		binaryTree tempNode = S.top();
		S.pop();

		printf("%d ", tempNode->value);

		//先压入右子树，后压入左子树
		if(tempTree != NULL)
			S.push(tempNode->pRight);

		if(tempTree != NULL)
			s.push(tempNode->pLeft);
	}
}

/* 非递归实现中序遍历 */
void inOrderUnrecur(binaryTree T)
{
	if(T == NULL)
		return;

	stack<int> S;
	binaryTree tempNode = T;

	while(!S.empty() && tempNode == NULL)
	{
		if(tempNode->pLeft != NULL)
		{
			S.push(tempNode->pLeft);
			tempNode = tempNode->pLeft;
		}
		else
		{
			tempNode = S.top();
			printf("%d ",tempNode->value);
			S.pop();
			tempNode = tempNode.pRight;
		}
	}
}

/* 非递归实现后序遍历 */

/* 按层遍历二叉树 */
//用一个队列保存数据
void floorOrder(binaryTree T)
{
	if(T == NULL)
		return;

	deque<int> Q;
	Q.push_back(T);
	
	while(!Q.empty())
	{
		binaryTree tempNode = Q.front();
		printf("%d ", tempNode->value);

		if(tempNode->pLeft != NULL)
			Q.push_back(tempNode.pLeft);

		if(tempNode->pRight != NULL)
			Q.push_back(tempNode.pRight);

		Q.pop_front();
	}
}
