/*
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Subscribe to see which companies asked this question
*/


// if 	A[i] represents the max profit for the first i th day
// then	A[i+1] could be max{A[i], prices[i+1] - minPrices};
// when here comes the ith day, we could choose to sell stock at that day or not,
//		if we choose to sell stock at that day, then we must buy stock at the lowest prices of the first i-1 th day,
//		if we choose not to sell stock at that day, then we hold the profit as before!!!


#define min(a,b) (a>b?b:a)
#define max(a,b) (a>b?a:b)

int maxProfit(int* prices, int pricesSize)
{
	int *A;	//the max profit of the first i th day
	int i;
	int min = *prices;
	int result;

	if(pricesSize <= 1)
		return 0;

	A = (int*) malloc(sizeof(int)*pricesSize);

	memset(A, 0, pricesSize * sizeof(int) / sizeof(char));

	for(i = 0; i < pricesSize; i++)
	{
		min = min(prices[i] , min);
		A[i] = max(A[i-1], prices[i] - min);
	}

	result = A[pricesSize -1 ];
	free(A);
	return result;

    
}