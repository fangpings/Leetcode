class Solution:
    def partitionLabels(self, S):
        record = {}
        for i in range(len(S)):
            if S[i] not in record:
                record[S[i]] = [i, i]
            else:
                record[S[i]][1] = i
        record = [item for _, item in record.items()]
        record.sort(key=lambda x:x[0])
        i = 0
        while i < len(record) - 1:
            if record[i+1][1] <= record[i][1]:
                record.pop(i+1)
            elif record[i+1][0] <= record[i][1]:
                record[i][1] = record[i+1][1]
            else:
                i += 1
        return [y - x + 1 for x, y in record]

if __name__ == '__main__':
    sol = Solution()
    print(sol.partitionLabels("abcd"))

