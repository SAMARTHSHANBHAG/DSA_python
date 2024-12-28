# Given two integer arrays nums1 and nums2, return an array of their intersection. 
# Each element in the result must appear as many times as it shows in both arrays, and you may return the result in any order.

# Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2]
# Output: [2, 2]

# Input: nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]
# Output: [4, 9]

def intersect(nums1, nums2):
    
    count = {}
    for num in nums1:
        count[num] = count.get(num, 0) + 1

    
    result = []
    for num in nums2:
        if num in count and count[num] > 0:
            result.append(num)
            count[num] -= 1

    return result

# Example Usage
print(intersect([1, 2, 2, 1], [2, 2]))         # Output: [2, 2]
print(intersect([4, 9, 5], [9, 4, 9, 8, 4]))  # Output: [4, 9]

