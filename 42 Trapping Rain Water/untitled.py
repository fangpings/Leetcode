def trap(height):
    l = len(height)
    left = right = 0
    tmp_max = 0
    minus = 0
    for i, h in enumerate(height):
        if h > tmp_max:
            tmp_max = h
            left = right = i
        elif h == tmp_max:
            right = i
    while left > 0 or right < l - 1:
        tmp_max = 0
        tmp_max_index = 0
        for i in range(left):
            if height[i] > tmp_max:
                tmp_max = height[i]
                tmp_max_index = i
        minus += left * (height[left] - tmp_max)
        left = tmp_max_index

        tmp_max = 0
        tmp_max_index = l - 1
        for i in range(right + 1, l):
            if height[i] >= tmp_max:
                tmp_max = height[i]
                tmp_max_index = i
        minus += (l - 1 - right) * (height[right] - tmp_max)
        right = tmp_max_index
    return max(height) * l - sum(height) - minus

if __name__ == '__main__':
    print(trap([1]))
