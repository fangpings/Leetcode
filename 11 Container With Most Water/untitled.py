def maxArea(height) -> int:
    left = 0
    right = len(height) - 1
    maxArea = 0
    while left < right:
        cur = (right - left) * min(height[left], height[right])
        if cur > maxArea:
            maxArea = cur
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return maxArea
if __name__ == '__main__':
    print(maxArea([1,8,6,2,5,4,8,3,7])==49)
    print(maxArea([1,7])==1)

