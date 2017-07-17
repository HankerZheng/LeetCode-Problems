// Given an integer n, return 1 - n in lexicographical order.

// For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

// Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.

// Show Company Tags



public class Solution {
    public List<Integer> lexicalOrder(int n) {
        List<Integer> ansList = new ArrayList();
        if (n < 10){
            for (int i= 1; i < n+1; i++){
                ansList.add(i);
            }
            return ansList;
        }
        
        for(int i=1; i<10; i++){
            addNewNumber(ansList, i, n);
        }
        return ansList;
    }
    
    public void addNewNumber(List ansList, int currentNum, int upperBound){
        ansList.add(currentNum);
        for (int i = 0; i < 10; i++){
            int newNumber = currentNum*10 + i;
            if (newNumber > upperBound){
                break;
            }
            addNewNumber(ansList, newNumber, upperBound);
        }
    }
}