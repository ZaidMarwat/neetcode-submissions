class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        m = {}
        for i in range(len(position)):
            m[position[i]] = (target-position[i])/speed[i]
        
        total = 0
        prevpos = -1
        m[prevpos] = float('-inf')
        for pos in sorted(position, reverse=True):
            if m[prevpos] < m[pos]:
                prevpos = pos
                total += 1
            
        return total