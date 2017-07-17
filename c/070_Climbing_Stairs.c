/*
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Subscribe to see which companies asked this question
*/

//DP:
//for the last stairs, there are two way to get to it
//		1. get to last by climbing 1 stairs;	
//		2. get to last by climbing 2 stairs;
//therefore, we have 	methods_count[i] = methods_count[i-1] + methods_count[i-2]

int climbStairs(int n) {

	int i;
	int *methods_count;
	int result;

	if(n == 0)
		return 0;
	else if(n == 1)
		return 1;
	else if(n == 2)
		return 2;

	methods_count = (int *) malloc(sizeof(int)*(n+1));
	memset(methods_count, 0, sizeof(int)*(n+1)/sizeof(char));

	methods_count[1] = 1;
	methods_count[2] = 2;

	for(i = 3; i <= n; i ++)
		methods_count[i] = methods_count[i-1] + methods_count[i-2];

	result = methods_count[n];

	free(methods_count);

	return result;
    
}