// Given a pattern and a string str, find if str follows the same pattern.

// Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

// Examples:
// pattern = "abba", str = "dog cat cat dog" should return true.
// pattern = "abba", str = "dog cat cat fish" should return false.
// pattern = "aaaa", str = "dog cat cat dog" should return false.
// pattern = "abba", str = "dog dog dog dog" should return false.
// Notes:
// You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.

public class Solution {
    public boolean wordPattern(String pattern, String str) {
        String[] words = str.split(" ");
        if(pattern.length() != words.length){
            return false;
        }
        Map <Character, String> char2Str = new HashMap();
        Map <String, Character> str2Char = new HashMap();
        
        for(int i = 0; i < words.length; i++){
            Character thisChar = new Character(pattern.charAt(i));
            String thisString = words[i];
            if ( !char2Str.containsKey(thisChar) && !str2Char.containsKey(thisString)){
                char2Str.put(thisChar, thisString);
                str2Char.put(thisString, thisChar);
            }else if (char2Str.getOrDefault(thisChar, "").equals(thisString) && str2Char.getOrDefault(thisString, ' ').equals(thisChar)){
                continue;
            }else{
                return false;
            }
        }
        return true;
    }
}