'''
Given an integer array nums, move all 0's to the end of it while
maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
'''


def move_zeroes(nums: list[int]) -> list[int]:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        i = 0
        
        while i < len(nums) - 1:
            
            if nums[i] == 0:
                j = i + 1
                while nums[j] == 0 and j < len(nums) - 1:
                    j += 1
                    
                nums[i], nums[j] = nums[j], nums[i]
            
            i += 1
            
            
        return nums


if __name__ == "__main__":

    nums = [0,1,0,3,12]
    assert(move_zeroes(nums) == [1,3,12,0,0])