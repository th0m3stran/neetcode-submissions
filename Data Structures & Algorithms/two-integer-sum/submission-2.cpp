using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> numMap;

        int n  = nums.size();

        for (int i  = 0; i < n; i++){
            int find = target - nums[i];  //does this 'find' nubmer exist in the hashmap already?
            if (numMap.count(find)){
                return {numMap[find], i}; //If it does, return the index of where
            }
            numMap[nums[i]] = i; //If not, add the number at index i at the hashmap
        }

        return {}; //No solution found 
        
    }
};




