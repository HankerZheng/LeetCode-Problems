# A frog is crossing a river. The river is divided into x units and at each unit there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

# Given a list of stones' positions (in units) in sorted ascending order, determine if the frog is able to cross the river by landing on the last stone. Initially, the frog is on the first stone and assume the first jump must be 1 unit.

# If the frog's last jump was k units, then its next jump must be either k - 1, k, or k + 1 units. Note that the frog can only jump in the forward direction.

# Note:

# Each stone's position will be a non-negative integer < 231.
# The first stone's position is always 0.
# Example 1:

# [0,1,3,5,6,8,12,17]

# There are a total of 8 stones.
# The first stone at the 0th unit, second stone at the 1st unit,
# third stone at the 3rd unit, and so on...
# The last stone at the 17th unit.

# Return true. The frog can jump to the last stone by jumping 
# 1 unit to the 2nd stone, then 2 units to the 3rd stone, then 
# 2 units to the 4th stone, then 3 units to the 6th stone, 
# 4 units to the 7th stone, and 5 units to the 8th stone.
# Example 2:

# [0,1,2,3,4,8,9,11]

# Return false. There is no way to jump to the last stone as 
# the gap between the 5th and 6th stone is too large.

class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        def mem_search(last_jump, cur_pos):
            if (last_jump, cur_pos) in history:
                return history[(last_jump, cur_pos)]
            if cur_pos == dest:
                return True
            ans = False
            for dx in delta:
                this_jump = last_jump + dx
                if this_jump > 0 and cur_pos + this_jump in stone_set:
                    ans |= mem_search(this_jump, index)

            history[(last_jump, cur_pos)] = ans
            return ans
        
        history = {}
        stone_set = set(stones)
        dest = stones[-1]
        delta = [1, 0, -1]
        return mem_search(0, 0)

if __name__ == '__main__':
    sol = Solution()