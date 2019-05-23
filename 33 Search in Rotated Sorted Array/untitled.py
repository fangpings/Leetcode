def search(nums, target):
    def recursive(nums, target, base):
        print(nums, base)
        def binary_search(nums, target, base):
            print(nums, base)
            if len(nums) <= 3:
                for i, n in enumerate(nums):
                    if n == target:
                        return base + i
                return -1

            mid = len(nums) // 2
            if target == nums[mid]:
                return base + mid
            elif target < nums[mid]:
                return binary_search(nums[:mid], target, base)
            else:
                return binary_search(nums[mid+1:], target, base + mid +1)

        if len(nums) <= 3:
            for i, n in enumerate(nums):
                if n == target:
                    return base + i
            return -1

        left, right = 0, len(nums) - 1
        mid = right // 2
        if nums[left] <= nums[mid] and nums[mid] <= nums[right]:
            # in right order
            return binary_search(nums, target, base)
        elif nums[left] > nums[mid]:
            # left part not in right order
            if target == nums[mid]:
                return base + mid
            elif target < nums[mid] or target > nums[right]:
                # target not in right part
                return recursive(nums[:mid], target, base)
            else:
                # target in right part
                return binary_search(nums[mid+1:], target, mid + base + 1)
        else:
            # right part not in right order
            if target == nums[mid]:
                return base + mid
            elif target < nums[left] or target > nums[mid]:
                return recursive(nums[mid+1:], target, base + mid + 1)
            else:
                return binary_search(nums[:mid], target, base)
    return recursive(nums, target, 0)
if __name__ == '__main__':
    print(search([1,2,3,4,5], 5))
    # print(search(list(range(100, 200))+list(range(100)), 0))