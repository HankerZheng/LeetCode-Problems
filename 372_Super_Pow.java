// Your task is to calculate ab mod 1337 where a is a positive
// integer and b is an extremely large positive integer given in
// the form of an array.

// Example1:

// a = 2
// b = [3]

// Result: 8
// Example2:

// a = 2
// b = [1,0]

// Result: 1024

public class Solution {
    public int superPow(int a, int[] b) {
        int res = 1;
        int base = a % 1337;
        for(int num: b){
            res = power1337(res, 10) * power1337(base, num) % 1337;
        }
        return res;
    }
    
    public int power1337(int a, int b){
        if (a == 0)  return 0;
        if (a == 1 || b == 0)  return 1;
        if (b == 1)  return a % 1337;
        
        int res = power1337(a, b / 2);
        res = res * res % 1337;
        return b%2==1 ? (res * a % 1337) : res;
    }
}