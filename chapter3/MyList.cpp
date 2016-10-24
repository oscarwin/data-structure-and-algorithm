/***************************************************************************
*  @file           MyList.cpp
*  @author      Peter Liu
*  @date         22  Oct 2016
*  @remark     
*  @note         Create a list of myself
***************************************************************************/

#include "MyList.h"

template <typename T> Node* MyList::MyList()
{
	pFirst = new Node;
	pLast = pFirst;
}

template <typename T> Node* MyList::MyList()
{
	Delete pFirst;
	pFirst == NULL;
}

template <typename T> bool MyList::IsEmpty()
{
	if (NULL == pFirst->Next)
	    return true;
	else
	    return false;
}

template <typename T> bool MyList::IsLast(Position P)
{
	return P->Next == NULL ? true : false;
}

template <typename T> void MyList::push_back(T temp)
{
	Node* pNode;
	pNode->Element = temp;
	pNode->Next = NULL;
	Node* temp = pLast;
	temp->Next = pNode;
	pLast = pNode;
}

template <typename T> void MyList::Insert(Position p, T Tect)
{
	Node* temp;
	temp->Element = Tect;
	temp->Next = p->Next;
	p->Next = temp;
}