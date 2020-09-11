'''
Question:
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

Solution:
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_list = [0] * len(nums)
        min_list = [0] * len(nums)
        max_list[0] = nums[0]
        min_list[0] = nums[0]
        for i in range(1,len(nums)):
            max_list[i] = max(max(max_list[i-1]*nums[i],min_list[i-1]*nums[i]),nums[i])
            min_list[i] = min(min(min_list[i-1]*nums[i],nums[i]),max_list[i-1]*nums[i])
        return max(max_list)
