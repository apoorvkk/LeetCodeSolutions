class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        
        
        ....X...
        
        
        X > 0:
            i can keep moving on
        X == 0:
            i am done
            
            
        [1, 4, 2, 1, 0, 1, 2, 1, 4]
        
        
        curr_zero_index = 4
        
        [0,0,0]
        """
        if len(nums) in (0,1):
            return True
        
        curr_zero_index = None
        
        # [1, 2]
        for i in range(len(nums)-2, -1, -1):
            if curr_zero_index:
                jump_needed = curr_zero_index - i + 1
                if nums[i] >= jump_needed:
                    curr_zero_index = None
            elif nums[i] == 0:
                    curr_zero_index = i
        
        return True if curr_zero_index is None else False
        