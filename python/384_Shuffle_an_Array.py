# Shuffle a set of numbers without duplicates.

# Example:

# // Init an array with set 1, 2, and 3.
# int[] nums = {1,2,3};
# Solution solution = new Solution(nums);

# // Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
# solution.shuffle();

# // Resets the array back to its original configuration [1,2,3].
# solution.reset();

# // Returns the random shuffling of array [1,2,3].
# solution.shuffle();
# Subscribe to see which companies asked this question

class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type size: int
        """
        self._original = list(nums)
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self._original

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        import random
        res = list(self._original)
        length = len(res)
        for i in xrange(length):
            rand_num = random.randrange(i, length)
            res[i], res[rand_num] = res[rand_num], res[i]
        return res
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

# if __name__ == '__main__':
#     sol = Solution(range(3))
#     for i in xrange(100):
#         print sol.shuffle()