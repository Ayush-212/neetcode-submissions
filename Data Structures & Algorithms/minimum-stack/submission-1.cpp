class MinStack {
public:
    MinStack() {
        
    }
    stack<pair<int,int>>st;
    void push(int val) {
        if(st.empty()){
            st.push({val,val});
        }else{
        int current_min= st.top().second;
        st.push({val,min(val,current_min)});
        }
    }
    
    void pop() {
        if(!st.empty()){
            st.pop();
        }
    }
    
    int top() {
        return st.top().first;
    }
    
    int getMin() {
        return st.top().second;
    }
};
