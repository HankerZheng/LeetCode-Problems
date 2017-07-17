public class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> traverseList = new ArrayList();
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0){
            return traverseList;
        }
        int loRow = 0, hiRow = matrix.length, loCol = 0, hiCol = matrix[0].length;
        while (loRow < hiRow && loCol < hiCol){
            traverseList.addAll(roundTraverse(matrix, loRow++, hiRow--, loCol++, hiCol--));
        }
        return traverseList;
    }
    public List<Integer> roundTraverse(int[][] matrix, int loRow, int hiRow, int loCol, int hiCol){
        List<Integer> thisRound = new ArrayList();
        if (loRow+1 == hiRow){
            for (int col = loCol; col < hiCol; col++){
                thisRound.add(matrix[loRow][col]);
            }
        }else if(loCol+1==hiCol){
            for (int row = loRow; row < hiRow; row ++){
                thisRound.add(matrix[row][loCol]);
            }
        }
        else{
            for(int col = loCol; col < hiCol-1; col ++){
                thisRound.add(matrix[loRow][col]);
            }
            for(int row = loRow; row < hiRow-1; row ++){
                thisRound.add(matrix[row][hiCol-1]);
            }
            for(int col = hiCol-1; col >= loCol+1; col --){
                thisRound.add(matrix[hiRow-1][col]);
            }
            for(int row = hiRow-1; row>= loRow+1; row--){
                thisRound.add(matrix[row][loCol]);
            }
        }
        return thisRound;
    }
}