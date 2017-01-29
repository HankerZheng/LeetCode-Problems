/*
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note: 
(1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
(2) 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

Example:

Given [3, 1, 5, 8]

Return 167

    nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
   coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.

Subscribe to see which companies asked this question

Show Tags
*/

//score[i][j] represents the max score you can get from balloon[i] to balloon[j], included.
//score[i][j] = max(score[i][k-1] + nums[k]*nums[i-1]*nums[j+1] + score[k+1][j])
//let k be the last balloon to burst in the range from i to j

#define nums(a)	( ( (a<numsSize)&&(a>=0) )? nums[a] : 1 )
#define score(a,b) ( (a<=b)? score[a][b]:0 )
#define max(a,b) ((a>b)?a:b)

int maxCoins(int* nums, int numsSize) {
    
    int **score;
    int i,k;
    int left, right;
    int max, temp;

    score = (int**)malloc(sizeof(int*) * numsSize);
    memset(score, 0, sizeof(int*)*numsSize/sizeof(char));

    score[0] = (int*)malloc(sizeof(int)*numsSize*numsSize);
    memset(score[0], 0, sizeof(int) * numsSize * numsSize / sizeof(char));
    for(i = 1; i < numsSize; i++)
	{
		score[i] = score[i-1] + numsSize;
	}

	for(k = 0; k < numsSize; k ++)
	{
		for(left = 0; (left+k)< numsSize; left ++ )
		{
		    right = left + k;
			max = 0;
			for(i = left; i <= right; i++)
			{
				temp = score(left,i-1) + nums(left-1)*nums(i)*nums(right+1)+score(i+1,right);
				max = max(temp,max);
			}
			score[left][right] = max;
		}
	}

	max = score[0][numsSize-1];

	free(score[0]); 
	free(score);

	return max;


}