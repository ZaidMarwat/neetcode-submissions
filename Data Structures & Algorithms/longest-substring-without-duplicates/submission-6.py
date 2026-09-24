class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        longest = 0
        l, r = 0, 1
        st = set()
        st.add(s[l])
        while r < len(s):
            if s[r] not in st:
                st.add(s[r])
                r += 1
            else:
                longest = max(longest, len(st))
                while s[r] in st:
                    st.remove(s[l])
                    l += 1
                st.add(s[r])
                r += 1
        
        longest = max(longest, len(st))

        return longest
        

