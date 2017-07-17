import java.util.*;

public class Solution {
    public String getPermutation(int n, int k) {
        StringBuilder sb = new StringBuilder();
        List<Integer> availableList = new LinkedList<>();
        for (int i = 1; i <= n ; i++){
            availableList.add(i);
        }
        int factTerm = 1;
        for (int i = 1; i < n ; i++){
            factTerm *= i;
        }
        int thisIndex = k - 1;
        while (sb.length() < n){
            sb.append(availableList.get(thisIndex/factTerm).toString());
            availableList.remove(thisIndex/factTerm);
            thisIndex = thisIndex % factTerm;
            factTerm /= Math.max(1, n - sb.length());
        }
        return sb.toString();
    }

}