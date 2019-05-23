class Solution:
    def simplifyPath(self, path):
        # just use split('/')
        l = len(path)
        stack = []
        i = 0
        while i < l:
            i += 1
            while i < l and path[i] == '/':
                i += 1
            tmp = ''
            while i < l and path[i] != '/':
                tmp += path[i]
                i += 1
            if tmp == '..':
                if stack != []:
                    stack.pop()
            elif tmp not in ('', '.'):
                stack.append('/' + tmp)
        if stack == []:
            return '/'
        return ''.join(stack)

if __name__ == '__main__':
    sol = Solution()
    print(sol.simplifyPath('/a//b////c/d//././/..'))





