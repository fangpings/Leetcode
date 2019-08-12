class Solution(object):
    def reverseWords(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        s.reverse()
        last = 0
        for i in range(len(s)):
            if s[i] == ' ':
                word = s[last:i]
                word.reverse()
                s[last:i] = word
                last = i + 1
        word = s[last:]
        word.reverse()
        s[last:] = word

if __name__ == '__main__':
    sol = Solution()
    s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
    sol.reverseWords(s)
    print(s)

