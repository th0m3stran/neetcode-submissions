class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {

        int n = temperatures.size();
        stack<int> st; //stores indices 
        vector<int> result(n,0); // n = max size of the vector initialise with 0

        for (int i = 0; i < n; i++){ // Looping through each day 
            // current day is warmer than the day on top of the stack
            while (!st.empty() && temperatures[i] > temperatures[st.top()]){ // Not empty, current temperature greater than previous day temp 
                int oldIndex = st.top();
                st.pop(); 

                result[oldIndex] = i - oldIndex;
            }

            //Current day now waits for a warmer future day 
            st.push(i);



        }

        return result;

        
    }
};
 
// We go through each day from left to right (only looking at future days)
// Stack stores indicies of days still waiting for warmer day 

//For each current day: 
//If today's temperature is warmer than the day on top of the stack, 
//Pop that previous day because we found its answer 

// Calculate how many days it waited (current index - previous index)

//Keep doing this while temperatures[i] > temperatures[st.top]