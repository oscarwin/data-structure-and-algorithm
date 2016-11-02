## 第3章
**本章实现自己的list, deque, stack**

### 环境：
- windows
- IDE采用VS2012

实现C++的容器可以加深对容器的理解，了解STL的实现。同时对拷贝构造函数、重载操作符加深理解。实现C++容器需要了解C++模板。

### 模板
- 类模板的实现文件也是放在一个头文件中

---
    //泛型算法，函数对象
    //通过添加一个类，在类中实现isLessThan函数，保证只有定义了该函数的才能采用该泛型函数

    template<typename Object, typename Comparator>
    const Object& findMax(const vector<Object> & arr, Comparator cmp)
    {
        int maxIndex = 0;
        for(int i = 1; i < arr.size(); ++i)
        {
            if(cmp.isLessThan(arr[maxIndex], arr[i]))
            maxIndex = i;
        }
        //不要返回局部变量的引用，这里巧妙的将下标作为返回对象的识别
        return arr[maxIndex];
    }

    class CaseInsensitiveCompare
    {
        public:
             bool isLessThan(const string & lhs, const string & rth) const
             {return strcmp(lhs.c_str(), ths.c_str()) < 0;}
    };

    int main()
    {
        vector<string> arr(3) = {"ZEBRA", "alligator", "crocodile"};
        std::cout << findMax(arr, CaseInsensitiveCompare()) << std::endl;
        return 0;
    }
    /* 该代码未测试 */


### 双向链表的实现
#### 实现链表过程中对C++的高级语法有了更加深入的理解
- const_iterator的成员变量声明为protected，为了派生类能访问到，外部数据不能访问
- const_iterator重载++运算符，因为++在前不是带参数的，因此才有了primer上说++i比i++效率高
- 迭代器实际上就是对指针的封装成了一个类，对其进行各种运算符的重载



### 栈的实现
- 栈可以通过一个表或者数组来实现
- 通过一个表单向链表实现十分方便，因为表中已经提供了push_back和pop_back函数
- 本文通过vector实现了一个简单的stack结构