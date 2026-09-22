class Solution:

    def encode(self, strs: List[str]) -> str:
        estr = ""
        for s in strs:
            estr += str(len(s)) + '#' + s
        
        return estr

    def decode(self, s: str) -> List[str]:
        ret = []
        num = ""
        skip = 0
        word = ""
        for ch in s:
            if skip:
                skip -= 1
                word += ch
                if skip == 0:
                    ret.append(word)
                    word = ""
                continue
            
            if ch == '#':
                skip = int(num)
                if skip == 0:
                    ret.append("")
                num = ""
            else:
                num += ch
        
        return ret

