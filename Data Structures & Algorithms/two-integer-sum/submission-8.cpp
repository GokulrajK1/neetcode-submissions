class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> differences {}; 
        int length = nums.size();
        for (int i = 0; i < length; ++i) {
            if (differences.find(nums[i]) != differences.end()) {
                return {differences[nums[i]], i};
            } 
            
            differences[target - nums[i]] = i; 
        }
    }
};
