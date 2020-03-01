class MyQueue {
public:
    /** Initialize your data structure here. */
    stack<int> instack,outstack;
    MyQueue() {
        
    }
    
    /** Push element x to the back of queue. */
    void push(int x) {
        instack.push(x);
    }
    
    /** Removes the element from in front of queue and returns that element. */
    int pop() {
        while(instack.size()>1)
        {outstack.push(instack.top());
            instack.pop();
        }
        int num=instack.top();
        instack.pop();
        while(!outstack.empty())
            {instack.push(outstack.top());
             outstack.pop();
             }
        return num;
    }
    
    /** Get the front element. */
    int peek() {
        while(instack.size()>1)
        {outstack.push(instack.top());
         instack.pop();
        
        }
        int num=instack.top();
        outstack.push(instack.top());
        instack.pop();
        while(!outstack.empty())
        {instack.push(outstack.top());
            outstack.pop();
        }
        return num;
        
    }
    
    /** Returns whether the queue is empty. */
    bool empty() {
        return instack.empty()&&outstack.empty();
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */
