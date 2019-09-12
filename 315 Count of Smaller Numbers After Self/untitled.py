# class Solution:
#     def countSmaller(self, nums):
#         if not nums:
#             return []
#         l = len(nums)
#         ret = [0 for _ in range(l)]
#         bigger = [[] for _ in range(l)]
#         for i in range(l - 2, -1, -1):
#             j = i + 1
#             while j < l and nums[j] >= nums[i]:
#                 bigger[i].append(nums[j])
#                 j += 1
#             if j < l:
#                 ret[i] += ret[j] + 1
#                 for num in bigger[j]:
#                     if num < nums[i]:
#                         ret[i] += 1
#                     else:
#                         bigger[i].append(num)
#         return ret

class Solution:
    def countSmaller(self, nums):
        def sort(enum):
            half = len(enum) // 2
            if half:
                left, right = sort(enum[:half]), sort(enum[half:])
                for i in range(len(enum))[::-1]:
                    if not right or left and left[-1][1] > right[-1][1]:
                        smaller[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            print(smaller)
            return enum
        smaller = [0] * len(nums)
        sort(list(enumerate(nums)))
        return smaller

if __name__ == '__main__':
    sol = Solution()
    print(sol.countSmaller([7,2,6,3]))