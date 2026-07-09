// Last updated: 7/9/2026, 11:56:12 PM
#include <vector>
#include <unordered_map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // Map to store: value -> index
        std::unordered_map<int, int> numMap;
        
        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            
            // Check if the complement exists in our map
            if (numMap.find(complement) != numMap.end()) {
                return {numMap[complement], i};
            }
            
            // Otherwise, add current number and index to map
            numMap[nums[i]] = i;
        }
        
        // Return empty if no solution is found (though the prompt guarantees one)
        return {};
    }
};