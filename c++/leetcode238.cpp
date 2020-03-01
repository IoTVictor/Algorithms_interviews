ass Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> tmp1(nums.size(),1);
        vector<int> tmp2(nums.size(),1);

        for(int i=1;i<nums.size();i++)
            tmp1[i]=tmp1[i-1]*nums[i-1];
        
        for(int i=nums.size()-2;i>=0;i--)
               tmp2[i]=tmp2[i+1]*nums[i+1];
        
        for(int i=nums.size()-1;i>=0;i--)
               tmp2[i]=tmp1[i]*tmp2[i];
        
        return tmp2;
    }
};
