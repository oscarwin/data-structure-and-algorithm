/* 
single linked list by C 
author: liuteng
data: 23 june 2017 */

#include <stdlib.h>

typedef struct Node
{
	int val;
	struct Node* pnext;
};

typedef Node* List;
typedef Node* Position;

/* name:  insert
** input: head of a list, insert position, node 
** output:void*/

void insert(List* L, Position p, int n)
{
	if(L == NULL || p == NULL) 
		return;
	
	struct Node* tmpNode = malloc(sizeof(Node));

	if(tmpNode == NULL)
		return;

	tmpNode->val = n;
	tmpNode->pnext = p->pnext;
	p->pnext = tmpNode;
}

void delete(List* L, int n)
{
	if(L == NULL)
		return;

	while(L->pnext != NULL && L->pnext->val != n)
	{
		L = L->pnext;
	}

	if(L->pnext != NULL)
	{
		Node* del = L->pnext;
		L->pnext = del->pnext;
		free(del);
	}
}
