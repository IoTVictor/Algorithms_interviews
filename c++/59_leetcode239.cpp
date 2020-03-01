class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        if(nums.size()<2) return nums;
        deque<int> q;
        vector<int> max_vec;
        for(int i=0;i<k;i++){
            while(!q.empty() && nums[i]>=nums[q.back()]){
                q.pop_back();
            }
            q.push_back(i);
        }

        max_vec.push_back(nums[q.front()]);
        for(int i=k;i<nums.size();++i){
            while(!q.empty() && nums[i]>=nums[q.back()]){
                q.pop_back();
            }
            q.push_back(i);
            if(q.front()<=i-k) q.pop_front();
            max_vec.push_back(nums[q.front()]);
        }
        return max_vec;
        }
};
