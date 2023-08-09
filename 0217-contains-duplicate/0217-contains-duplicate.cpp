class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> numSet;  // Create a hash table (unordered_set) to store unique numbers

        for (int num : nums) {
            if (numSet.find(num) != numSet.end()) {
                return true;  // If the number already exists in the set, it's a duplicate
            }
            numSet.insert(num);  // Add the number to the set
        }

        return false;  // If no duplicates were found
    }
};
