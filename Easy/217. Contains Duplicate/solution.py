class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        existing = set() # define an empty set to track numbers

        for num in nums: # loop through nums list
            if num in existing:
                return True # return true if duplicate number is found 
            existing.add(num) # add number to set

        return False # no duplicates, return false