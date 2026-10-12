class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char,int> charmap;
        int left= 0;
        int maxlength=0;
        for(int right=0;right<s.length();right++){
            char current = s[right];

            if(charmap.find(current)!= charmap.end() && charmap[current]>= left){
                left = charmap[current]+1;
            }

            charmap[current] = right;

            maxlength = max(maxlength,right-left+1);

        }
        return maxlength;
    }
};
