/*
** 用C语言实现平方探测的哈希表
*/
#include <stdlib.h>
#include <stdio.h>

typedef int Element;
typedef int position;
typedef struct HashTB* HashTable;

HashTable initTable(int size);
void destroyTable(HashTable H);
void insert(Element key, HashTable H);
position find(Element key, HashTable H);
void delete(position p, HashTable H);
position hash(int k, int tableSize);
HashTable rehash(HashTable H);

enum kindOfElement {FULL, EMPTY, DELETE};

typedef struct Entry
{
	Element key;             //元素值
	enum kindOfElement info; //元素状态
};

typedef struct Entry Cell;

typedef struct HashTB
{
	int tableSize;
	Cell *cellTable;
};

/*初始化哈希表*/
HashTable initTable(int size)
{
	HashTable H;

	H = (HashTable)malloc(sizeof(struct HashTB));
	if(H == NULL)
	{
		fprintf(stderr, "out of space.\n");
	}

	H->tableSize = size;
	H->cellTable = malloc(sizeof(Cell) * size);  

	if(H->cellTable == NULL)
	{
		fprintf(stderr, "out of space.\n");
	}

	for(int i = 0; i < H->tableSize; ++i)
	{
		H->cellTable[i].info = EMPTY;
	}

	return H;
}

/*删除哈希表*/
void destroyTable(HashTable H)
{
	if(H == NULL)
		return;
	
	free(H->cellTable);
	free(H);
}

/*哈希函数*/
position hash(int k, int tableSize)
{
	return k % tableSize;
}

/*如果找到指定元素返回该元素位置，如果找不到返回一个空位置*/
position find(Element key, HashTable H)
{
	if(H == NULL)
		return -1;
	
	position pos = hash(key, H->tableSize);
	int collisionNum = 0;

	while(H->cellTable[pos].info != EMPTY && H->cellTable[pos].key != key)
	{
		 pos  = pos + ++collisionNum - 1;
		 if(pos > H->tableSize)
			pos -= H->tableSize;
	}
	return pos;
}

/*插入元素*/
void insert(Element key, HashTable H)
{
	if(H == NULL)
		return;
	
	position p = find(key, H);
	
	if(H->cellTable[p].info != FULL)
	{
		H->cellTable[p].key = key;
		H->cellTable[p].info = FULL;
	}
}

/*删除元素*/
void delete(Element key, HashTable H)
{
	if(H == NULL)
		return;

	position p = find(key, H);

	if(H->cellTable[p].key == key && H->cellTable[p].info == FULL)
	{
		H->cellTable[p].info = DELETE;
	}
}


HashTable rehash(HashTable H)
{
	HashTable newH;
	
	newH = initTable(H->tableSize * 2);

	for(int i = 0; i < H->tableSize; ++i)
	{
		if(H->cellTable[i].info == FULL)
		{
			insert(H->cellTable[i].key, newH);
		}
	}

	destroyTable(H);
	return newH;
}
