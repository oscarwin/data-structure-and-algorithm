/***************************************************************************
*  @file           MyList.h
*  @author      Peter Liu
*  @date         22  Oct 2016
*  @remark     
*  @note         Create a list of myself
***************************************************************************/


template< typename T> class MyList
{
	typedef Node* Position;        //表示位置指针
public:
	MyList();
	~MyList();
	List MakeEmpty();
	bool IsEmpty();
	bool IsLast(Position);
	void Insert(Position p, T Tect);
	void push_back(T Tect);
	void Delete(Position);
public:
	struct Node
	{
		T Element;
		Node * Next;
		//结构体构造函数
		Node(Node* n = NULL):
			,Next = n{}
	};
	Node* pFirst;                      //表头
	Node* pLast;
};