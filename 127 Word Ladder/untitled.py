from collections import defaultdict

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(len(beginWord)):
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)
        queue = [(beginWord, 1)]
        visited = []
        while queue:
            current, steps = queue.pop(0)
            for i in range(len(beginWord)):
                for next_word in all_combo_dict[current[:i] + '*' + current[i+1:]]:
                    if next_word == endWord:
                        return steps + 1
                    if next_word not in visited:
                        queue.append((next_word, steps + 1))
                        visited.append(next_word)
                all_combo_dict[current[:i] + '*' + current[i+1:]] = []
        return 0

        # stack = [beginWord]
        # min_steps = 1000000
        # recorder = defaultdict(int)
        # while stack:
        #     tmp = stack[-1]
        #     if recorder[tmp] < len(next_map[tmp]):
        #         current = next_map[tmp][recorder[tmp]]
        #         if current not in stack:
        #             if current == endWord:
        #                 if len(stack) + 1 < min_steps:
        #                     min_steps = len(stack) + 1
        #                 stack.pop()
        #                 recorder[tmp] = 0
        #             else:
        #                 stack.append(current)
        #                 recorder[tmp] += 1
        #         else:
        #             recorder[tmp] += 1
        #     else:
        #         recorder[tmp] = 0
        #         stack.pop()
        # return 0

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        begin = set([beginWord])
        end = set([endWord])
        words = set(wordList)
        if endWord not in words:
            return 0
        dis = 1
        while begin and end:
            if len(begin) > len(end):
                begin, end = end, begin
            temp = set()
            for word in begin:
                for i, c in enumerate(word):
                    left, right = word[:i], word[i + 1:]
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        next_word = left + char + right
                        if next_word in end:
                            return dis + 1
                        if next_word in words:
                            words.discard(next_word)
                            temp.add(next_word)
            begin = temp
            dis += 1
        
        return 0


if __name__ == '__main__':
    sol = Solution()
    print(sol.ladderLength('hit', 'cog', ["hot","dot","dog","lot","log","cog"]))



 