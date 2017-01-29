/*
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Subscribe to see which companies asked this question

Show Tags
Show Similar Problems
*/

//A_i represents that when we complete the firest transaction in the i th day, the max profit we could get;
//	which means that we sell the first stock at exactly the i th day

//use two array to store relatively the max profit of the first ith day and the max profit of the last (n-i-1)th day
//then, use the old way, to get the final answer,
//after this optimation, the time complexity would be O(n)

#define min(a,b) (a>b?b:a)
#define max(a,b) (a>b?a:b)

int maxProfit(int* prices, int pricesSize) {

	int i;
	int maxPrice;
	int minPrice;
	int* first_i;
	int* last_i;
	int maxProfit = 0;
	int thisProfit = 0;

	if(pricesSize <= 1)
		return 0;

// calculate the max profit of the first ith day
	first_i = (int*) malloc(pricesSize * sizeof(int));
	memset(first_i, 0, pricesSize*sizeof(int)/sizeof(char));
	minPrice = prices[0];
	for(i = 0; i < pricesSize; i++)		// i = [0 .. pricesSize - 1]
	{
		if(i == 0)
		{
			first_i[i] = 0;
			continue;
		}
		if(prices[i] < minPrice)
			minPrice = prices[i];
		first_i[i] = max(first_i[i-1], prices[i] - minPrice);
	}

// calculate the max profit of the last (n-i)th day
// from the end to the start, we gona 
	last_i = (int*) malloc(pricesSize * sizeof(int));
	memset(last_i, 0, pricesSize*sizeof(int)/sizeof(char));
	maxPrice = prices[pricesSize - 1];
	for(i = pricesSize - 1; i >= 0; i--)	// i = [pricesSize - 1 .. 0]
	{
		if(i == pricesSize - 1)
		{
			last_i[i] = 0;
			continue;
		}
		if(prices[i] > maxPrice)
			maxPrice = prices[i];
		last_i[i] = max(last_i[i + 1], maxPrice - prices[i] );
	}
//assume the first transaction has been done in the ith day
	for(i = 0; i < pricesSize; i++)
	{
		thisProfit = first_i[i] + last_i[i];
		if(thisProfit > maxProfit)
			maxProfit = thisProfit;
	}
	
	free(last_i);
	free(first_i);
	return maxProfit;
}










//below is the O(n2) answer
//which exceeds the time limit!


#define min(a,b) (a>b?b:a)
#define max(a,b) (a>b?a:b)

int oneProfit(int* prices, int pricesSize)
{
	int i;
	int minPrice = *prices;
	int maxProfit = 0;
	int result;

	if(pricesSize <= 1)
		return 0;

	for(i = 0; i < pricesSize; i++)
	{
		minPrice = min(prices[i] , minPrice);
		maxProfit = max(maxProfit, prices[i] - minPrice);
	}

	return maxProfit;
}


int maxProfit(int* prices, int pricesSize) {

	int i;
	int maxPrice = 0;
	int thisProfit = 0;
	int minPrice = *prices;

	if(pricesSize <= 1)
		return 0;

	else if(i == 2)
		return oneProfit(prices, pricesSize);


	for(i = 1; i < pricesSize-1; i++)
	{
		if(prices[i] < minPrice)
		{	//today's price is lowest in the first ith day, no sell try today
			minPrice = prices[i];
			thisProfit = oneProfit(prices + i + 1, pricesSize - i - 1);
			if(thisProfit > maxPrice)
				maxPrice = thisProfit;
			continue;
		}
		else
		{	//today's price is not lowest in the first ith day, try end first sell today
			thisProfit = prices[i] - minPrice + oneProfit(prices + i + 1, pricesSize - i - 1);
			if(thisProfit > maxPrice)
				maxPrice = thisProfit;
		}

	}
	return maxPrice;
}