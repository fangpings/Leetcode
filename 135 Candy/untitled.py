class Solution:
    def candy(self, ratings):
        descending = -1
        total = 0
        ratings = [-100000] + ratings
        max_descending = 0
        current = 0
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                current += 1
                total += current
                descending = -1
                max_descending = current - 1
            elif ratings[i] == ratings[i-1]:
                current = 1
                total += current
                descending = -1
                max_descending = current - 1
            else:
                current = 1
                descending += 1
                if descending >= max_descending:
                    descending += 1
                    max_descending = 10000000
                total += current + descending
        return total

if __name__ == '__main__':
    sol = Solution()
    print(sol.candy([1,2,2,3,3,2,2,1]))
