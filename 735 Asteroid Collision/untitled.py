class Solution:
    def asteroidCollision(self, asteroids):
        stack = []
        for a in asteroids:
            if stack and a < 0:
                while stack and stack[-1] > 0 and stack[-1] < -a:
                    stack.pop()
                if stack and stack[-1] == -a:
                    stack.pop()
                elif not stack or stack[-1] < 0:
                    stack.append(a)
            else:
                stack.append(a)
        return stack

if __name__ == '__main__':
    sol = Solution()
    print(sol.asteroidCollision([-2, -1, 1, 2]))