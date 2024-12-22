# Given an array of integers. Write a function to return the sum of all even numbers in the array.
# Input: [1, 2, 3, 4, 5, 6]  
# Output: 12  
# Explanation: 2 + 4 + 6 = 12

def sum_of_evens(arr):
    
    total = 0

    for num in arr:
        if num % 2 == 0:
            
            total += num

    
    return total


input_array = [1, 2, 3, 4, 5, 6]
output = sum_of_evens(input_array)
print(output)  # Output: 12

