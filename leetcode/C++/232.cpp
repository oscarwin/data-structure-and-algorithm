class MyQueue {
public:
    /** Initialize your data structure here. */
    MyQueue() {

    }
    
    /** Push element x to the back of queue. */
    void push(int x) {
        input.push_front(x);
    }
    
    /** Removes the element from in front of queue and returns that element. */
    int pop() {
        int ret(0);
        if (!output.empty())
        {
            ret = output.front();
            output.pop_front();
            return ret;
        }
        
        transfer();
        
        ret = output.front();
        output.pop_front();
        return ret;
    }
    
    /** Get the front element. */
    int peek() {
        if (!output.empty())
        {
            return output.front();
        }
        
        transfer();
        
        return output.front();
    }
    
    /** Returns whether the queue is empty. */
    bool empty() {
        if (!output.empty())
        {
            return false;
        }
        
        transfer();
        
        return output.empty();
    }
    
    void transfer()
    {
        while (!input.empty())
        {
            output.push_front(input.front());
            input.pop_front();
        }
    }
private:
    std::deque<int> input;
    std::deque<int> output;
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */