#!/usr/bin/python3
#-*- coding:utf-8 -*-

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.input = []
        self.output = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.input.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.output) != 0:
            return self.output.pop()
        
        self.__transfer()
        
        return self.output.pop()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.output) != 0:
            return self.output[-1]
        
        self.__transfer()
        
        return self.output[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.output) != 0:
            return False
        
        self.__transfer()
        
        return len(self.output) == 0
    
    def __transfer(self) -> None:
        """
        Transfer element from input to output
        """
        while len(self.input) != 0:
            self.output.append(self.input.pop())


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push("hello")
obj.push("world")
param_2 = obj.pop()
print(param_2)
param_3 = obj.peek()
print(param_3)
param_4 = obj.empty()
print(param_4)