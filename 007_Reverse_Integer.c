/*
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Have you thought about this?
Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!

If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.

Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?

For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

Update (2014-11-10):
Test cases had been added to test the overflow behavior.

Subscribe to see which companies asked this question
*/


// 32-bit integer range [-2147483648, 2147483647]
#define int32MAX 2147483647
#define int32MIN -2147483648

int reverse(int x) {
    
    int input;
    int output = 0;
    int digit;
    int flag_max;
    int flag_sign;

    if(x == 0)
    	return 0;
    else if(x < 0)
    {
    	flag_sign = 0;  //input < 0
    	input = -x;
    }
    else
    {
    	flag_sign = 1;  //input > 0
    	input = x;
    }


    while(input != 0)
    {
    	digit = input  %10;
    	input = input /10;
    	flag_max = output <(int32MAX -digit) / 10 ;
    	if (flag_max == 0)
    		flag_max = (output == (int32MAX -digit) / 10)&&(digit <= 7);
    	if(flag_max == 0)	//overflow
    		return 0;

    	output = output *10 +digit;
    }

    return flag_sign ? output : -output;
}