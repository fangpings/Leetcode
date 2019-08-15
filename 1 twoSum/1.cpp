#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> imap;

        for (int i = 0; i < nums.size(); i++)
        {
            int complement = target - nums[i];
            if(imap.find(complement) != imap.end())
            {
                return vector<int> {i, imap[complement]};
            }
            imap[nums[i]] = i;
        }
        return vector<int>();
    }
};

int main(){
    Solution sol;
    vector<int> test {2, 7, 11, 15};
    auto answer = sol.twoSum(test, 9);
    for(auto &i : answer){
        cout << i << endl;
    }
}