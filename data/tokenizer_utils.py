from typing import List, Dict

class Solution:
    def tokenize_numbers(self, numbers: List[int], vocab: Dict[str, int]) -> List[List[str]]:
        # Tokenize each number using greedy left-to-right longest match.
        # Return a list of token lists showing how each number gets split.
        pass
        result=[]
        for number in numbers:
            text=str(number)
            tokens=[]
            i=0
            while i<len(text):
                best_token=None
                for token in vocab:
                    if text.startswith(token,i):
                        if best_token is None or len(best_token)<len(token):
                            best_token=token
                if best_token==None:
                    raise ValueError(
                        f"No token found for '{text[i:]}'"
                    )
                tokens.append(best_token)
                i+=len(best_token)
            result.append(tokens)
        return result
                    
    def count_tokens(self, text: str, vocab: Dict[str, int]) -> int:
        # Count how many tokens the text uses with greedy tokenization.
        # Use greedy left-to-right longest match.
        pass
        tokens=[]
        i=0;
        while i<len(text):
            best_token=None
            for token in vocab:
                if text.startswith(token,i):
                    if best_token is None or len(best_token)<len(token):
                        best_token=token
            if best_token is None:
                raise ValueError(
                    f"no token found in '{text[i:]}'"
                )
            tokens.append(best_token)
            i+=len(best_token)
        return len(tokens)

    def fertility_score(self, text: str, vocab: Dict[str, int]) -> float:
        # Compute tokens-per-word ratio (fertility).
        # Higher = more expensive and less efficient.
        # Round to 4 decimal places.
        pass
        words=text.split()
        if words==0:
            return 0.0
        total_tokens=self.count_tokens(text,vocab)
        ans=total_tokens/len(words)
        return round(ans,4)
