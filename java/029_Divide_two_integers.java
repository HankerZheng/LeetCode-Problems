/** 
* Divide two integers without using multiplication, division and mod operator.
* If it is overflow, return MAX_INT.
*
* Time Consume: 40ms
* Corner Cases: (-1, 1), (1, -1), (-1, -1), (-2147438648, -1), (13, 0)
**/
class Solution {
    public int divide(int dividend, int divisor) {
        
        if (dividend == 0){
            return 0;
        } else if (divisor == 0){
            return Integer.MAX_VALUE;
        }
        
        boolean negative = (dividend > 0) ^ (divisor > 0);
        long left = Math.abs((long) dividend);
        long div = Math.abs((long) divisor);
        
        long res = 0;
        long factor = 0;
    
        
        while (div <= left){
            factor = 2;
            while (div * factor < left){
                factor <<= 1;
            }
            factor >>= 1;
            res += factor;
            left = left - factor * div;
        }
        res = negative? -res: res;
        if (res > Integer.MAX_VALUE || res < Integer.MIN_VALUE){
            return Integer.MAX_VALUE;
        }
        return (int) res;
        
    }
}
