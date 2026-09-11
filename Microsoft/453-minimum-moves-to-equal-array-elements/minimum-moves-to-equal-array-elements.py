class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # nums = list(nums)
        # moves = 0
        # while len(set(nums)) > 1:
        #     max_num= max(nums)
        #     idx = nums.index(max_num)

        #     for i in range(len(nums)):
        #         if i != idx:
        #             nums[i] += 1
                
        #     moves +=1
        
        # return moves

        lo = min(nums)
        return sum(x - lo for x in nums)

        