class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int ans = 0;
        //values in the nums array
        for(int val: nums){
            ans ^= val;
            
        }
        return ans;
        
    }
};