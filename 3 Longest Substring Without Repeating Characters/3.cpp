#include <string>
#include <iostream>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if(s.length() == 0){
            return 0;
        }
        int max_len = 1;
        string current_long;
        for (auto &c : s)
        {
            auto pos = current_long.find_last_of(c);
            if(pos == string::npos){
                current_long.append(1, c);
            }else{
                current_long = current_long.substr(pos + 1).append(1, c);
            }
            max_len = current_long.length() > max_len ? current_long.length() : max_len;
        }
        return max_len;
    }
};

int main(){
    Solution sol;
    cout << sol.lengthOfLongestSubstring("pwwkew");
}