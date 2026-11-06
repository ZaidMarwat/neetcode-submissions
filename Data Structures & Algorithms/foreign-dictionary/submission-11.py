class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(list)
        letters = set(words[0])
        indegree = defaultdict(int)
        for i in range(len(words)-1):
            word1, word2 = words[i], words[i+1]
            letters.update(word2)
            diff = False
            for ch1, ch2 in zip(word1,word2):
                if ch1 != ch2:
                    adj[ch1].append(ch2)
                    indegree[ch2] += 1
                    diff = True
                    break
            if not diff and len(word1) > len(word2):
                return ""

        q = deque([c for c in letters if indegree[c] == 0])
        res = ""
        while q:
            ch = q.popleft()
            res += ch
            for ch2 in adj[ch]:
                indegree[ch2] -= 1
                if indegree[ch2] == 0:
                    q.append(ch2)
        
        return res if len(res) == len(letters) else ""


