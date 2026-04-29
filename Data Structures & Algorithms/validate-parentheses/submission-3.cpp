class Solution {
public:
    bool isValid(string s) {
        stack<char> st; 

        for (char c : s){
            if (c == '(' || c == '{' || c == '['){
                st.push(c);
            } else {
                if (st.empty()){ // False statement 1: Empty 
                    return false;
                }

                //False statement 2: not a match
                if ((c == ')' && st.top() != '(') ||(c == '}' && st.top() != '{') || (c == ']' && st.top() != '[')){
                    return false;
                }

                st.pop(); // match found 
            }
        }

        return st.empty(); // returns true if valid parenthesis 
    }
};
