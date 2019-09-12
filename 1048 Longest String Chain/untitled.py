from collections import defaultdict

class Solution:
    def longestStrChain(self, words):
        if not words:
            return 0
        hashmap = defaultdict(list)
        for word in words:
            hashmap[len(word)].append(word)
        keys = sorted(hashmap.keys(), reverse=True)
        hashmap[keys[0]] = [(x, 1) for x in hashmap[keys[0]]]
        global_max = 1
        for i in range(1, len(keys)):
            for j in range(len(hashmap[keys[i]])):
                tmp_max = 0
                for last_key, max_chain in hashmap[keys[i-1]]:
                    if self.chain(hashmap[keys[i]][j], last_key):
                        tmp_max = max(tmp_max, max_chain)
                hashmap[keys[i]][j] = (hashmap[keys[i]][j], tmp_max + 1)
                global_max = max(global_max, tmp_max + 1)
        return global_max

    def chain(sefl, word1, word2):
        for i in range(len(word2)):
            if word1 == word2[:i] + word2[i+1:]:
                return True
        return False

if __name__ == '__main__':
    sol = Solution()
    print(sol.longestStrChain(["a",'ab', 'aa']))




