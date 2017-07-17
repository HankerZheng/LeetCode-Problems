/*
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.

Note:
You may assume that you have an infinite number of each kind of coin.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

Subscribe to see which companies asked this question
*/


//have to judge whether amount k is reachable or not!!!

#define coinsCount(a) ( (a<0)? (int32MAX-1): coinsCount[a]) 
#define min(a,b)	(a<b?a:b)
#define int32MAX 2147483647
#define int32MIN -2147483648

int coinChange(int* coins, int coinsSize, int amount) {
    
    int *coinsCount;
    int i,j;
    int minCount, temp;

    if(amount == 0)
        return 0;

    coinsCount = (int*) malloc(sizeof(int) * (amount+1));
    memset(coinsCount, 0, sizeof(int) * (amount+1) /sizeof(char));

    for(i = 1; i <= amount; i ++)
    {
    	minCount = int32MAX;
    	for(j = 0; j < coinsSize; j++)
    	{
    	    if(coinsCount(i-coins[j]) == int32MAX)
    	    //if the amount(i-coins[j]) is unreachable, just skip this coin;
    	        continue;
    		temp = coinsCount(i-coins[j]) + 1;
    		minCount = min(minCount, temp);
    	}
    	coinsCount[i] = minCount;
    }

    free(coinsCount );

    if(minCount ==  int32MAX)
        return -1;
    else
        return minCount;

} 