// Given an absolute path for a file (Unix-style), simplify it.

// For example,
// path = "/home/", => "/home"
// path = "/a/./b/../../c/", => "/c"
// click to show corner cases.

public class Solution {
    public String simplifyPath(String path) {
        String[] paths = path.split("/");
        Deque<String> dirList = new ArrayDeque();
        for(String dirName: paths){
            if (dirName.equals("") || dirName.equals(".")){
                continue;
            }else if(dirName.equals("..") && dirList.size() != 0){
                dirList.removeLast();
            }else{
                dirList.add(dirName);
            }
        }
        if (dirList.size() == 0)    return "/";
        StringBuilder fianlPath = new StringBuilder();
        for (String dirName: dirList){
            fianlPath.append("/" + dirName);
        }
        return fianlPath.toString();
    }
}