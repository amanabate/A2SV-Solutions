# Problem: Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/submissions/

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not t or not s:
            return ""
        
        dict_t = Counter(t) 
        required = len(dict_t) 
        left, right = 0, 0
        formed = 0
        window_counts = {}
        min_len = float("inf")
        min_window = (0, 0)

        while right < len(s):
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1

            if char in dict_t and window_counts[char] == dict_t[char]:
                formed += 1

            while left <= right and formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_window = (left, right)

                window_counts[s[left]] -= 1
                if s[left] in dict_t and window_counts[s[left]] < dict_t[s[left]]:
                    formed -= 1
                left += 1

            right += 1

        if min_len != float("inf"):
            start, end = min_window  
            
            return s[start:end + 1]  
        else:
            return "" 

            