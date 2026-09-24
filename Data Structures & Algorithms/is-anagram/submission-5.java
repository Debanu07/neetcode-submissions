class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character,Integer> h1= new HashMap<>();
        if(s.length() != t.length()){
            return false;
        }
        for (char c : s.toCharArray()){
            h1.put(c,h1.getOrDefault(c,0)+1);
        }
        for (char c : t.toCharArray()){
            if (!h1.containsKey(c)){
                return false;
            }
            h1.put(c,h1.get(c)-1);
            if (h1.get(c)<0){
                return false;
            }
        }
        return true;
    }
}
