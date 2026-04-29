class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()){ // if they dont have the same length no chance of same characters automatic false statement 
            return false;
        }
        
        unordered_map<char, int> countS;
        unordered_map<char, int> countT;

        for (int i = 0; i < s.length(); i++){ //doesn't matter if s.length or t.length they should be the same 
            countS[s[i]]++;
            countT[t[i]]++;

        }
        return countS == countT;


        
    }
};

// sort given strings and check for equality
//hash map, .contains function 



