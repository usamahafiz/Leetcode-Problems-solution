class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int currSum = 0;
        int maxSum = INT_MIN; //means negative maximum value
        for (int val : nums) {
            currSum += val;
            maxSum = max(currSum, maxSum); //compare the maximum value between currSum and maxSum
            if (currSum < 0) {
                currSum = 0; // if value is in negative then reset it to zero
            }
        }
        return maxSum;
    }
};