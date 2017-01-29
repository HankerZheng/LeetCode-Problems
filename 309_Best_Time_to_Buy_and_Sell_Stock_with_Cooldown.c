/*
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

prices = [1, 2, 3, 0, 2]
maxProfit = 3
transactions = [buy, sell, cooldown, buy, sell]
Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.

Subscribe to see which companies asked this question
*/



//DP solution for this question
//there are 3 options you can choose on each day -- buy, sell and hold

#define max(a,b) (a>b?a:b)

int maxProfit(int* prices, int pricesSize) {

	int *buy, *sell, *hold0, *hold1;
	int i;

	if(pricesSize <= 1)
		return 0;

	buy = (int*) malloc(sizeof(int)*pricesSize);
	memset(buy, 0, sizeof(int)/sizeof(char)*pricesSize);
	sell = (int*) malloc(sizeof(int)*pricesSize);
	memset(sell, 0, sizeof(int)/sizeof(char)*pricesSize);
	hold0 = (int*) malloc(sizeof(int)*pricesSize);
	memset(hold0, 0, sizeof(int)/sizeof(char)*pricesSize);
	hold1 = (int*) malloc(sizeof(int)*pricesSize);
	memset(hold1, 0, sizeof(int)/sizeof(char)*pricesSize);

    buy[0] = -*prices;
    sell[0] = 0;
    hold0[0] = 0;
    hold1[0] = -*prices;
    
	for(i = 1; i < pricesSize; i++)
	{
		buy[i] = hold0[i-1] - prices[i];		

		sell[i] = max(buy[i-1], hold1[i-1]) + prices[i];

		hold0[i] = max(hold0[i-1], sell[i-1]);

		hold1[i] = max(hold1[i-1], buy[i-1]);
	}

	return max(sell[i-1], hold0[i-1]);	//it is impossible we get the max profit if we buy a stock on the last day
    
}



//below is the solution by state machine
//there are 3 state, s0, s1, s2;
//		<rest> s0 ---[buy]--> s1;		at s0, you can choose whether rest or buy
//		<rest> s1 ---[sell]-> s2;		at s1, you can choose whether rest or sell
//			   s2 ---[rest]-> s0;		at s2, you can only choose to rest

#define max(a,b) (a>b?a:b)

int maxProfit(int* prices, int pricesSize) {

	int *s0,*s1, *s2;
	int i;

	if(pricesSize <= 1)
		return 0;

	s0 = (int*) malloc(sizeof(int)*pricesSize);
	memset(s0, 0, sizeof(int)/sizeof(char)*pricesSize);
	s1 = (int*) malloc(sizeof(int)*pricesSize);
	memset(s1, 0, sizeof(int)/sizeof(char)*pricesSize);
	s2 = (int*) malloc(sizeof(int)*pricesSize);
	memset(s2, 0, sizeof(int)/sizeof(char)*pricesSize);

    s0[0] = 0;
    s1[0] = -*prices;
    s2[0] = 0;
    
	for(i = 1; i < pricesSize; i++)
	{
		//when you in s0[i], in the (i-1)-th day, you could either do rest at s2 or do rest at s0
		s0[i] = max(s2[i-1], s0[i-1]);		
		//when you in s1[i], in the (i-1)-th day, you could either do rest at s2 or do buy at s0
		s1[i] = max(s1[i-1], s0[i-1] - prices[i]);
		//when you in s2[i], in the (i-1)-th day, you could only do sell at s1
		s2[i] = s1[i-1] + prices[i];
	}

	return max(s0[i-1], s2[i-1]);
    
}
