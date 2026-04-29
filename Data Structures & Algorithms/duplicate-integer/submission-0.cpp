#include <unordered_map>

using namespace std;

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, int> freq;

        int n = nums.size();
        int count; 

        for (int i = 0; i < n; i++){ //starting at index 0 we loop increasing index each time
            if (freq.contains(nums[i])){ //hashmap checks if value at key exists 
                return true; //
            }

            freq[nums[i]] = i; 
        }

        return false;

   
        
    }
};

//we have a map 
// we have i indicating to index 0; each time we pass we increase index 
// map checks if value exists in any of the indexes 
// if exists return true; if doesn't exist we return false

