# class Solution:
#     def largestRectangleArea(self, heights):
#         def find_min(nums, start, end):
#             tmp_min = nums[start]
#             tmp_min_index = [start]
#             while start <= end:
#                 if nums[start] < tmp_min:
#                     tmp_min = nums[start]
#                     tmp_min_index = [start]
#                 elif nums[start] == tmp_min:
#                     tmp_min_index.append(start)
#                 start += 1
#             return tmp_min, tmp_min_index
#         def rec(heights, start, end):
#             if start > end:
#                 return
#             if start == end:
#                 return heights[start]
#             tmp_min, tmp_min_index = find_min(heights, start, end)
#             max_area = tmp_min * (end - start + 1)
#             i = 0
#             tmp_min_index = [start-1] + tmp_min_index + [end+1]
#             while i < len(tmp_min_index) - 1:
#                 if tmp_min_index[i] + 1 <= tmp_min_index[i+1] - 1:
#                     tmp_max = rec(heights, tmp_min_index[i] + 1, tmp_min_index[i+1] - 1)
#                     if tmp_max > max_area:
#                         max_area = tmp_max
#                 i += 1
#             return max_area
#         return rec(heights, 0, len(heights) - 1)

class Solution:
    def largestRectangleArea(self, heights):
        heights.append(0)
        stack = [-1]
        ret = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                ret = max(ret, h * w)
            stack.append(i)
        return ret


if __name__ == '__main__':
    sol = Solution()
    print(sol.largestRectangleArea([3,2,1]))

