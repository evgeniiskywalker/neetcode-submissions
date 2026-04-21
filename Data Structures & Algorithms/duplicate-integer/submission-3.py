class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates = {}

        for num in nums:
            if num not in duplicates:
                duplicates[num] = 1
            else:
                duplicates[num] = duplicates.get(num) + 1

            if duplicates[num] > 1:
                return True
        
        return False