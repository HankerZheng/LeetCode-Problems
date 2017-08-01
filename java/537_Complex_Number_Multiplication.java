// Given two strings representing two complex numbers.

// You need to return a string representing their multiplication. Note i2 = -1 according to the definition.

// Example 1:
// Input: "1+1i", "1+1i"
// Output: "0+2i"
// Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
// Example 2:
// Input: "1+-1i", "1+-1i"
// Output: "0+-2i"
// Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
// Note:

// The input strings will not have extra blank.
// The input strings will be given in the form of a+bi, where the integer a and b will both belong to the range of [-100, 100]. And the output should be also in this form.


// Runtime: 11 ms


public class Solution {
    public String complexNumberMultiply(String a, String b) {
        ComplexNumber ca = parseComplex(a);
        ComplexNumber cb = parseComplex(b);
        return ca.multiply(cb).toString();
    }
    
    private ComplexNumber parseComplex(String a) {
        String[] nums = a.split("[+i]");
        return new ComplexNumber(Integer.parseInt(nums[0]), Integer.parseInt(nums[1]));
    }
}

class ComplexNumber {
    int real;
    int img;
    
    public ComplexNumber(int real, int img) {
        this.real = real;
        this.img = img;
    }
    public ComplexNumber multiply(ComplexNumber o) {
        int nreal = this.real * o.real - this.img * o.img;
        int nimg = this.img * o.real + this.real * o.img;
        this.real = nreal;
        this.img = nimg;
        return this;
    }
    
    public String toString() {
        return real + "+" + img + "i";
    }
}