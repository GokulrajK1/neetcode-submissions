class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {return false;}

        unordered_map<char, int> counts_s {};
        unordered_map<char, int> counts_t {};
        
        auto it_s = s.begin();
        auto it_t = t.begin(); 

        while (it_s != s.end() && it_t != t.end()) {
            counts_s[*it_s]++;
            counts_t[*it_t]++;
            ++it_s;
            ++it_t;
        }

        return counts_s == counts_t;



    }
};
