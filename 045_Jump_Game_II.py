# Given an array of non-negative integers, you are initially
# positioned at the first index of the array.

# Each element in the array represents your maximum jump length
# at that position.

# Your goal is to reach the last index in the minimum number of jumps.

# For example:
# Given array A = [2,3,1,1,4]

# The minimum number of jumps to reach the last index is 2.
# (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

# Note:
# You can assume that you can always reach the last index.

# Subscribe to see which companies asked this question

# KeyPoints: Assume now we stand at posi `posi`,
#            we gonna jump to the point that could reach max.
#            That is, search through nums[posi:posi+num[posi]]
# Runtime: 90ms

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        current_posi = 0
        count = 0
        reach = current_posi + nums[current_posi]
        dest = len(nums)-1

        # jump while not reach dest
        while current_posi < dest:
            jump_to = current_posi # don't jump if can't reach further
            # search all the possible reach
            for jump in xrange(1, nums[current_posi]+1):
                next_posi = current_posi+jump # if jump to next_posi
                if next_posi >= dest:
                    # this jump can reach dest
                    return count+1
                # if can reach further, update jump_to position 
                if next_posi+nums[next_posi] > reach:
                    reach = next_posi+nums[next_posi]
                    jump_to = next_posi
            if jump_to == current_posi:
                # no possible jump can reach more far
                # dest can't be reached
                return -1
            current_posi = jump_to
            count +=1
        return count




if __name__ == '__main__':
    sol = Solution()
    print sol.jump([])
    print sol.jump([3,2,1,0,1])
    print sol.jump([3])
    print sol.jump([3,2,1,4])
    print sol.jump([1,1,1,1,1,1,1])
    print sol.jump([2,1])
