class Solution:
    def pushDominoes(self, dominoes: str) -> str:

        dominoes = list(dominoes)
        temp = [''] * len(dominoes)
        q = deque()
        
        for i, ch in enumerate(dominoes):
            if ch != '.':
                q.append((i,ch))
                
        while q:
            temp = defaultdict(str)
            for _ in range(len(q)):
                i, ch = q.popleft()
    
                if ch == 'L' and i > 0 and dominoes[i-1] == '.':
                    temp[i-1] += 'L'
                    q.append((i-1, 'L'))
                elif ch == 'R' and i < len(dominoes)-1 and dominoes[i+1] == '.':
                    temp[i+1] += 'R'
                    q.append((i+1, 'R'))
            for k,v in temp.items():
                if v == 'RL' or v == 'LR':
                    dominoes[k] = '.'
                else:
                    dominoes[k] = v

        
        return "".join(dominoes)

