class Solution {
public:
    bool isValid(string s) {
        stack<char>st;
        for(int i=0;i<s.length();i++){
            char c=s[i];
            if(c=='(')
            st.push(')');
            else if (c=='{')
            st.push('}');
            else if(c =='[')
            st.push(']');
            else if(st.empty() || st.top()!=c)
            return false;

    else
    st.pop();

        }
        return st.empty();
    }
};