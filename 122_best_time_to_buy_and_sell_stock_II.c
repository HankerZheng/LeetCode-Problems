/*
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Subscribe to see which companies asked this question
*/

int maxProfit(int* prices, int pricesSize) {
	int i;
	int lastDay = *prices;
	int toDay = *(prices+1);
	int profit = 0;

    if(pricesSize <= 1)
    	return 0;
    if(pricesSize == 2)
    	return (toDay - lastDay > 0)? (toDay - lastDay) : 0;

    for(i = 1; i<pricesSize; i++)
    {
    	toDay = *(prices+i);
    	if(toDay > lastDay)
    		profit += toDay - lastDay;
    	lastDay = toDay;
    }

    return profit;
}   