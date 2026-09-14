class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        if(nums.size()==0 || k<=0){
            return {} ;
        }
        int n = nums.size();
        vector<int>r(n-k+1);
        int ri=0;
        deque<int>q;
        for(int i =0;i<n;i++){
            //window ke bhr ane wale index ko remove karna hoga 
            while(!q.empty() && q.front()<i-k+1){
                q.pop_front();
            }
            //smaller elment ko rare se remove karna hoga 
            while(!q.empty() && nums[q.back()]<nums[i]){
                q.pop_back();

            }
            q.push_back(i);
        
        //jabh hamari window complete hogi tabh 
        if(i>=k-1){
            r[ri++]=nums[q.front()];
        }
    }
    return r;
    }
};