import torch
import torch.nn as nn
from torchtyping import TensorType
from typing import List

class Solution:
    def get_dataset(self, positive: List[str], negative: List[str]) -> TensorType[float]:
        # 1. Build vocabulary: collect all unique words, sort them, assign integer IDs starting at 1
        # 2. Encode each sentence by replacing words with their IDs
        # 3. Combine positive + negative into one list of tensors
        # 4. Pad shorter sequences with 0s using nn.utils.rnn.pad_sequence(tensors, batch_first=True)
        pass
        all_sentence=positive+negative 
        result=[]
        store_words=set()
        for sentence in all_sentence:
            for word in sentence.split():
                store_words.add(word)
            # store_words.update(sentence.split())
        sorted_words=sorted(store_words)
        vocab={}
        for index,word in enumerate(sorted_words,start=1):
            vocab[word]=index
        for sentence in all_sentence:
            sen_list=[]
            for word in sentence.split():
                sen_list.append(vocab[word])
            sen_list=torch.tensor(sen_list)
            result.append(sen_list)
        result=nn.utils.rnn.pad_sequence(result,batch_first=True)
        return result
        
