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
                return true; 
            }

            freq[nums[i]] = i; //if not, we need to store it so it remembers 
        }

        return false;

   
        
    }
};


