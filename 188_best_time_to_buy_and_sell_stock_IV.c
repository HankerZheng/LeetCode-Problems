/*
Write a function to find the longest common prefix string amongst an array of strings.

Subscribe to see which companies asked this question
*/
/*
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Credits:
Special thanks to @Freezen for adding this problem and creating all test cases.

Subscribe to see which companies asked this question
*/
/*
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Credits:
Special thanks to @Freezen for adding this problem and creating all test cases.

Subscribe to see which companies asked this question
*/


//二维数组很容易出错
//在计算乘以的因子的地方, pricesSize, k, k+1 错了好几遍！！！

//ways to mallocate 2 dimension array:
/*
				//first allocate memory for rows ptrs
	Array = (int**) malloc(sizeof(int*)*rows);				//mallocate size should be sizeof(int*) !!!
	memset(Array, 0, sizeof(int*)*rows/sizeof(char));
				//second allocate memory for the whole matrix
	Array[0] = (int*) malloc(sizeof(int)*rows*colunms);
	memset(Array[0], 0, sizeof(int)*rows*colunms / sizeof(char));
				//then assign the address of each row to rows ptrs
	for(i = 1;i < rows; i++)
	{
		Array[i] = Array[i - 1] + colunms;
	}

	////OPERATION HERE/////

				//finally free all the space allocated
	free(Array[0]);
	free(Array);
*/



#define min(a,b) (a>b?b:a)
#define max(a,b) (a>b?a:b)

int maxProfit(int k, int* prices, int pricesSize) {

    int i,j;
    int profit;

    int priceToday;
    int priceYesterday;
    int transactionCount;
    int flag;

    int **local, **global;
    int diff_price;

//special case when pricesSize is 0 or 1;
    if(pricesSize <= 1)
    	return 0;

//calculate the profit and count under unlimmited transactions;
	profit = 0;
	priceYesterday = *prices;
	transactionCount = 0;
	flag = 0;
	for(i = 1; i < pricesSize; i++)
	{
		priceToday = prices[i];
		if(priceToday > priceYesterday)
		{
			profit += priceToday - priceYesterday;
			flag = 1;
		}
		else
		{
			transactionCount = (flag == 1) ? (transactionCount+1): transactionCount;
			flag = 0;
		}
		priceYesterday =  priceToday;
	}
	if( flag == 1)
		transactionCount++;

	if( k >= transactionCount)
		return profit;

//calculate the profit under normal cases
//two array local[i][j] and global[i][j]
//local[i][j],  having done the j-th transaction in the i-th day
//global[i][j], the max profit when having done j transactions in the first j-th day
	//initialization
	local = (int**) malloc(sizeof(int*)*pricesSize);
	memset(local, 0, sizeof(int*)*pricesSize/sizeof(char));
	local[0] = (int*) malloc(sizeof(int)*pricesSize*(k+1));
	memset(local[0],  0, sizeof(int)*pricesSize*(k+1) / sizeof(char));
	for(i = 1;i < pricesSize; i++)
		local[i] = local[i - 1] + k + 1;
		//finish allocating space for local[pricesSize][k+1]


	global = (int**) malloc(sizeof(int*)*pricesSize);
	memset(global, 0, sizeof(int*)*pricesSize/sizeof(char));
	global[0] = (int*) malloc(sizeof(int)*pricesSize*(k+1));
	memset(global[0], 0, sizeof(int)*pricesSize*(k+1) / sizeof(char));
	for(i = 1;i < pricesSize; i++)
		global[i] = global[i - 1] + k + 1;
		//finish allocating space for global[pricesSize][k+1]
	profit = 0;

	//main loop
	for(j = 1; j <= k; j++)
	{
		for(i = 1; i < pricesSize; i ++)
		{
				//difference between today and yesterday
			diff_price = prices[i] - prices[i - 1];
				//on i-th day and we sell stock on the i-th day,
					//1. we dont make any transaction on the (i-1)-th day,
					//		just buy and sell one stock on the i-th day with 0 profit but 1 transacntion count
					//2. we do make one transaction on the (i-1)-th day,
					//		finish the j-th transaction on the i-th day, because local[i-1][j] means that we must sell stock on (i-1)-th daytherefore, we only should plus diff
			local[i][j]  = max(global[i-1][j-1], local[i-1][j] + diff_price);
				//on i-th day, we could choose whether to make transaction or not
					//1. we dont make any transaction on i-th day, so MaxProfit remains in global[i-1][j]
					//2. we do finish one transaction on i-th day, which means we sell stock on i-th day with price prices[i]
			global[i][j] = max(global[i-1][j], local[i][j]);
		}
		//need to be {i-1}, because when we jump out of the loop, i has already been incremented;
		if(global[i-1][j] > profit)
			profit = global[i-1][j];
	}

	free(global[0]);
	free(local[0]);
	free(global);
	free(local);

	return profit;
}






//以下是使用一维数组存储数据的解法

#define min(a,b) (a>b?b:a)
#define max(a,b) (a>b?a:b)

int maxProfit(int k, int* prices, int pricesSize) {

    int i,j;
    int profit;

    int priceToday;
    int priceYesterday;
    int transactionCount;
    int flag;

    int *local, *global;
    int diff_price;

//special case when pricesSize is 0 or 1;
    if(pricesSize <= 1)
    	return 0;

//calculate the profit and count under unlimmited transactions;
	profit = 0;
	priceYesterday = *prices;
	transactionCount = 0;
	flag = 0;
	for(i = 1; i < pricesSize; i++)
	{
		priceToday = prices[i];
		if(priceToday > priceYesterday)
		{
			profit += priceToday - priceYesterday;
			flag = 1;
		}
		else
		{
			transactionCount = (flag == 1) ? (transactionCount+1): transactionCount;
			flag = 0;
		}
		priceYesterday =  priceToday;
	}
	if( flag == 1)
		transactionCount++;

	if( k >= transactionCount)
		return profit;

//calculate the profit under normal cases
//two array local[i][j] and global[i][j]
//local[i][j],  having done the j-th transaction in the i-th day
//global[i][j], the max profit when having done j transactions in the first j-th day
	//initialization
	local = (int*) malloc(sizeof(int)*pricesSize*(k+1));
	global = (int*) malloc(sizeof(int)*pricesSize*(k+1));
	memset(local,  0, sizeof(int)*pricesSize*(k+1) / sizeof(char));
	memset(global, 0, sizeof(int)*pricesSize*(k+1) / sizeof(char));
	profit = 0;

	//main loop
	for(j = 1; j <= k; j++)
	{
		for(i = 1; i < pricesSize; i ++)
		{
				//difference between today and yesterday
			diff_price = prices[i] - prices[i - 1];
				//on i-th day and we sell stock on the i-th day,
					//1. we dont make any transaction on the (i-1)-th day,
					//		just buy and sell one stock on the i-th day with 0 profit but 1 transacntion count
					//2. we do make one transaction on the (i-1)-th day,
					//		finish the j-th transaction on the i-th day, because local[i-1][j] means that we must sell stock on (i-1)-th daytherefore, we only should plus diff
			local[i*(k+1)+j]  = max(global[(i-1)*(k+1)+j-1], local[(i-1)*(k+1)+j] + diff_price);
				//on i-th day, we could choose whether to make transaction or not
					//1. we dont make any transaction on i-th day, so MaxProfit remains in global[i-1][j]
					//2. we do finish one transaction on i-th day, which means we sell stock on i-th day with price prices[i]
			global[i*(k+1)+j] = max(global[(i-1)*(k+1)+j], local[i*(k+1)+j]);
		}
		if(global[(i-1)*(k+1)+j] > profit)
			profit = global[(i-1)*(k+1)+j];
	}


	free(global);
	free(local);

	return profit;
}


