def groupAnagrams(strs):
    # index = {}
    # for i, c in enumerate("abcdefghijklmnopqrstuvwxyz"):
    #     index[c] = 1 << i
    ret = []
    ret_index = {}
    current_index = 0
    for s in strs:
        tmp = ''.join(sorted(s))
        if tmp not in ret_index:
            ret_index[tmp] = current_index
            ret.append([s])
            current_index += 1
        else:
            ret[ret_index[tmp]].append(s)
    return ret

if __name__ == '__main__':
    print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))