/*
Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.

Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.

Subscribe to see which companies asked this question
*/

//it should be pow(10,i-1) rather than pow(10,i)!!!!!




//below is 98ms answer
#define int32MAX 2147483647
#define int32MIN -2147483648

bool isPalindrome(int x) {

	int i;
	int digit_count;
	int input = x;
	int digit;

	if( input == 0)
		return 1;
	else if(input < 0)
		return 0;       		//negetive number is not palindrome;

	for(digit_count = 0; input != 0; digit_count++)
		input = input /10;
	if(digit_count == 1)		// 1-digit number must be palindrome
		return 1;
		
    input = x;
	for(i = digit_count; i > 1 ; i = i - 2)
	{
		digit = input / pow(10,i-1) ;
		if(digit != input % 10)
			return 0;
		input = (input - digit * pow(10,i-1) ) /10;
	}
	return 1;
    
}



//below is 76ms answer
#define int32MAX 2147483647
#define int32MIN -2147483648

int my_pow(int a, int b)
{
	int answer = 1;
	for(i = 0; i < b; i++)
		answer *=a;

}
int get_ith_highest_digit(int n, int i)
{
    int input = n;
    int th = my_pow(10,i);
    for(;input>=th;input = input /10)
        ;
    return input%10;
}
bool isPalindrome(int x) {

	int i;
	int digit_count;
	int input = x;
	int digit;

	if( input == 0)
		return 1;
	else if(input < 0)
		return 0;       //negetive number is not palindrome;

    if(input < 10)      //1-digit number is a palindrome;
        return 1;
        
    for(i = 1; input >=10; i++)
    {
        digit = get_ith_highest_digit(input, i);
        if(digit != input %10)
            return 0;
        input = input/10;
    }
	return 1;
    
}