# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
# representing the number of elements in nums1 and nums2, respectively.
# Merge nums2 into nums1 so that the resulting array is sorted in non-decreasing order.
# The final sorted array should not be returned by the function but instead, modify nums1 in-place.

# Input: nums1 = [1, 2, 3, 0, 0, 0], m = 3, nums2 = [2, 5, 6], n = 3
# Output: nums1 = [1, 2, 2, 3, 5, 6]

# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: nums1 = [1]

# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: nums1 = [1]

def merge(nums1, m, nums2, n):
    # Initialize pointers
    p1 = m - 1  # Last initialized element in nums1
    p2 = n - 1  # Last element in nums2
    p = m + n - 1  # Last position in nums1

    # While there are elements to compare
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    # If there are remaining elements in nums2
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1

# Example Usage
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)  # Output: [1, 2, 2, 3, 5, 6]

nums1 = [0]
m = 0
nums2 = [1]
n = 1
merge(nums1, m, nums2, n)
print(nums1)  # Output: [1]

