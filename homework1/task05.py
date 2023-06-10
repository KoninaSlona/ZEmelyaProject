"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
def find_maximal_subarray_sum(nums: list[int], k: int) -> int:
    
    # create storage of sum
    sum_value = -(2**31-1)
    
    # a loop that iterates over the lengths of subarrays 
    for index in range(1, k):
        # цикл перебора чисел листа 
        for num_index in range(0, len(nums)):
            # variable maximum subarray length
            nums_max_len = num_index+index+1
            # checking if we have gone beyond the array boundaries
            if (nums_max_len>len(nums)):
                continue
            # put the value of the sum of the subarray into a variable 
            temp_sum=sum([nums[i] for i in range(num_index, nums_max_len)])
            # checking whether the calculated value is greater than what was or not
            if (sum_value<temp_sum):
                sum_value=temp_sum
    return sum_value