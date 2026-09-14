class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temp) {
        stack<int>st ;
        vector<int> ans(temp.size(), 0);
        for (int i = 0; i<temp.size();i++){
            while(!st.empty() && temp[i]>temp[st.top()]){
                int prev = st.top();
                st.pop();
                //kitne din baad hume warmer day mil raha hai 
                ans[prev]=i-prev;

            }
            st.push(i);

        }
        return ans;

    }
};