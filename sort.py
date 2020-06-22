



import numpy as np

class Solution:
    def sort(self, nums):
        # n = len(nums)
        for i in range(len(nums)): # first
            for j in range(i, len(nums)): # second
                # move the bigger one to the end
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        return nums



    def brick_wall(self, bricks):
        '''
        :param bricks: list of lists
        :return:
        '''
        height = len(bricks)
        # width = len(bricks[0])
        real_width = sum(bricks[0]) # total length of each layer
        new_bricks = [[0]*(real_width+2) for _ in range(height)]

        for i in range(height): # 0
            for j in range(len(bricks[i])): # 0
                val = bricks[i][j] # 1
                for x in range(j+1, j+1+val): #
                    new_bricks[i][x] = 1

        print (np.array(new_bricks))
        return min(np.sum(np.array(new_bricks), axis = 1))


sol = Solution()
# print (sol.sort([5,2,1,5,6,8]))

# 2
print (sol.brick_wall([
       [1,2,2,1],
       [3,1,2],
       [1,3,2],
       [2,4],
       [3,1,2],
       [1,3,1,1]]))
