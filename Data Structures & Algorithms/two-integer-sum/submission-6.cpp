class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> differences {}; 
        int length = nums.size();
        for (int i = 0; i < length; ++i) {
            auto it = differences.find(nums[i]);
            if (it != differences.end()) {
                vector<int> res = {it->second, i};
                return res;
            } 
            
            differences[target - nums[i]] = i; 
        }
    }
};
