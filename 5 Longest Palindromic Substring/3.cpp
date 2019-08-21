#include <vector>
#include <string>
#include <iostream>
using namespace std;

class Solution {
public:
    string longestPalindrome(string s) {
        int len = s.length();
        if(len < 1){
            return string();
        }
        string ret(1, s[0]);
        vector<vector<int>> dp(len, vector<int>(len, 0));
        for(int i = 0; i < len; ++i){
            dp[i][i] = 1;
        }
        for(int i = 0; i < len - 1; ++i){
            if(s[i] == s[i+1]){
                dp[i][i+1] = 1;
                ret = s.substr(i, 2);
            }
        }
        for(int l = 2; l < len; ++l){
            for(int i = 0; i + l < len; ++i){
                dp[i][i+l] = int(dp[i+1][i+l-1] && s[i] == s[i+l]);
                // cout << i << l << dp[i][i+l] << endl;
                if(dp[i][i+l]){
                    ret = s.substr(i, l+1);
                }
            }
        }
        return ret;
    }
};

int main(){
    Solution sol;
    cout << sol.longestPalindrome("");
}

