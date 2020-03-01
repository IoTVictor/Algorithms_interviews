class MyStack {
public:
    /** Initialize your data structure here. */
    queue<int> q1,q2;
    MyStack() {
    }
    
    /** Push element x onto stack. */
    void push(int x) {
        q1.push(x);
        
    }
    
    /** Removes the element on top of the stack and returns that element. */
    int pop() {
        if(q1.size()==0 &&q2.size()==0) return 0;
        
        while(q1.size()>1){
            q2.push(q1.front());
            q1.pop();
        }
        int num=q1.front();
        q1.pop();
        while(q2.size()>0){
            q1.push(q2.front());
            q2.pop();
        }
        return num;
    }
    
    /** Get the top element. */
    int top() {
        if(q1.size()==0 &&q2.size()==0) return 0;
        while(q1.size()>1){
            q2.push(q1.front());
            q1.pop();
        }
        int num=q1.front();
        q2.push(num);
        q1.pop();
        while(q2.size()>0){
            q1.push(q2.front());
            q2.pop();
        }
        return num;
    }
    
    /** Returns whether the stack is empty. */
    bool empty() {
        return q1.empty() && q2.empty();
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */
