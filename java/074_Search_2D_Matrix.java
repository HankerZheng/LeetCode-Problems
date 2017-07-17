// Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

// Integers in each row are sorted from left to right.
// The first integer of each row is greater than the last integer of the previous row.
// For example,

// Consider the following matrix:

// [
//   [1,   3,  5,  7],
//   [10, 11, 16, 20],
//   [23, 30, 34, 50]
// ]
// Given target = 3, return true.

public class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix.length == 0 || matrix[0].length == 0)    return false;
        // first find the row
        int rowIdx = binarySearchRow(matrix, target);
        if (rowIdx < 0){
            return false;
        }
        int colIdx = binarySearch(matrix[rowIdx], target);
        return matrix[rowIdx][colIdx] == target;
    }
    
    public int binarySearch(int[] nums, int target){
        int left = 0, right = nums.length - 1;
        while (left <= right){
            int mid = left + (right - left) / 2;
            if(nums[mid] == target){
                return mid;
            }else if(nums[mid] < target){
                left = mid + 1;
            }else{
                right = mid - 1;
            }
        }
        return right;
    }
    public int binarySearchRow(int[][] matrix, int target){
        int left = 0, right = matrix.length - 1;
        while (left <= right){
            int mid = left + (right - left) / 2;
            int thisNum = matrix[mid][0];
            if(thisNum == target){
                return mid;
            }else if(thisNum < target){
                left = mid + 1;
            }else{
                right = mid - 1;
            }
        }
        return right;
    }
}