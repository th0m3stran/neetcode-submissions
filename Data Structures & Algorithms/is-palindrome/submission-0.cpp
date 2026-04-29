#include <cctype> //analyse characters 
#include <string>

using namespace std;

class Solution {
public:
    bool isPalindrome(string s) {
        int left = 0; 
        int right = s.size() - 1; //end of the array

        while (left < right){
            //skip non-alphanumeric from left 
            while (left < right && !isalnum(s[left])){
                left++;
            }

            //skip non-alphanumeric from right 
            while (left < right && !isalnum(s[right])){
                right--;
            }

            //compare lowercase
            if (tolower(s[left]) != tolower(s[right])){
                return false;
            }

            left++;
            right--;
        }


        return true;

        

    }
};

//1. Iron out the spaces, nonalphanumeric, case sensitivity 
//2. Pointer left and right, left++ right--


