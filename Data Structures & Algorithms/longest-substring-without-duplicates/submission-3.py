class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
            
        st = set()
        length = len(s)
        start = 0
        end = 0
        result = 1
        
        st.add(s[start])
        for i in range(length - 1):
            end = i + 1
            if s[end] in st:
                result = max(result, end - start)
                while s[start] != s[end]:
                    st.remove(s[start])
                    start = start + 1
                st.remove(s[start])
                start = start + 1
            st.add(s[end])
        
        return max(result, end - start + 1)

            
            
            


