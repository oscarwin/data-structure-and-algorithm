#include <vector>
#include <list>

template <typename T>
class CHashTable
{
public:
	//初始化哈希表大小
	CHashTable(int size = 101);
	~CHashTable();

	void insert(const T& obj);
	bool contains(const T& obj);
	void remove(const T& obj);

private:
	std::vector<std::list<T> > m_table; 
	int myhash(const T& obj);
	int hash(int key);
}

template <typename T>
CHashTable::CHashTable(int size /*= 101*/)
{
	m_table.resize(size);
	m_table.reserve(size);
}

template <typename T>
void insert(const T& obj)
{
	int key = myhash(obj);
	m_table[key].push_back(obj);
}

template <typename T>
bool contains(const T& obj)
{
	int key = myhash(obj);
	for(auto it = m_table[key].cbegin(); it != m_table[key].cend(); ++it)
	{
		if(*it = obj)
			return true;
	}
	return false;
}

template <typename T>
void remove(const T& obj)
{
	if(contains(obj))
	{
		int key = myhash(obj);

	}
}
