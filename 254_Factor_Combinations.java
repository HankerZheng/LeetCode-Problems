// Numbers can be regarded as product of its factors. For example,

// 8 = 2 x 2 x 2;
//   = 2 x 4.
// Write a function that takes an integer n and return all possible combinations of its factors.

// Note: 
// You may assume that n is always positive.
// Factors should be greater than 1 and less than n.
// Examples: 
// input: 1
// output: 
// []
// input: 37
// output: 
// []
// input: 12
// output:
// [
//   [2, 6],
//   [2, 2, 3],
//   [3, 4]
// ]
// input: 32
// output:
// [
//   [2, 16],
//   [2, 2, 8],
//   [2, 2, 2, 4],
//   [2, 2, 2, 2, 2],
//   [2, 4, 4],
//   [4, 8]
// ]


public class Solution {
    public List<List<Integer>> getFactors(int n) {
        List<List<Integer>> ansList = new ArrayList();
        int upperBound = (int) Math.sqrt(n) + 1; 
        for (int i = 2; i < upperBound; i++){
            if (n % i == 0 && n / i >= i){
                List<Integer> thisList = new ArrayList();
                thisList.add(i);
                thisList.add(n/i);
                ansList.add(thisList);
                List<List<Integer>> subres = getFactors(n/i);
                for (int idx = 0; idx < subres.size(); idx++){
                    if (subres.get(idx).get(0) >= i){
                        List<Integer> newAns = new ArrayList();
                        newAns.add(i);
                        newAns.addAll(subres.get(idx));
                        ansList.add(newAns);
                    }
                }
            }
        }
        return ansList;
    }
}