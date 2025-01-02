# Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target.
# You may assume that each input has exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]
# Explanation: nums[0] + nums[1] = 2 + 7 = 9.

# Input: nums = [3, 2, 4], target = 6
# Output: [1, 2]

# Input: nums = [3, 3], target = 6
# Output: [0, 1]

def two_sum(nums, target):
    # Create a dictionary to store numbers and their indices
    num_map = {}

    # Iterate through the array
    for i, num in enumerate(nums):
        # Calculate the complement
        complement = target - num

        # Check if the complement exists in the dictionary
        if complement in num_map:
            return [num_map[complement], i]

        # Store the current number and its index in the dictionary
        num_map[num] = i

# Example Usage
nums1 = [2, 7, 11, 15]
target1 = 9
print(two_sum(nums1, target1))  # Output: [0, 1]

nums2 = [3, 2, 4]
target2 = 6
print(two_sum(nums2, target2))  # Output: [1, 2]

nums3 = [3, 3]
target3 = 6
print(two_sum(nums3, target3))  # Output: [0, 1]

