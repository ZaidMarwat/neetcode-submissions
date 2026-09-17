class Solution:

    def encode(self, strs: List[str]) -> str:
        # if not strs:
        #     return ""
        arr = []
        for s in strs:
            arr.append(str(len(s)) + '#' + s)
        return ''.join(arr)


    def decode(self, s: str) -> List[str]:
        # if not s:
        #     return []
        ret = []
        skip = 0
        num = ""
        word = ""
        for c in s:
            if skip > 0:
                skip -= 1
                word += c
                if skip == 0:
                    ret.append(word)
                    word = ""
                continue
            
            if c != '#':
                num += c
            else:
                skip = int(num)
                num = ""
                if skip == 0:
                    ret.append("")
        
        return ret