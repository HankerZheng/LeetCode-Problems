public class Solution {
    public double myPow(double x, int n) {
        if ( x == 1 || n == 0) return 1.0;
        if (x == 0) return 0.0;
        if (n==1) return x;
        if (n==-1) return 1.0/x;
        
        double res = myPow(x, n / 2);
        if (n % 2 == 0){
            return res * res;
        }else if(n < 0){
            return res * res / x;
        }else{
            return res * res * x;
        }
    }
}