class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        
        # If s1 is longer than s2, its permutation cannot exist in s2
        if n1 > n2:
            return False
            
        # Frequency arrays for 26 lowercase English letters
        s1_count = [0] * 26
        s2_count = [0] * 26
        
        # Populate counts for s1 and the first window of s2
        for i in range(n1):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
            
        # If the first window matches, we are done
        if s1_count == s2_count:
            return True
            
        # Slide the window across s2
        for i in range(n1, n2):
            # Add character entering window from the right
            s2_count[ord(s2[i]) - ord('a')] += 1
            # Remove character leaving window from the left
            s2_count[ord(s2[i - n1]) - ord('a')] -= 1
            
            # Check if current window matches s1
            if s1_count == s2_count:
                return True
                
        return False
