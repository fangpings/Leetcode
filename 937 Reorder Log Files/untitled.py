class Solution:
    def reorderLogFiles(self, logs):
        letter = []
        digit = []
        for log in logs:
            if log.split(' ')[1].isdigit():
                digit.append(log)
            else:
                letter.append(log)
        letter.sort(key=lambda x:x.partition(' ')[-1] + x.partition(' ')[0])
        return letter + digit

if __name__ == '__main__':
    sol = Solution()
    print(sol.reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]))
