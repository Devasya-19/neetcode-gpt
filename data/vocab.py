from typing import Dict, List, Tuple

class Solution:
    def build_vocab(self, text: str) -> Tuple[Dict[str, int], Dict[int, str]]:
        # Return (stoi, itos) where:
        # - stoi maps each unique character to a unique integer (sorted alphabetically)
        # - itos is the reverse mapping (integer to character)
        pass
        chars=sorted(list(set(text)))
        stoi={ch:i for i,ch in enumerate(chars)}
        itos={i:ch for i,ch in enumerate(chars)}
        return (stoi,itos)

    def encode(self, text: str, stoi: Dict[str, int]) -> List[int]:
        # Convert a string to a list of integers using stoi mapping
        pass
        encode= [stoi[c] for c in text]
        return encode

    def decode(self, ids: List[int], itos: Dict[int, str]) -> str:
        # Convert a list of integers back to a string using itos mapping
        pass
        decode=''.join(itos[i] for i in ids)
        return decode
