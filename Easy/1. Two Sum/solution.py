class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index = {} # dictionary to track numbers from initial list and their index values

        for i in range(len(nums)):
            diff = target - nums[i] # diff is the number we want to look for in the map

            if diff in num_index:
                return [num_index[diff], i] # return index value of diff and current index value
            
            num_index[nums[i]] = i # add current number to map with current index value