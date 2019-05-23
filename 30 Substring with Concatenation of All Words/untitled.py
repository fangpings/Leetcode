from collections import defaultdict
import copy
import time

def findSubstring(s, words):
    if words == []:
        return []
    length = len(words[0])
    nums = len(words)
    dic = defaultdict(int)
    for word in words:
        dic[word] += 1
    i = 0
    ret = []
    black_list = [0 for _ in range(len(s))]
    while i <= len(s) - length * nums:
        print('test', i, black_list[i])
        if black_list[i] == 0:
            tmp_dic = copy.deepcopy(dic)
            subs = s[i:i + length * nums]
            l = length * nums
            j = 0
            while j < l:
                if black_list[i+j] != 0:
                    print(2)
                    break
                if tmp_dic[subs[j:j+length]] > 0:
                    tmp_dic[subs[j:j+length]] -= 1
                    j += length
                else:
                    print(1)
                    if dic[subs[j:j+length]] == 0:
                        black_list[i + j] = 1
                        print('blacklist', i+j, black_list[i+j])
                    break
            if j == l:
                ret.append(i)
        else:
            print(2)
        i += 1
    return ret

if __name__ == '__main__':
    print(findSubstring("ababababababababababababababab", ["aba","bab"]))