# You are given two integer arrays nums1 and nums2 sorted
# in ascending order and an integer k.

# Define a pair (u,v) which consists of one element from
# the first array and one element from the second array.

# Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

# Example 1:
# Given nums1 = [1,7,11], nums2 = [2,4,6],  k = 3

# Return: [1,2],[1,4],[1,6]

# The first 3 pairs are returned from the sequence:
# [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
# Example 2:
# Given nums1 = [1,1,2], nums2 = [1,2,3],  k = 2

# Return: [1,1],[1,1]

# The first 2 pairs are returned from the sequence:
# [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
# Example 3:
# Given nums1 = [1,2], nums2 = [3],  k = 3 

# Return: [1,3],[2,3]

# All possible pairs are returned from the sequence:
# [1,3],[2,3]

# Key Points: We could consider all the possible pairs as
#             one array, every pair is a point in this array.
#             The nearest larger pair must be one position near
#             the point already been selected.
#             Therefore, for every new ans point (x,y), we only
#             need to push (x+1,y) and (x, y+1) into heap.
#
#             Be careful, don't push one point more than one times.
#             Use dp to record the points already pushed          
#
# Run Time: 128 ms

from heapq import *

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        def cal_sum(x):
            return nums1[x[0]]+nums2[x[1]]

        if not nums1 or not nums2 or not k:
            return []

        ans, i  = [], 0
        heap = [(cal_sum((0,0)), (0, 0))]
        dp = [-1 for x in xrange(len(nums2))]
        dp[0] = 0

        while heap and i<k:
            index = heappop(heap)[1]
            ans.append([nums1[index[0]],nums2[index[1]]])
            if index[0]<(len(nums1)-1) and dp[index[1]]==index[0]:
                new_index = (index[0]+1, index[1])
                heappush(heap, (cal_sum(new_index),new_index))
                dp[index[1]] += 1
            if index[1]<(len(nums2)-1) and dp[index[1]+1]<index[0]:
                new_index = (index[0], index[1]+1)
                heappush(heap, (cal_sum(new_index),new_index))
                dp[index[1]+1]+=1
            i+=1

        return ans


if __name__ == "__main__":
    test = Solution()
    ans = test.kSmallestPairs([1,7,11],[2,3,6],33)
    print ans
    ans = test.kSmallestPairs([1,1,2],[1,2,3],11)
    print ans