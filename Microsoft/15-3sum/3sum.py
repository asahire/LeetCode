class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # n = len(nums)
        # res = set()

        # for i in range(n):
        #     for j in range(i+1, n):
        #         for k in range(j+1, n):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 res.add(tuple(sorted((nums[i], nums[j], nums[k]))))
        
        # return [list(t) for t in res]
        
        nums.sort()
        n = len(nums)
        res = []
       
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left, right = i+1, n-1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                  
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right-1]:
                        right -= 1

                    left += 1
                    right -= 1


        return res               