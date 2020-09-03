class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s) 
        temp_map = [0] * n 

        i = 1
        j = 0   # length of the previous longest prefix suffix 

        temp_map[0] = 0    
        # Preprocessing the pattern
        while i < n: 
            if s[i] == s[j]: 
                j += 1
                temp_map[i] = j 
                i += 1
            else: 
                if j != 0: 
                    j = temp_map[j-1] 
                else: 
                    temp_map[i] = 0
                    i += 1
        length = temp_map[n-1] 
        
        if gt(length,0) and n%(n-length) == 0: 
            return True
        else: 
            return False
