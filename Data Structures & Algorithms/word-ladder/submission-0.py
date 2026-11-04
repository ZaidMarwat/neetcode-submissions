class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        adj = defaultdict(list)
        for word in wordList:
            for word2 in wordList:
                if sum(1 for a,b in zip(word, word2) if a != b) == 1:
                    adj[word].append(word2)
        
        for word in wordList:
            if sum(1 for a,b in zip(word, beginWord) if a != b) == 1:
                adj[beginWord].append(word)
        
        print(adj)
        q = deque([beginWord])
        seen = {beginWord}
        count = 1
        while q and endWord not in seen:
            for _ in range(len(q)):
                print('in')
                word = q.popleft()
                for newWord in adj[word]:
                    if newWord not in seen:
                        q.append(newWord)
                        seen.add(newWord)

            count += 1
        print(count)
        return count if endWord in seen else 0
