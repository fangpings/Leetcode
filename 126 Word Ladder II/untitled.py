from collections import defaultdict

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        begin = {beginWord: [[beginWord]]}
        end = {endWord: [[endWord]]}
        if endWord not in wordList:
            return []
        wordList = set(wordList)
        ret = []
        flag = False
        order = True
        while begin and end:
            if len(begin) > len(end):
                begin, end = end, begin
                order = not order
            temp = defaultdict(list)
            for word, history in begin.items():
                wordList.discard(word)
                for i, c in enumerate(word):
                    left, right = word[:i], word[i + 1:]
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        next_word = left + char + right
                        if next_word in end:
                            # ret.append(history + end[next_word] if order else end[next_word] + history)
                            if order:
                                ret += [h1 + h2 for h1 in history for h2 in end[next_word]]
                            else:
                                ret += [h2 + h1 for h1 in history for h2 in end[next_word]]
                            flag = True
                        if next_word in wordList:
                            if order:
                                temp[next_word] += [h + [next_word] for h in history]
                            else:
                                temp[next_word] += [[next_word] + h for h in history]
            if flag:
                return ret
            begin = temp 
        # while begin:
        #     temp = defaultdict(list)
        #     for word, history in begin.items():
        #         wordList.discard(word)
        #         for i, c in enumerate(word):
        #             left, right = word[:i], word[i + 1:]
        #             for char in 'abcdefghijklmnopqrstuvwxyz':
        #                 next_word = left + char + right
        #                 if next_word == endWord:
        #                     ret += [h + [endWord] for h in history]
        #                     flag = True
        #                 if next_word in wordList:
        #                     temp[next_word] += [h + [next_word] for h in history]
        #     if flag:
        #         return ret
        #     begin = temp 
        return ret

if __name__ == '__main__':
    sol = Solution()
    print(sol.findLadders("magic", "pearl", ["flail","halon","lexus","joint","pears","slabs","lorie","lapse","wroth","yalow","swear","cavil","piety","yogis","dhaka","laxer","tatum","provo","truss","tends","deana","dried","hutch","basho","flyby","miler","fries","floes","lingo","wider","scary","marks","perry","igloo","melts","lanny","satan","foamy","perks","denim","plugs","cloak","cyril","women","issue","rocky","marry","trash","merry","topic","hicks","dicky","prado","casio","lapel","diane","serer","paige","parry","elope","balds","dated","copra","earth","marty","slake","balms","daryl","loves","civet","sweat","daley","touch","maria","dacca","muggy","chore","felix","ogled","acids","terse","cults","darla","snubs","boats","recta","cohan","purse","joist","grosz","sheri","steam","manic","luisa","gluts","spits","boxer","abner","cooke","scowl","kenya","hasps","roger","edwin","black","terns","folks","demur","dingo","party","brian","numbs","forgo","gunny","waled","bucks","titan","ruffs","pizza","ravel","poole","suits","stoic","segre","white","lemur","belts","scums","parks","gusts","ozark","umped","heard","lorna","emile","orbit","onset","cruet","amiss","fumed","gelds","italy","rakes","loxed","kilts","mania","tombs","gaped","merge","molar","smith","tangs","misty","wefts","yawns","smile","scuff","width","paris","coded","sodom","shits","benny","pudgy","mayer","peary","curve","tulsa","ramos","thick","dogie","gourd","strop","ahmad","clove","tract","calyx","maris","wants","lipid","pearl","maybe","banjo","south","blend","diana","lanai","waged","shari","magic","duchy","decca","wried","maine","nutty","turns","satyr","holds","finks","twits","peaks","teems","peace","melon","czars","robby","tabby","shove","minty","marta","dregs","lacks","casts","aruba","stall","nurse","jewry","knuth"]))
