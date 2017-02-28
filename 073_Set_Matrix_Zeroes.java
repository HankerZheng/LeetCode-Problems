
// Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

// click to show follow up.

// Follow up:
// Did you use extra space?
// A straight forward solution using O(mn) space is probably a bad idea.
// A simple improvement uses O(m + n) space, but still not the best solution.
// Could you devise a constant space solution?

public class Solution {
    public void setZeroes(int[][] matrix) {
        if (matrix == null || matrix[0] == null) return;
        int m = matrix.length, n = matrix[0].length;
        boolean firstRow = false, firstCol = false;
        // traverse the first row
        for (int col = 0; col < n; col ++){
            if (matrix[0][col] == 0){
                firstRow = true;
                break;
            }
        }
        // traverse the first col
        for (int row = 0; row < m; row ++){
            if (matrix[row][0] == 0){
                firstCol = true;
                break;
            }
        }
        // traverse the rest cells in the matrix
        for(int row = 1; row < m; row ++){
            for (int col = 1; col < n; col++){
                if (matrix[row][col] == 0){
                    matrix[0][col] = 0;
                    matrix[row][0] = 0;
                }
            }
        }
        // make row Zero
        for (int row = 1; row < m; row++){
            if (matrix[row][0] == 0){
                makeRowZero(matrix, row);
            }
        }
        // make col Zero
        for(int col = 1; col < n; col++){
            if (matrix[0][col] == 0){
                makeColZero(matrix, col);
            }
        }
        if (firstRow)   makeRowZero(matrix, 0);
        if (firstCol)    makeColZero(matrix, 0);
    }
    
    public void makeRowZero(int[][] matrix, int rowIdx){
        for(int col = 0; col < matrix[0].length; col++){
            matrix[rowIdx][col] = 0;
        }
    }
    public void makeColZero(int[][] matrix, int colIdx){
        for(int row = 0; row < matrix.length; row++){
            matrix[row][colIdx] = 0;
        }
    }
}