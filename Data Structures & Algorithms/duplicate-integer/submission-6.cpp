

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> uniques {}; 
        for (auto itr = nums.begin(); itr != nums.end(); itr++) {
            if (uniques.find(*itr) != uniques.end()) {
                return true;
            } else {
                uniques.insert(*itr);
            }
        }
        return false; 
    }
};
