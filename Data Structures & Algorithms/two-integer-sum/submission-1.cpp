using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> numMap;
        int n = nums.size(); 

        for (int i = 0; i < n; i++){
            int find = target -  nums[i];
            if (numMap.count(find)){ //does this 'find' nubmer exist in the hashmap already?
                return {numMap[find], i}; //if it does, reutnr the index of where
            }
            numMap[nums[i]] = i; //If not, add the number at index i at the hashmap
        }

        return {}; //No solution found 
        
        
    }
};




