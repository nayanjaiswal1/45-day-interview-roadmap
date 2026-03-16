class Solution:
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))

    def containsDuplicate2(self,nums):
        seen = ()
        for i in nums:
            if i in seen :
                return True
            seen.add(i)
        
        return False