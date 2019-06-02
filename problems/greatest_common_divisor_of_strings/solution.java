class Solution {
    public String gcdOfStrings(String s1, String s2) {
        if(s1 == null || s2 == null)
            return "";
        if(s1.charAt(0) != s2.charAt(0))
            return "";
        int len = gcd(s2.length(), s1.length());
        System.out.println("len = "+len);
        return s1.substring(0, len);           
    }
    
    private int gcd(int x, int y){
        return y != 0 ? gcd(y,x%y) : x;
    }
}