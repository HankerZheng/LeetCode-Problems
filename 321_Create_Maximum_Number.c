/*
Given two arrays of length m and n with digits 0-9 representing two numbers. Create the maximum number of length k <= m + n from digits of the two. The relative order of the digits from the same array must be preserved. Return an array of the k digits. You should try to optimize your time and space complexity.

Example 1:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
return [9, 8, 6, 5, 3]

Example 2:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
return [6, 7, 6, 0, 4]

Example 3:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
return [9, 8, 9]

Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.

Subscribe to see which companies asked this question
*/

/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */

// for each solution, there could be i numbers chosen from nums1 and (k - i) numbers chosen from nums2

int* maxNumber(int* nums1, int nums1Size, int* nums2, int nums2Size, int k, int* returnSize) {

	int i;

	if(k == 0)
		return NULL;

	for(i =0; i<= k; i ++)
	{
		//whether there is enough numbers to choose from the given nums1 or nums2
		if(i > nums1Size)
			break;
		if((k - i) > nums2Size)
			continue;

		//choose i numbers from nums1
		//get the biggest number from the first (nums1Size - i) nums
		for(j = 0; )

		//choose (k-i) numbers from nums2
		//get the biggest number from the first (nums2Size - (k-i)) nums

	}
    
}