public class Solution {
    public double myPow(double x, int n) {
        if ( x == 1 || n == 0) return 1.0;
        if (x == 0) return 0.0;
        if (n==1) return x;
        if (n==-1) return 1.0/x;

        int power = n;
        double res = 1;
        double base = n > 0 ? x : (1.0 /x );
        while (power != 1 || power != -1){
            res = res * res;
            if (power % 2 == 1){
                res *= base;
            }
            power = power / 2;
        }
        return power * base;
    }
}
