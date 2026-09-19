from typing import List
from collections import Counter

class Solution:
    def get_merges(self, corpus: str, num_merges: int) -> List[List[str]]:
        # 1. Split corpus into a list of individual characters
        # 2. For each merge step:
        #    a. Count frequency of all adjacent token pairs
        #    b. Find the most frequent pair (break ties lexicographically)
        #    c. Merge all non-overlapping occurrences left to right
        #    d. Record the merge as [token_a, token_b]
        # 3. Return the list of merges performed
        pass
        token=list(corpus)
        merges=[]
        for a in range(num_merges):
            pair_count=Counter()
            for i in range(len(token)-1):
                pair=(token[i],token[i+1])
                pair_count[pair]+=1
            if not pair_count:
                break
            best_pair=min(
                pair_count,
                key=lambda x:(-pair_count[x],x)
            )
            merges.append([best_pair[0],best_pair[1]])
            new_tokens=[]
            i=0;
            while i<len(token):
                if i<len(token)-1 and (token[i],token[i+1])==best_pair:
                    new_tokens.append(token[i]+token[i+1])
                    i+=2
                else:
                    new_tokens.append(token[i])
                    i+=1
            token=new_tokens
        return merges
