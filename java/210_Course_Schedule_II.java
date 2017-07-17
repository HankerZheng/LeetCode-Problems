// There are a total of n courses you have to take, labeled from 0 to n - 1.

// Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

// Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

// There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

// For example:

// 2, [[1,0]]
// There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1]

// 4, [[1,0],[2,0],[3,1],[3,2]]
// There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3]. Another correct ordering is[0,2,1,3].



public class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        HashMap<Integer, List<Integer>> edges = new HashMap();
        Queue<Integer> zeroDegree = new LinkedList();
        int[] order = new int[numCourses];
        int[] degrees = new int[numCourses];
        int idx;
        
        for (idx = 0; idx < numCourses; idx ++){
            edges.put(idx, new ArrayList());
        }
        for (int[] edge: prerequisites){
            edges.get(edge[1]).add(edge[0]);
            degrees[edge[0]] ++;
        }
        for (idx = 0; idx < numCourses; idx++){
            if (degrees[idx] == 0){
                zeroDegree.add(idx);
            }
        }
        idx = 0;
        while (!zeroDegree.isEmpty()){
            int thisCourse = zeroDegree.remove();
            order[idx++] = thisCourse;
            for(int nextCourse: edges.get(thisCourse)){
                if ((--degrees[nextCourse]) == 0){
                    zeroDegree.add(nextCourse);
                }
            }
        }
        return idx==numCourses? order: new int[0];
        
    }
}